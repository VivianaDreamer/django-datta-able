import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PPA_simulation import PPA_simulation
from costs import costs
from cashflow import cashflow


# Technical assessment
Operation_type='PPA'  #Implement list: 'PPA' or 'Onsite generation'

if Operation_type=='PPA':
   [H2_hourly, H2_annual, PPA_type, PPA_size, Elec_type, Elec_size]=PPA_simulation()

#if Operation_type=='Onsite generation':
    #
   
#Economic assessment
T=len(H2_annual.columns)# project financial horizon in years
WACC =0.07   

#total cost calculation
energy_cost=50 # user define USD/MWh
water_cost=3   #USD/m3
water_type='tap'  
[CAPEX_tot, OPEX_tot] = costs(Elec_type,Elec_size,PPA_type,PPA_size,energy_cost,water_cost,H2_annual)

#Cashflows
[NPV_H2,NPV_H2_output, LCOH] = cashflow(CAPEX_tot,OPEX_tot,H2_annual,WACC)

#Prints and plots
