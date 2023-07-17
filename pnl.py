import numpy as np
from shrinkage import *
from MVO import *
from numpy import linalg as LA
import cvxpy as cp
import scipy

Assets=np.load('assets_.npy')
n=515
Assets=Assets[0:n,4000:5000]
SigmaTrue=np.cov(Assets)+10**-3*np.eye(Assets.shape[0],Assets.shape[0])
Returns=np.sum(Assets,axis=1)/Assets.shape[1]
XOpt=portfolio(SigmaTrue,0,Returns)



"""
Assets=np.load('AssetsSim.npy')
Assets=Assets.T

Returns=np.sum(Assets,axis=1)/Assets.shape[1]

Returns=np.sum(Assets,axis=1)/Assets.shape[1]
XOpt=portfolio(SigmaTrue,0,Returns)
"""



returnsOpt=Assets.T@XOpt[0]
np.save("Optimal.npy",returnsOpt)








j=0

sharperolling=[]
sharpeshrinkedrolling=[]
returnsrolling=[]

returnsshrinkedrolling=[]



T=30
t=20

while(j<Assets.shape[1]):




    AssetsTrain=Assets[:,j:j+T]
    AssetsTest=Assets[:,j+T:j+T+t]

    if j>T:

        for i in range(0, AssetsTrain.shape[1]):
            returnsrolling.append(AssetsTrain[:,i].T@X[0])
            returnsshrinkedrolling.append(AssetsTrain[:,i].T@XShrinkage[0])



    Sigma=np.cov(AssetsTrain)+10**-3*np.eye(AssetsTrain.shape[0],AssetsTrain.shape[0])









    Returns=np.sum(AssetsTrain,axis=1)/AssetsTrain.shape[1]



    X=portfolio(Sigma,0,Returns)




    XShrinkage=portfolio(covariance_shrinked(Sigma,0.01),0,Returns)



    for i in range(0, AssetsTest.shape[1]):
        returnsrolling.append(AssetsTest[:,i].T@X[0])
        returnsshrinkedrolling.append(AssetsTest[:,i].T@XShrinkage[0])




    j=j+T+t

    print(j)


print(returnsrolling)
print(returnsshrinkedrolling)




np.save("returns.npy",returnsrolling)
np.save("returnsshrinked.npy",returnsshrinkedrolling )
