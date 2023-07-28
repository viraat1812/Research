import numpy as np
from shrinkage import *
from MVO import *

from numpy import linalg as LA
import cvxpy as cp
import scipy


def testing(Assets):




    Assets=Assets.T



    i=0

    sharperolling=[]
    sharpeshrinkedrolling=[]

    returnsrolling=[]

    returnsshrinkedrolling=[]

    returnn=[]

    returnERC=[]

    T=23
    t=7

    j=0

    while(j<Assets.shape[1]):




        AssetsTrain=Assets[:,j:j+T]
        AssetsTest=Assets[:,j+T:j+T+t]

        if j>T:

            for i in range(0, AssetsTrain.shape[1]):
                returnsrolling.append(AssetsTrain[:,i].T@X[0])
                returnsshrinkedrolling.append(AssetsTrain[:,i].T@XShrinkage[0])
                returnn.append(AssetsTrain[:,i].T@Xoneovern[0])
                



        Sigma=np.cov(AssetsTrain)+10**-3*np.eye(AssetsTrain.shape[0],AssetsTrain.shape[0])









        Returns=np.sum(AssetsTrain,axis=1)/AssetsTrain.shape[1]

        shrink=covariance_shrinked(Sigma,0.1)



        X=portfolio(Sigma,0,Returns)




        XShrinkage=portfolio(shrink,0,Returns)


        Xoneovern=portfolio(np.zeros((AssetsTrain.shape[0],AssetsTrain.shape[0])),0,np.zeros((AssetsTrain.shape[0],1)))







        for i in range(0, AssetsTest.shape[1]):
            returnsrolling.append(AssetsTest[:,i].T@X[0])
            returnsshrinkedrolling.append(AssetsTest[:,i].T@XShrinkage[0])
            returnn.append(AssetsTest[:,i].T@Xoneovern[0])





        j=j+T+t





    returnsrolling=np.array(returnsrolling)
    returnsshrinkedrolling=np.array(returnsshrinkedrolling)
    returnn=np.array(returnn)





    returnsrolling=returnsrolling[np.logical_not(np.isnan(returnsrolling))]
    returnsshrinkedrolling=returnsshrinkedrolling[np.logical_not(np.isnan(returnsshrinkedrolling))]
    returnn=returnn[np.logical_not(np.isnan(returnn))]



    returnsrolling=returnsrolling[np.logical_not(np.isinf(returnsrolling))]
    returnsshrinkedrolling=returnsshrinkedrolling[np.logical_not(np.isinf(returnsshrinkedrolling))]
    returnn=returnn[np.logical_not(np.isinf(returnn))]



    I0=1
    portfolioVal=[]
    portfolioValShrinked=[]
    portfolioValn=[]




    for i in range(0,returnsrolling.shape[0]):
        I0=(1+returnsrolling[i])*I0
        portfolioVal.append(I0)

    I0=1


    for i in range(0,returnsshrinkedrolling.shape[0]):
        I0=(1+returnsshrinkedrolling[i])*I0
        portfolioValShrinked.append(I0)

    I0=1

    for i in range(0,returnn.shape[0]):
        I0=(1+returnn[i])*I0
        portfolioValn.append(I0)


    portfolioVal=np.array(portfolioVal)
    portfolioValShrinked=np.array(portfolioValShrinked)
    portfolioValn=np.array(portfolioValn)








    return [portfolioVal[portfolioVal.shape[0]-1], portfolioValShrinked[portfolioValShrinked.shape[0]-1], portfolioValn[portfolioValn.shape[0]-1]]
