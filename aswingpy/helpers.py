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

def writedata(f, data, fmt='%G'):
    np.savetxt(f,np.atleast_2d(data), fmt, delimiter='    ', newline='\n')

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


bvardict = {
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
