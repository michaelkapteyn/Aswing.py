from aswingpy import geometry, model, oper, params
import numpy as np

if __name__ == '__main__':

    #Vehicle name
    name = "dae_flex"

    #Create new (empty) geometry object and populate with data from a .asw file
    aswgeom = geometry.aswGeometry()
    aswgeom.readaswfile('inputfiles/' + name + '.asw')

    # Create a new parameter object
    paramOutput = ["Ax", "Ay", "Az", "Ux", "Uy", "Uz", "phi", "theta", "psi", "Peng1", "alpha"]
    sensorOutput = ["phi", "theta", "psi"];
    aswparam = params.aswParams(paramOutput, sensorOutput, maxNewtonIters=50, enableGraphics=False)

    # Define a new operating point
    aswoper = oper.aswOperatingPoint(Veas=1, Vias=1, altitude=1, loadFactor=1, constraints=oper.aswConstraints("right"))

    # Create an aswing model using the above objects
    aswmodel = model.aswModel(aswgeom, [aswoper], aswparam)

    aswmodel.solve()
    
