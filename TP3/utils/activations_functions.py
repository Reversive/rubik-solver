import numpy as np
from enum import Enum
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

TANH_FUNC = lambda x, BETA: np.tanh(BETA * x)
EXP_FUNC = lambda x, BETA: 1/(1+np.exp(-2*BETA*x))
class ActivationFunctions(Enum):
    SIGN = {
        "act_func": lambda x, BETA: np.sign(x*BETA),
        "deriv_act_func": lambda x, BETA: 1,
        "output_transform": StandardScaler()
    }
    LINEAR = {
        "act_func": lambda x, BETA: x,
        "deriv_act_func": lambda x, BETA: 1,
        "output_transform": StandardScaler()
    }
    TANH = {
        "act_func": TANH_FUNC, 
        "deriv_act_func" : lambda x, BETA: BETA*(1 - TANH_FUNC(x, BETA)**2),
        "output_transform": MinMaxScaler(feature_range=(-1,1))
    }
    EXP = {
        "act_func": EXP_FUNC, 
        "deriv_act_func" : lambda x, BETA: EXP_FUNC(x, BETA)*(1 - EXP_FUNC(x, BETA)),
        "output_transform": MinMaxScaler() # default range is (0,1)
    }
    RELU = {
        "act_func": lambda x, BETA: np.maximum(0, BETA*x),
        "deriv_act_func" : lambda x, BETA: np.where(x > 0, BETA, 0),
        "output_transform": MinMaxScaler() # default range is (0,1)
    }
