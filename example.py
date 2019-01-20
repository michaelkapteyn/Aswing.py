from aswingpy import geometry, model, oper
import numpy as np

if __name__ == '__main__':

    #Vehicle name
    name = "dae_flex"

    #Create new (empty) geometry object and populate with data from a .asw file
    aswgeom = geometry.aswGeometry()
    aswgeom.readfromasw('inputfiles/' + name + '.asw')


    # Create a new (empty) operating point object and populate with data from a .pnt file
    aswoper = oper.aswOperatingPoint()
    aswoper.readfrompt('inputfiles/' + name + '.pt')

    # Create an aswing model using the above objects
    aswmodel = model.aswModel(aswgeom, aswoper)

    # Run the above model in aswing, storing the results in the model object
