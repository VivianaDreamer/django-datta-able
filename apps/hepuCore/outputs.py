from PEMSEC import PEMSEC
import pandas as pd


def outputs(input, size, type):
    if type == 'PEM':
        SEC = PEMSEC
        P_min = 0.1  # % (%)Pnom
        P_max = 1.0  # % (%)Pnom

    ##add if alk and SOEC

    P_curtailment = pd.DataFrame(index=input.index)

    P_max = P_max * size
    P_min = P_min * size

    output = input
    output[output < P_min] = 0
    output[output > P_max] = P_max

    P_curtailment = output - input

    output = output.apply(lambda x: (x / (SEC(x / (size)))))

    return output, P_curtailment

#
