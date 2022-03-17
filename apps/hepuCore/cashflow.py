import numpy as np
import numpy_financial as npf


def cashflow(CAPEX, OPEX, output_yearly, WACC):
    NPV_OPEX = npf.pv(WACC, len(output_yearly), OPEX)
    NPV_tot = (-CAPEX + NPV_OPEX)
    NPV_output = npf.npv(WACC, (np.array(output_yearly) * 10 ** 3).reshape(20))  # kg of H2

    LCO_X = -NPV_tot / NPV_output
    # print(NPV_OPEX[i])
    return NPV_tot, NPV_output, LCO_X
