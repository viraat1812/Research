import numpy as np
from numpy import linalg as LA
import math
import scipy

def covariance_shrinked(sigma,rho):
    x=[]
    lambda_,v_lambda=scipy.linalg.eigh(sigma)



    lambda__=solution(rho,lambda_,sigma)




    for i in range(0,sigma.shape[0]):
        x.append(lambda__*(1-(1/2)*(math.sqrt(lambda_[i]**2*lambda__**2+4*lambda_[i]*lambda__)-lambda_[i]*lambda__)))
    X_shrinked=np.zeros((sigma.shape[0],sigma.shape[0]))
    for i in range(0,sigma.shape[0]):


        X_shrinked=X_shrinked+x[i]*np.dot(np.transpose([v_lambda[i]]),[v_lambda[i]])
    return X_shrinked
def fun(gamma,*args):
    param=np.array(args)




    f1=0
    f2=0
    for i in range(1,param[0].shape[0]):
        f1=f1+param[0][i]

        f2=f2+math.sqrt(param[0][i]**2*gamma**2+4*gamma*param[0][i])

    return (param[0][0]**2-1/2*f1)*gamma-param[0][param[0].shape[0]-1]+1/2*f2

import numpy as np

def bisection(fun, a, b, tol,*args):


    arg=np.array(args)
    arg=arg[0]




    if np.sign(fun(a,arg)) == np.sign(fun(b,arg)):
        raise Exception("The scalars a and b do not bound a root")


    m = (a + b)/2


    if np.abs(fun(m,arg)) < tol:

        return m
    elif np.sign(fun(a,arg)) == np.sign(fun(m,arg)):

        return bisection(fun, m, b, tol,arg)
    elif np.sign(fun(b,arg)) == np.sign(fun(m,arg)):

        return bisection(fun, a, m, tol,arg)

def solution(rho, lambda_, sigma):

    args=np.append(rho,np.append(lambda_,sigma.shape[0]))


    p=sigma.shape[0]

    lam=lambda_.max()

    r=0
    for i in range(0,sigma.shape[0]):
        r=r+1/lambda_[i]
    root=bisection(fun,(p**2*lam+2*p*rho**2-p*math.sqrt(p**2*lam**2+4*p*rho**2*lam))/(2*rho**4),min(p/rho**2,1/rho*math.sqrt(r)),0.01,args)
    return root
