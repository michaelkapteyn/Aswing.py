# Functions relating to ".set" files
# Manipulates ASWING Settings, Parameters

from aswingpy.helpers import *
import numpy as np

class aswParams:
    def __init__(self, outputVars=[], sensorVars=[], maxNewtonIters = 50, enableGraphics = False):
        self.outputVars = outputVars;
        self.sensorVars = sensorVars;

        self.maxNewtonIters = maxNewtonIters;
        self.enableGraphics = enableGraphics;

    def encode(self):
        self.outputVarsEncoded = np.asarray([[outputVarsdict[v] if v in outputVarsdict else 0 for v in self.outputVars]]).transpose()
        self.sensorVarsEncoded = np.asarray([[sensorVarsdict[v], 0] if v in sensorVarsdict else 0 for v in self.sensorVars])
