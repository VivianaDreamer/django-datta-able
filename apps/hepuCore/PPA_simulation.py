import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PEMEL import PEM
from outputs import outputs


## General project definitions
def PPA_simulation():
    Project_name='Project1' #user input
    Location='Location X'   #user input
    COD=2024                #Start of production
    Horizon=20              #years of operation before decommisioning

    ## Define energy input
    energy_input=pd.DataFrame(np.ones(8760))    #Preliminary Input vector 
    PPA_type='24/7'                             #User to choose between 24/7 or solar
    PPA_size=10                                 #float(input('Input the nominal power of the PPA between 1-100 [MW]'))

    if PPA_type=='24/7':
        energy_input=energy_input*PPA_size
        
    #if PPA_type=='solar'
    #    for i in range (1,24):
    #        for j in range (1,365):

    ## Define type of electrolyzer
    Elec_type='PEM' #Select from a list: ALK, PEM, SOEC
    Elec_size=10 #float(input('Input the nominal power of the electrolyzer between 1-100 [MW]'))

    if Elec_type=='PEM':
        Elec=PEM
        deg=(PEM.deg)

    #if Elec_type=='ALK':
    #    Elec=ALK
    #if Elec_type=='SOEC':
    #    Elec=SOEC

    ## Define output vector
    [H2_output, P_curtailment]=outputs(energy_input,Elec_size,Elec_type)
    H2_hourly=pd.DataFrame(np.zeros([8760,20]))
    H2_annual=pd.DataFrame(np.zeros([1,20]))
    for i in range (0,20):
        H2_hourly[i]=H2_output*(1-i*deg)  #TONS/H
        H2_annual[i]=sum(H2_hourly[i])    #TONS/A
    return H2_hourly, H2_annual, PPA_type, PPA_size, Elec_type, Elec_size

#define replacements
