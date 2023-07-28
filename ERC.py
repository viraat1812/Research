import numpy as np
from scipy import optimize

def riskFun(x,*args):

    args=np.array(args)
    args=args[0]

    Sigma=args[0:args.shape[0]-1,:]
    ret=args[args.shape[0]-1,:]
    riskVar=0
    for i in range(0,x.shape[0]):
        for j in range(0,x.shape[0]):
            sigx=Sigma@x
            sigx=sigx.T
            riskVar=riskVar+(x[i]*sigx[i]-x[j]*sigx[j])**2

    return riskVar-ret@x.T


def normalize(x):
    return (np.sum(x)-1)

def nonnegative(x):
    return x


def riskParity(Sigma,ret):

    x0=np.ones([Sigma.shape[0],1])*1/Sigma.shape[0]

    args=np.append(Sigma,[ret.T],axis=0)

    cons=({'type':'eq','fun':normalize},{'type':'ineq','fun':nonnegative})

    xopt=optimize.minimize(riskFun, x0, constraints=cons,args=args,method='SLSQP',tol=1e-10)
    xopt=xopt['x']
    xopt=np.array(xopt)
    #print(xopt.shape)

    for i in range(0,xopt.shape[0]):
        sigx=Sigma@xopt
        print(xopt[i]*sigx[i])
        

    return xopt
