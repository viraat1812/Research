import cvxpy as cp
import numpy as np
from shrinkage import *
import math


def portfolio(sigma,value,r):
    n=sigma.shape[0]



    x=cp.Variable(n)

    ret = r.T@x


    risk = cp.quad_form(x, cp.psd_wrap(sigma))


    #prob = cp.Problem(cp.Minimize(risk), [sum(x)==1, ret >= value, x >= 0])

    prob = cp.Problem(cp.Minimize(risk-ret), [sum(x)==1, x >= 0])

    prob.solve()

    return x.value,risk.value
