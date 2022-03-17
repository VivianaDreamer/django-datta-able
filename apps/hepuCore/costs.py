import numpy as np
import numpy_financial as npf


def costs(Elec_type, Elec_size, PPA_type, PPA_size, energy_cost, water_cost, H2_annual):
    # CAPEX USD
    # specific Electrolyzer
    if Elec_type == 'PEM':
        sp_CAPEX_PEM_container = 1.2  # USD/W_ac tech, BOP and transport
        sp_CAPEX_PEM_development = 0.5  # USD/W_ac

    sp_tot_CAPEX_Elec = sp_CAPEX_PEM_container + sp_CAPEX_PEM_development

    # Total CAPEX
    CAPEX = Elec_size * sp_tot_CAPEX_Elec * 10 ** 6

    # OPEX
    sp_OM_electrolyzer = 0.02 * sp_CAPEX_PEM_container  # USD/W/year
    sp_tapwatercons = 16  # lts/kg H2

    if PPA_type == '24/7':
        hours = 8760
    if PPA_type == 'solar':
        hours = 10 / 24 * 365
    Energy_cost = energy_cost * PPA_size * hours
    OM_electrolyzer = sp_OM_electrolyzer * Elec_size * 10 ** 6
    Cost_Water = water_cost * sp_tapwatercons * float(H2_annual[0] * 10 ** 3)

    OPEX = Energy_cost + OM_electrolyzer + Cost_Water

    return CAPEX, OPEX
