# Contains methods for retrieving results after an aswing run
from aswingpy.helpers import *

class aswResults:
    def __init__(self, filepath=None, paramOutput=[], sensorOutput=[]):
        if filepath is not None:
            self.p, self.s = self.readoutfile(filepath,paramOutput,sensorOutput)

    def readoutfile(self, filepath, paramOutput, sensorOutput):

        #make sure  paramOutput and sensorOutput lists are ordered in the same way that ASWING outputs them
        paramOutputEncoded = np.asarray([[outputVarsdict[v] if v in outputVarsdict else 0 for v in paramOutput]]).transpose()
        sensorOutputEncoded = np.asarray([[sensorVarsdict[v] if v in sensorVarsdict else 0 for v in sensorOutput]]).transpose()
        paramOutput = [x for _,x in sorted(zip(paramOutputEncoded,paramOutput))]
        sensorOutput = [x for _,x in sorted(zip(sensorOutputEncoded,sensorOutput))]

        paramOutput = ["i", "t"]+ paramOutput
        with open(filepath, "r") as fp:
            #first two lines are comments
            fp.readline()
            fp.readline()
            #next two lines list variable info and values
            vars = fp.readline()
            vals = fp.readline().split()
            pDict = {}
            sDict = {}
            for pIdx, param in enumerate(paramOutput):
                pDict[param] = vals[pIdx]


            start = len(paramOutput)
            for pIdx, param in enumerate(sensorOutput):
                sDict[param] = [asnum(v) for v in vals[start+pIdx::len(sensorOutput)]]

            return pDict, sDict

# aswR = aswResults()
# paramOutput = ["Ux", "Uz", "Uy", "Rx", "Ry", "Rz", "phi", "theta", "psi", "alpha", "Lift", "CL", "Cm"]
# sensorOutput = ["Ux", "Uy", "Uz"];
# p,s = aswR.readoutfile("outfiles/dae.t",paramOutput, sensorOutput)
# print(p)
# print(s)
