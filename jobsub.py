#!/usr/bin/env python

import os.path

codehome = "/afs/cern.ch/work/d/ddesouza/UIC/SPRACE/CMSSW_13_0_5/src/K0Star"
cmssource = "/afs/cern.ch/work/d/ddesouza/UIC/SPRACE/CMSSW_13_0_5/src/"
outfolder = "/eos/user/d/ddesouza/K0Star/HM250_Pbgoing/"

#os.system("python3 HTCondor_submit.py -i DATA_SAMPLES/HM250/pgoing/listoffiles_pPb_DATA_HM250_pgoing -v DATA_SAMPLES/HM250/pgoing/V0_HM250_pgoing -o "+str(outfolder)+"/K0Star_HM250_pgoing -n 3 -s K0StarHM250_pgoing -c "+str(cmssource)+" -p "+str(codehome))
#os.system("python3 HTCondor_submit.py -i DATA_SAMPLES/HM250/Pbgoing/listoffiles_pPb_DATA_HM250_Pbgoing -v DATA_SAMPLES/HM250/Pbgoing/V0_HM250_Pbgoing -o "+str(outfolder)+"/K0Star_HM250_Pbgoing -n 3 -s K0StarHM250_Pbgoing -c "+str(cmssource)+" -p "+str(codehome))
