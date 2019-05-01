""" Contains helper functions for the aswing package
"""

""" Author: Michael Kapteyn, Aerospace Computational Design Lab, MIT
"""

import os, sys
import numpy as np

# asnum: converts string s to an integer or float as appropriate
def asnum(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def writedata(f, data, fmt='%G', delimiter='    '):
    np.savetxt(f,np.atleast_2d(data), fmt, delimiter, newline='\n')

def isinline(line, stringtofind, rng):
    if len(line) < max(rng):
        return False
    else:
        return stringtofind in line[rng[0]-1:rng[1]]


def islineignored(line):
    return isinline(line,"!",[1,1]) or isinline(line,"#",[1,1]) or isinline(line,"%",[1,1]) or line.strip() == ""


def islineend(line):
    return isinline(line.lower(),"end",[1,3])


def parsedatablock(fp, line, idx, nvalue, nvalueswithoutmult=0):
    qadd = np.zeros(nvalue)
    qfac = np.ones(nvalue)
    fdata = np.zeros((1,nvalue))
    iline = 1

    while line:
        if islineend(line):
            break
        elif islineignored(line):
            pass

        elif isinline(line,"*",[1,1]):
            for i,val in enumerate(line[2:len(line)].split()):
                qfac[nvalueswithoutmult+i] = asnum(val)

        elif isinline(line,"+",[1,1]):
            for i,val in enumerate(line[2:len(line)].split()):
                qadd[nvalueswithoutmult+i] = asnum(val)
        else:
            rdat = np.zeros(nvalue)
            for i,val in enumerate(line.split()):
                print(val)
                rdat[i] = asnum(val)

            flinedata = np.multiply(rdat,qfac)+qadd
            if iline == 1:
                fdata = flinedata
            else:
                fdata = np.vstack((fdata,flinedata))
            iline = iline+1
        line = fp.readline()
        idx += 1
    return np.atleast_2d(fdata), line, idx


def parsebeamblock(fp, line, idx, nvalue):
    qadd = np.zeros(nvalue)
    qfac = np.ones(nvalue)
    fdata = np.zeros((1,nvalue))
    iline = 1
    beam_data_end = False
    while line:
        if islineend(line):
            beam_data_end = True
            return fdata, line, idx,beam_data_end
        elif isinline(line.strip(), "t", [1,1]):
            return fdata, line, idx,beam_data_end
        elif islineignored(line):
            pass

        elif isinline(line,"*",[1,1]):
            for i,val in enumerate(line[2:len(line)].split()):
                qfac[i] = asnum(val)

        elif isinline(line,"+",[1,1]):
            for i,val in enumerate(line[2:len(line)].split()):
                qadd[i] = asnum(val)
        else:
            rdat = np.zeros(nvalue)
            for i,val in enumerate(line.split()):
                rdat[i] = asnum(val)

            flinedata = np.multiply(rdat,qfac)+qadd
            if iline == 1:
                fdata = flinedata
            else:
                fdata = np.vstack((fdata,flinedata))
            iline = iline+1
        line = fp.readline()
        idx += 1
    return np.atleast_2d(fdata), line, idx, beam_data_end


globalbvardict = {
    "x" : [],
    "y" : [],
    "z" : [],
    "twist" : [],
    "EIcc" : [],
    "EInn" : [],
    "EIcn" : [],
    "EIcs" : [],
    "EIsn" : [],
    "GJ" : [],
    "EA" : [],
    "GKc" : [],
    "GKn" : [],
    "mgcc" : [],
    "mgnn" : [],
    "mg" : [],
    "Ccg" : [],
    "Ncg" : [],
    "Dmgcc" : [],
    "Dmgnn" : [],
    "Dmg" : [],
    "DCcg" : [],
    "DNcg" : [],
    "Cea" : [],
    "Nea" : [],
    "Cta" : [],
    "Nta" : [],
    "tdeps" : [],
    "tdgam" : [],
    "Cshell" : [],
    "Nshell" : [],
    "Atshell" : [],
    "radius" : [],
    "Cdf" : [],
    "Cdp" : [],
    "chord" : [],
    "Xax" : [],
    "alpha" : [],
    "Cm" : [],
    "CLmax" : [],
    "CLmin" : [],
    "dCLda" : [],
    "dCLdF1" : [],
    "dCLdF2" : [],
    "dCLdF3" : [],
    "dCLdF4" : [],
    "dCLdF5" : [],
    "dCLdF6" : [],
    "dCLdF7" : [],
    "dCLdF8" : [],
    "dCLdF9" : [],
    "dCLdF10" : [],
    "dCLdF11" : [],
    "dCLdF12" : [],
    "dCLdF13" : [],
    "dCLdF14" : [],
    "dCLdF15" : [],
    "dCLdF16" : [],
    "dCLdF17" : [],
    "dCLdF18" : [],
    "dCLdF19" : [],
    "dCLdF20" : [],
    "dCMdF1" : [],
    "dCMdF2" : [],
    "dCMdF3" : [],
    "dCMdF4" : [],
    "dCMdF5" : [],
    "dCMdF6" : [],
    "dCMdF7" : [],
    "dCMdF8" : [],
    "dCMdF9" : [],
    "dCMdF10" : [],
    "dCMdF11" : [],
    "dCMdF12" : [],
    "dCMdF13" : [],
    "dCMdF14" : [],
    "dCMdF15" : [],
    "dCMdF16" : [],
    "dCMdF17" : [],
    "dCMdF18" : [],
    "dCMdF19" : [],
    "dCMdF20" : [],
    "dCDdF1" : [],
    "dCDdF2" : [],
    "dCDdF3" : [],
    "dCDdF4" : [],
    "dCDdF5" : [],
    "dCDdF6" : [],
    "dCDdF7" : [],
    "dCDdF8" : [],
    "dCDdF9" : [],
    "dCDdF10" : [],
    "dCDdF11" : [],
    "dCDdF12" : [],
    "dCDdF13" : [],
    "dCDdF14" : [],
    "dCDdF15" : [],
    "dCDdF16" : [],
    "dCDdF17" : [],
    "dCDdF18" : [],
    "dCDdF19" : [],
    "dCDdF20" : []
}

outputVarsdict = {
"Ax" : 1,   #linear acceleration
"Ay" : 2,
"Az" : 3,
"alphax" : 4,   #ang.acc
"alphay" : 5,
"alphaz" : 6,
"Ux" : 7,   #velocity
"Uy" : 8,
"Uz" : 9,
"Wx" : 10,  #rot.rate
"Wy" : 11,
"Wz" : 12,
"Rx" : 13,  #position
"Ry" : 14,
"Rz" : 15,
"phi" : 16,     #bank
"theta" : 17,   #elev
"psi" : 18,     #head
"Flap1" : 19,
"Flap2" : 20,
"Flap3" : 21,
"Flap4" : 22,
"Flap5" : 23,
"Flap6" : 24,
"Flap7" : 25,
"Flap8" : 26,
"Flap9" : 27,
"Flap10" : 28,
"Flap11" : 29,
"Flap12" : 30,
"Flap13" : 31,
"Flap14" : 32,
"Flap15" : 33,
"Flap16" : 34,
"Flap17" : 35,
"Flap18" : 36,
"Flap19" : 37,
"Flap20" : 38,
"Peng1" : 39,
"Peng2" : 40,
"Peng3" : 41,
"Peng4" : 42,
"Peng5" : 43,
"Peng6" : 44,
"Peng7" : 45,
"Peng8" : 46,
"Peng9" : 47,
"Peng10" : 48,
"Peng11" : 49,
"Peng12" : 50,
"Int(Vi-Vic)dt" : 51,
"Int(be-bec)dt" : 52,
"Int(al-alc)dt" : 53,
"Int(Ph-Phc)dt" : 54,
"Int(Th-Thc)dt" : 55,
"Int(Ps-Psc)dt" : 56,
"Int(Wx-Wxc)dt" : 57,
"Int(Wy-Wyc)dt" : 58,
"Int(Wz-Wzc)dt" : 59,
"Int(a-g-ac)dt" : 60,
"Int(a-g-ac)dt" : 61,
"Int(a-g-ac)dt" : 62,
"xcg" : 63, #cg position
"ycg" : 64,
"zcg" : 65,
"V" : 66,
"beta" : 67,
"alpha" : 68,
"VIAS_ref" : 69,
"beta_ref" : 70,
"alpha_ref" : 71,
"Drag" : 72,
"Sideforce" : 73,
"Lift" : 74,
"CDi" : 75,
"CD" : 76,
"CY" : 77,
"CL" : 78,
"Cl" : 79,
"Cm" : 80,
"Cn" : 81,
"span eff." : 82
}

sensorVarsdict = {
"Ax" : 1,  #linear  acceleration
"Ay" : 2,
"Az" : 3,
"alphax" : 4,   #ang.acc
"alphay" : 5,
"alphaz" : 6,
"Ux" : 7,   #velocity
"Uy" : 8,
"Uz" : 9,
"Wx" : 10,  #rot.rate
"Wy" : 11,
"Wz" : 12,
"Rx" : 13,  #position
"Ry" : 14,
"Rz" : 15,
"phi" : 16,     #bank
"theta" : 17,   #elev
"psi" : 18,     #head
"V" : 19,
"beta" : 20,
"alpha" : 21,
"Fc" : 22, #forces
"Fs" : 23,
"Fn" : 24,
"Mc" : 25,  #moments
"Ms" : 26,
"Mn" : 27,
"rx" : 28,  #position
"ry" : 29,
"rz" : 30,
"ux" : 31,  #velocity
"uy" : 32,
"uz" : 33,
"Wx-Wxc dt" : 34,
"Wy-Wyc dt" : 35,
"Wz-Wzc dt" : 36,
"ax-axc dt" : 37,
"ay-ayc dt" : 38,
"az-azc dt" : 39,
"Vi-Vic dt" : 40,
"be-bec dt" : 41,
"al-alc dt" : 42,
"Ph-Phc dt" : 43,
"Th-Thc dt" : 44,
"Ps-Psc dt" : 45,
"Gamma" : 46,
"eps_max" : 47,
"tau" : 48
}
