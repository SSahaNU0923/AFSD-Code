#### **Case Description**



**Rotational Speed**: 400 rpm

**Travel Speed**: 100 mm/min

**Axial Pressure**: 5 MPa

**Dwell time**: 60 seconds





Follow the steps given below to run the simulation:



#### **Step 1: Mesh generation**

###### **Meshing rules**

**For the wall**: 1.5 mm along height and width, and 2 mm along the travel direction.

**For substrate below the wall**: 1.5 mm in width, 2 mm along the travel direction, and 1.67 mm in height.

**For the remaining portion of the substrate**: biased linearly from 1.5 mm near the wall to 6 mm at the outer periphery, and 1.67 mm in height.



Use any of your preferred programs or software (e.g., Abaqus) to discretize the domain and save the file as a "*.inp*" file. In our case, the mesh file is saved as ***thinwall.inp***.





#### **Step 2: Generation of Toolpath**

Run ***generate\_toolpath.py*** to generate the ***toolpath.crs*** file. You have to set the parameters, such as travel speed, dwell time, number of layers, layer length, and height of each layer to get the proper toolpath.





#### **Step 3: Preprocessing the mesh file**

Use the ***preprocess.py*** file, which calls the ***preprocessor.py*** function, the ***thinwall.inp***, and the ***toolpath.crs*** file to start the preprocessing. Once you run the code, the ***thinwall.k*** file will be generated and directly fed into the main program named ***AFSD\_new\_model.py***.



#### **Step 4: Run the AFSD simulation**

Run the ***AFSD\_new\_model.py*** file to initiate the simulation process. Make sure your folder contains the necessary files -- ***gamma\_afsd.py***, ***func.py***, and ***toolpath.crs***. Check that the temperature-dependent material properties, such as thermal conductivity, specific heat capacity, Young's modulus, yield strength, and thermal expansion coefficient, are located in the ***0\_properties*** folder.





#### **Step 4: Get the results**

The temperature and residual stress history will be saved for each second of the physical time simultaneously in the ***results*** folder. The files are in the "*.vtk*" format, which can be post-processed using any suitable software such as ***ParaView***.

