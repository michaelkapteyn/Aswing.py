""" Contains classes and methods for an ASWING model.
    A model consists of (at minimum) a geometry (configuration) definition.
    A model may also contain an operating point definition, a control law definition.
    A model can also contain results structures from running ASWING with the above files
"""

""" Author: Michael Kapteyn, Aerospace Computational Design Lab, MIT
"""
from aswingpy.helpers import *

class aswModel:
    def __init__(self, geometry, operatingPoint=[], controlLaw=[]):
        self.geometry = geometry
        self.oper = operatingPoint
        self.control = controlLaw
