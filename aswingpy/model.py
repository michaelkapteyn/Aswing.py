""" Contains classes and methods for an ASWING model.
    A model consists of (at minimum) a geometry (configuration) definition.
    A model may also contain an operating point definition, a control law definition.
    A model can also contain results structures from running ASWING with the above files
"""

""" Author: Michael Kapteyn, Aerospace Computational Design Lab, MIT
"""
from aswingpy.helpers import *
import subprocess as sp

class aswModel:
    def __init__(self, geometry, operatingPoints=[], params=[], controlLaw=[]):
        self.geometry = geometry
        self.operatingPoints = operatingPoints
        self.params = params
        self.control = controlLaw


    def writecmdfile(self, filepath = None):
        if filepath is None:
            filepath = 'runs/' + self.geometry.name + '.aswcmd'

        with open(filepath, "w+") as f:
            # load geometry file
            f.write("load "+self.geometry.name+".asw\n")

            # open graphics menu
            f.write("plpa\n")
            # disable graphics
            f.write("g\n\n")
            # enter oper menu
            f.write("oper\n")

            ## Settings common to every operating point
            f.write("k\n")

            # change max newton iters
            f.write("i\n")
            f.write(str(self.params.maxNewtonIters)+"\n")
            f.write("\n")
            # change parameter output
            f.write("p\n")
            f.write("s\n")
            self.params.encode()
            writedata(f,self.params.outputVarsEncoded)

            #next menu
            f.write("\n")

            # change sensor output
            writedata(f,self.params.sensorVarsEncoded,delimiter=' ')

            # prev menu
            f.write("\n\n")

            # set flight constraints
            f.write("%\n") # enable keyboard entry
            f.write("F\n") # start with free-flight
            f.write("b\n") # express rotations in global coordinates
            writedata(f,self.operatingPoints[0].constraints, delimiter=' ')

            # prev menu
            f.write("\n")

            # set altitude
            f.write("a\n")
            f.write(str(self.operatingPoints[0].altitude))
            f.write("\n\n")

            ## Configure each operating point
            for oper in self.operatingPoints:
                # set velocity
                f.write("!V ")
                f.write(str(oper.Vias))
                f.write("\n")
                f.write("n\n")
                f.write(str(oper.loadFactor))
                f.write("\n")
                f.write("!Ex ")
                f.write(str(oper.bankAngle))

            f.write("\n")
            # Apply and converge all of the above constraints to all operating points
            f.write("xx\n")
            # Open a menu: Parameter seq. plots,output
            f.write("p\n")
            # write parameters to a file (use default name [AC_NAME].t)
            f.write("w\n\n\n\n")
            # write operating point to a file
            f.write("ww\nout.txt\n")
            # quit ASWING
            f.write("\n\n\nquit\n")

    def solve(self):
        # write asw file
        self.geometry.writeaswfile()

        # write command file
        fname = 'runs/' + self.geometry.name + '.aswcmd'
        self.writecmdfile(fname)

        # call aswing and generate output file
        sp.check_call("aswing<"+fname)
        
        # [TODO] save output in aswResult class
