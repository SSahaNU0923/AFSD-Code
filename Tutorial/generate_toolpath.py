#------------------------------------------------------------------------------
# This file is part of AFSD-Code, adapted from:
# AM_Thermomechancial_Solver by Shuheng Liao
# https://github.com/ShuhengLiao/AM_Thermomechanical_Solver
# Orignial Cppyright (c) 2023 Shuheng Liao
# Modificiations Copyright (c) 2025 Sourav Saha
# Licensed under the MIT License; see LICENSE file for details
#------------------------------------------------------------------------------


def generate_toolpath(travel_speed_mm_min, dwell_time_s, num_layers, layer_length, z_increment):
    travel_speed = travel_speed_mm_min / 60.0  # mm/s
    dt = 0.1  # initial positioning time

    time = 0.0
    x, y, z = 0.0, 0.0, 0.0
    toolpath = []

    # Initial position
    toolpath.append((time, x, y, z, 0))

    # Move to starting point (y = -100, z = 0), no deposition
    time += dt
    y = -100.0
    z = z_increment
    toolpath.append((time, x, y, z, 0))

    for _ in range(num_layers):
        # Move forward while depositing
        state = 1
        duration = layer_length / travel_speed
        time += duration
        y += layer_length
        toolpath.append((time, x, y, z, state))

        # Dwell (no deposition)
        time += dwell_time_s
        y -= layer_length
        z += z_increment
        if z > num_layers * z_increment:
            break
        toolpath.append((time, x, y, z, 0))

    # Output the toolpath data
    print(f"{'time':<8}{'x':<8}{'y':<10}{'z':<8}{'state'}")
    for row in toolpath:
        print(f"{row[0]:<8.2f}{row[1]:<8.2f}{row[2]:<10.2f}{row[3]:<8.2f}{row[4]}")

    # Write to file
    with open("toolpath.crs", "w") as f:
        for row in toolpath:
            f.write(f"{row[0]:<8.2f}{row[1]:<8.2f}{row[2]:<10.2f}{row[3]:<8.2f}{row[4]}\n")

    print("Toolpath saved to 'toolpath.crs'")

# Now call the function AFTER it's defined

generate_toolpath(travel_speed_mm_min=100, dwell_time_s=60, num_layers=4, layer_length=200, z_increment=3)
