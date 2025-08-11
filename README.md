# AFSD-Code
This is a companion codebase for the article "A Surface-based Heat source Model for Thermomechanical Simulation of Additive Friction Stir Deposition Process . T.Ruvo, A. Sarker, S. Liao, S. Saha"

This codebase is based on the original codebase to be found in: https://github.com/NU-IDEAS-Lab/ded_dt_thermomechanical_solver


Paper: A GPU-accelerated FEM solver for residual stress simulation in additive manufacturing using CuPy


Authors: Shuheng Liao, Ashkan Golgoon


Additional programming by Rujing Zha and Anthony Goeckner.


Paper: Liao, S., Golgoon, A., Mozaffar, M., & Cao, J. (2023). Efficient GPU-accelerated thermomechanical solver for residual stress prediction in additive manufacturing. Computational Mechanics, 71(5), 879-893

The current implementation modifies the orginal source code, adds the new thermal model, and implements for AFSD simulation. 

To understand how to generate the toolpath and geometry file, please refer to the original distribution: https://github.com/NU-IDEAS-Lab/ded_dt_thermomechanical_solver

The current implementation has all the dependecies mentioned and requires the same packages mentioned in https://github.com/NU-IDEAS-Lab/ded_dt_thermomechanical_solver 

The input geometry is provided for one case as representative case. Other cases will be released upon publication. 
