""" Contains classes and methods for ASWING geometry (configuration) definition
"""

""" Author: Michael Kapteyn, Aerospace Computational Design Lab, MIT
"""
from aswingpy.helpers import *
class aswGeometry:
	def __init__(self, name=[], units=[], constants=[], reference=[], weights=[], sensors=[], engines=[], struts=[], joints=[], jangles=[], grounds=[], beams={}):
		self.name = name
		self.units = units
		self.constants = constants
		self.reference = reference
		self.weights = weights
		self.sensors = sensors
		self.engines = engines
		self.struts = struts
		self.joints = joints
		self.jangles = jangles
		self.ground = grounds
		self.beams = beams

	def readfromasw(self, filepath):
	    self.name = []
	    self.units = []
	    self.constants = []
	    self.reference = []
	    self.weights = []
	    self.sensors = []
	    self.engines = []
	    self.struts = []
	    self.joints = []
	    self.jangles = []
	    self.grounds = []
	    self.beams = {} #dict

	    with open(filepath) as fp:
	        line = fp.readline()
	        idx = 1
	        while line:
	            # Check for and read name block
	            if isinline(line.lower(),"name",[1,4]):
	                print("\nReading Name: ")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        self.name = line
	                        print("Name is:", self.name)
	                line = fp.readline()
	                idx += 1

	            # Check for and read units block
	            elif isinline(line.lower(),"unit",[1,4]):
	                print("\nReading Units:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        splitline = line.split()
	                        if splitline[0].lower() == "l":
	                            lengthUnits = splitline[2]
	                            print("Length unit is", lengthUnits)
	                        elif splitline[0].lower() == "t":
	                            timeUnits = splitline[2]
	                            print("Time unit is", timeUnits)
	                        elif splitline[0].lower() == "f":
	                            forceUnits = splitline[2]
	                            print("Force unit is", forceUnits)
	                line = fp.readline()
	                idx += 1
	                self.units = units(lengthUnits, timeUnits, forceUnits)

	            # Check for and read constants block
	            elif isinline(line.lower(), "cons", [1,4]):
	                print("\nReading Constants:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        splitline = line.split()
	                        g = asnum(splitline[0])
	                        rhoSL = asnum(splitline[1])
	                        SoSSL = asnum(splitline[2])
	                        print("Gravity is", g)
	                        print("Density is", rhoSL)
	                        print("Speed of sound is", SoSSL)

	                self.constants = constants(g, rhoSL, SoSSL)
	                line = fp.readline()
	                idx += 1

	            # Check for and read reference values block
	            elif isinline(line.lower(), "refe", [1,4]):
	                print("\nReading Reference Values:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 3)
	                        area = data[0,0]
	                        chord = data[0,1]
	                        span = data[0,2]
	                        moments = data[1,:]
	                        print("Area is", area)
	                        print("chord is", chord)
	                        print("span is", span)
	                        print("moments are", moments)
	                        break

	                self.reference = reference(area, chord, span, moments, np.zeros((3,1)), np.zeros((3,1)))
	                line = fp.readline()
	                idx += 1

	            # Check for and read weight block
	            elif isinline(line.lower(), "weig", [1,4]):
	                print("\nReading Weight Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 14, 1)
	                        for row in data:
	                            if len(row) == 11:
	                                self.weights.append(weight(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
	                            else:
	                                self.weights.append(weight(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))
	                        print("Weight data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            # Check for and read sensor block
	            elif isinline(line.lower(), "sens", [1,4]):
	                print("\nReading Sensor Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 12, 2)
	                        for row in data:
	                            if len(row) == 6:
	                                self.sensors.append(sensor(row[0], row[1], row[2], row[3], row[4], row[5]))
	                            else:
	                                self.sensors.append(sensor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
	                        print("Sensor data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            # Check for and read engine block
	            elif isinline(line.lower(), "engi", [1,4]):
	                print("\nReading Engine Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 25, 3)
	                        for row in data:
	                            if len(row) == 11:
	                                self.engines.append(engine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
	                            elif len(row) == 15:
	                                self.engines.append(engine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))
	                            else:
	                                self.engines.append(engine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24]))
	                        print("Engine data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            # Check for and read strut block
	            elif isinline(line.lower(), "stru", [1,4]):
	                print("\nReading Strut Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 10, 1)
	                        for row in data:
	                            self.struts.append(strut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
	                        print("Strut data", data)
	                        break
	                line = fp.readline()
	                idx += 1


	            # Check for and read joint block
	            elif isinline(line.lower(), "join", [1,4]):
	                print("\nReading Joint Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 4, 2)
	                        for row in data:
	                            if len(row) == 4:
	                                self.joints.append(joint(row[0], row[1], row[2], row[3]))
	                            else:
	                                self.joints.append(joint(row[0], row[1], row[2], row[3], row[4]))
	                        print("Joint data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            # Check for and read jangle blocks
	            elif isinline(line.lower(), "jang", [1,4]):
	                print("\nReading Jangle Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 4, 2)
	                        self.jangles.append(jangle(data[0,0], data[0,1], data[0,2], data[0,3], data[1:,0], data[1:,1]))
	                        print("Jangle data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            # Check for and read ground block
	            elif isinline(line.lower(), "grou", [1,4]):
	                print("\nReading Ground Block:")
	                while line:
	                    line = fp.readline()
	                    idx += 1
	                    if islineignored(line):
	                        pass
	                    elif islineend(line):
	                        break
	                    else:
	                        data, line, idx = parsedatablock(fp, line, idx, 3, 1)
	                        for row in data:
	                            if len(row) == 2:
	                                self.grounds.append(ground(row[0], row[1]))
	                            else:
	                                self.grounds.append(ground(row[0], row[1], row[2]))
	                        print("Ground data", data)
	                        break
	                line = fp.readline()
	                idx += 1

	            elif isinline(line.lower(), "beam", [1,4]):
	                print("\nReading Beam Blocks:")

	                #Incremenet the beam counter
	                # nbeam = nbeam+1

	                # Read beam number and optional physical index
	                splitline = line.split()
	                beamIdx = asnum(splitline[1])
	                if len(splitline) > 2:
	                    physicalIdx = asnum(splitline[2])
	                else:
	                    physicalIdx = beamIdx

	                #Read the beam name
	                line = fp.readline()
	                idx+=1

	                beam_name = line.strip("\n")
	                print(beam_name)
	                line = fp.readline()
	                idx += 1
	                line = fp.readline()
	                idx += 1
	                beam_data_end = False
	                while not beam_data_end:

	                    bvar = line.split()
	                    print(bvar)
	                    if bvar[0] != "t":
	                        print("Warning: First beam variable must be t")
	                    line = fp.readline()
	                    idx += 1
	                    data, line, idx, beam_data_end = parsebeamblock(fp, line, idx, len(bvar))
	                    for i in range(1,len(bvar)):
	                        if bvar[i] not in bvardict:
	                            print("Warning: variable ", bvar[i] , " is not a valid variable")
	                        else:
	                            bvardict[bvar[i]] = data[:,[0, i]]
	                    if beam_data_end:
	                        break
	                self.beams[beam_name] = beam(beamIdx, physicalIdx, beam_name, bvardict)
	            else:
	                pass

	            line = fp.readline()
	            idx += 1



class units:
	def __init__(self, lengthUnits, timeUnits, forceUnits):
		self.length = lengthUnits
		self.time = timeUnits
		self.force = forceUnits

class constants:
	def __init__(self, g, rho, V):
		self.sea_level_air_density = rho
		self.sea_level_speed_of_sound = V
		self.gravity = g

class reference:
    def __init__(self, area, chord, span, mom, acc, vel):
        self.area = area
        self.chord = chord
        self.span = span
        self.mom = mom
        self.acc = acc
        self.vel = vel

class weight:
    #This allows specification of "point-masses", or point-objects to be more precise.
    def __init__(self, beamIdx, t, Xp, Yp, Zp, Mg, CDA, Vol, Hx, Hy, Hz, Ix = 0, Iy = 0, Iz = 0):
        #Each point-mass possesses mass, and also angular momentum,
        # aerodynamic drag-area, and aerodynamic volume.  Each is cantilevered from
        # a surface or fuselage beam via a massless rigid pylon.  The pylon attachment
        # point is at location t on the reference axis of beam "beamIdx"
        self.beamIdx = beamIdx
        self.t = t

        #The other free end of the pylon is specified by the cartesian
        # coordinates Xo, Yo, Zo, which is where the point-mass is located
        # in the undeformed state (i.e. when the beam has its jig shape).
        # The pylon is assumed to be rigid (infinitely stiff), and will wave
        # the point-mass around as the beam section at t moves and rotates
        # during deformation.  The angular momentum vector's direction will
        # also change accordingly.
        self.Xp = Xp
        self.Yp = Yp
        self.Zp = Zp

        # Weight (NOT mass) of the object
        self.Mg = Mg

        #The aero drag force vector D on the point mass is calculated from the
        # specified drag area CDA as
        #  _             _
        #  D = 0.5 rho V V  CDA
        #       _                                                     _
        # where V is the net local relative velocity vector, and V = |V|.
        self.CDA = CDA

        # Aerodynamic Volume
        self.Vol = Vol

        self.Hx = Hx
        self.Hy = Hy
        self.Hz = Hz

        self.Ix = Ix
        self.Iy = Iy
        self.Iz = Iz

class sensor:
    def __init__(self, sensorIdx, beamIdx, t, Xp, Yp, Zp, Vx = 1, Vy = 0, Vz = 0, Ax = 0, Ay = 0, Az = 1):
	    self.sensorIdx = sensorIdx
	    self.beamIdx = beamIdx
	    self.t = t
	    self.Xp = Xp
	    self.Yp = Yp
	    self.Zp = Zp
	    self.Vx = Vx
	    self.Vy = Vy
	    self.Vz = Vz
	    self.Ax = Ax
	    self.Ay = Ay
	    self.Az = Az

class engine:
	def __init__(self, engIdx, engType, beamIdx, t, Xp, Yp, Zp, Tx, Ty, Tz, dFdPe, dMdPe=0, Rdisk=0, Omega=0, cdA = 0, cl=0, CLa=0, S0=0, C0=0, S1=0, C1=0, S2=0, C2=0, S3=0, C3=0):

		self.engIdx = engIdx
		# Currently, aswing supports three engine types:
		#
		#  type 0: A simple proportional engine model.  Peng is an arbitrary control variable,
		#          and thrust and torque are set using the two gains:
		#             T = dFdPe*Peng
		#             Q = dMdPe*Peng
		#             F = ( Tx , Ty , Tz ) * T
		#             M = ( Ty , Ty , Tz ) * Q
		#
		#  type 1: An extended actuator-disk model, with thrust and torque set by the model
		#             T = f( Peng , rho , V , Rdisk )
		# 	    Q = Peng/Omega
		#
		# type 2: Same as type 1, with added P-factor terms for prop whirl prediction
		#
		# The Steady theory document asw.ps describes types 0 and 1.
		# The Unsteady theory document aswu.ps describes the added terms in type 2.
		self.engType = engType
		self.beamIdx = beamIdx
		self.t = t
		self.Xp = Xp
		self.Yp = Yp
		self.Zp = Zp
		self.Tx = Tx
		self.Ty = Ty
		self.Tz = Tz
		self.dFdPe = dFdPe
		self.dMdPe = dMdPe

		# for engine type 1
		self.Rdisk = Rdisk
		self.Omega = Omega
		self.cdA = cdA

		# for engine type 2
		self.cl = cl
		self.CLa = CLa
		self.S0 = S0
		self.C0 = C0
		self.S1 = S1
		self.C1 = C1
		self.S2 = S2
		self.C2 = C2
		self.S3 = S3
		self.C3 = C3


class strut:
    def __init__(self,beamIdx, t, Xp, Yp, Zp, Xw, Yw, Zw, dL, EAw):
        # This allows the specification of struts or wires, each of which is attached
        # at the end of a rigid pylon cantilevered from the specified t location
        # of beam number "beamIdx"
        self.beamIdx = beamIdx
        self.t = t

        # Xp, Yp, Zp, give the location for the other pylon
        # endpoint just like for the point-masses.  Here, this other endpoint is
        # where one end of the strut is attached.
        self.Xp = Xp
        self.Yp = Yp
        self.Zp = Zp

        # Xw, Yw, Zw give the location of the anchor at the other end of
        # the strut.  This other end is assumed to be grounded (i.e. fixed
        # in the x,y,z coordinate system).
        self.Xw = Xw
        self.Yw = Yw
        self.Zw = Zw
        self.dL = dL

        # EAw is the extensional stiffness of the strut.  It can be made huge
        # to simulate an effectively-rigid strut.
        #
        # As in the case of point-masses, multiple struts at the same location
        # have their contributions superimposed.  The net effective EA is simply
        # the sum of the individual EA values.
        self.EAw = EAw

class joint:
	def __init__(self, beam1Idx, beam2Idx, t1, t2, jointType = 0):
		# This allows specification of some number of "joints" between
		# pairs of beams.
		# A joint is a rigid pylon linking the two beams at the specified t locations.
		self.beam1Idx = beam1Idx
		self.beam2Idx = beam2Idx
		self.t1 = t1
		self.t2 = t2

		# The optional KJtype indicator specifies the type of joint:
		#
		# KJtype = 0:  Both translation and rotation matched    (rigid  joint)
		#  1:  Only translation matched                 (pinned joint)
		#  2:  Only rotation matched                    (roller joint)
		#  3:  translation matched, two angles matched,
		#      one remaining angle depends on moment    (sprung-hinge joint)
		self.jointType = jointType

class jangle:
	def __init__(self, jointIdx, hx, hy, hz, Momh, Angh):
		self.jointIdx = jointIdx
		self.hx = hx
		self.hy = hy
		self.hz = hz
		self.Momh = Momh
		self.Angh = Angh


class ground:
	def __init__(self, beamIdx, t, groundType =0):
		self.beamIdx = beamIdx
		self.t = t
		self.groundType = 0

class beam:
	def __init__(self, beamIdx, physicalIdx, name, spanwise):
		self.beamIdx = beamIdx
		self.physicalIdx = physicalIdx
		self.name = name
		self.spanwise = spanwise
