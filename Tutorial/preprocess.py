#------------------------------------------------------------------------------
# This file is part of AFSD-Code, adapted from:
# AM_Thermomechancial_Solver by Shuheng Liao
# https://github.com/ShuhengLiao/AM_Thermomechanical_Solver
# Orignial Cppyright (c) 2023 Shuheng Liao
# Modificiations Copyright (c) 2025 Sourav Saha
# Licensed under the MIT License; see LICENSE file for details
#------------------------------------------------------------------------------

from preprocessor import write_keywords,write_birth,write_parameters

import time
import numpy as np


file_name = 'thinwall.inp' #input mesh file from abaqus
toolpath_file = 'toolpath.crs'
output_file = 'thinwall.k' #define keyword file name

substrate_height = 0
radius = 15
path_resolution = 0.75 # half of the element size
write_keywords(file_name,output_file,substrate_height)
write_birth(output_file,toolpath_file,path_resolution,radius,gif_end=5,nFrame=50,mode=1,camera_position=[(0, -50, 75),(0, 0, 0),(0.0, 0.0, 1.0)])

write_parameters(output_file)
