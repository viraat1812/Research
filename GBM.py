import numpy as np
import math
import matplotlib.pyplot as plt


def gbm(mu,sigma,Mu,Sigma,correlation,X0,N,epsilon):
    dt=1/365
    mu=mu/100
    sigma=sigma/100
    X=X0
    BrownianPath=[]
    corr=np.eye(Mu.shape[1],Mu.shape[1])*epsilon+ correlation
    for i in range(0,N):

        Z=np.random.normal(Mu,Sigma,size=(1,Mu.shape[1]))
        Z=np.linalg.cholesky(corr)@(Z.T)

        X=X*np.exp((mu-1/2*sigma*sigma)*dt+(sigma*Z.T*math.sqrt(dt)))

        BrownianPath.append(X[0])
    BrownianPath=np.array(BrownianPath)

    return BrownianPath
