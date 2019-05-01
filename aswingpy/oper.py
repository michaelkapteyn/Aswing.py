""" Contains classes and methods for ASWING operating point definition
"""

""" Author: Michael Kapteyn, Aerospace Computational Design Lab, MIT
"""
from aswingpy.helpers import *

class aswOperatingPoint:
    def __init__(self, Veas, Vias, altitude, loadFactor, constraints = []):
        self.Veas = Veas
        self.Vias = Vias
        self.altitude = altitude
        self.loadFactor = loadFactor
        self.bankAngle = -np.rad2deg(np.arccos(1/loadFactor))
        if constraints is None:
            constraints = aswConstraints()
        self.constraints = constraints


def aswConstraints(maneuver = ""):
    if "level" in maneuver.lower():
        constraints = np.array( [[9, 31],\
                                [17, 1],\
                                [21, 4],\
                                [22, 5],\
                                [23, 6],\
                                [24, 32]])
    elif "right" in maneuver.lower():
        constraints = np.array([[21, 4],\
                                [22, 5],\
                                [23, 6],\
                                [17, 1],\
                                [12, 33],\
                                [24, 32],\
                                [9 , 3]])

    elif "left" in maneuver.lower():
        constraints = np.array([[21, 4],\
                                [22, 5],\
                                [23, 6],\
                                [17, 1],\
                                [12, 33],\
                                [24, 32],\
                                [9 , 3]])

    else: #operate in a vacuum
        constraints = None

    return constraints
