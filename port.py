import numpy as np
from shrinkage import *
from MVO import *
from ERC import*
from numpy import linalg as LA
import cvxpy as cp
import scipy


def rollingportfolio(Assets):

    SigmaTrue=np.cov(Assets)+10**-5*np.eye(Assets.shape[0],Assets.shape[0])

    Returns=np.sum(Assets,axis=1)/Assets.shape[1]
    XOpt=portfolio(SigmaTrue,0,Returns)


    j=0

    


    returnsrolling=[]

    returnsshrinkedrolling=[]

    returnn=[]

    returnERC=[]

    returnERCS=[]




    T=30
    t=20

    while(j<Assets.shape[1]):




        AssetsTrain=Assets[:,j:j+T]
        AssetsTest=Assets[:,j+T:j+T+t]

        if j>T:

            for i in range(0, AssetsTrain.shape[1]):
                returnsrolling.append(AssetsTrain[:,i].T@X[0])
                returnsshrinkedrolling.append(AssetsTrain[:,i].T@XShrinkage[0])
                returnn.append(AssetsTrain[:,i].T@Xoneovern[0])
                returnERC.append(AssetsTrain[:,i].T@XERC)
                returnERCS.append(AssetsTrain[:,i].T@XERCS)






        Sigma=np.cov(AssetsTrain)+10**-5*np.eye(AssetsTrain.shape[0],AssetsTrain.shape[0])










        Returns=np.sum(AssetsTrain,axis=1)/AssetsTrain.shape[1]







        X=portfolio(Sigma,0,Returns)




        Xoneovern=portfolio(np.zeros((AssetsTrain.shape[0],AssetsTrain.shape[0])),0,np.zeros((AssetsTrain.shape[0],1)))



        shrink=covariance_shrinked(Sigma,0.1)


        XShrinkage=portfolio(shrink,0,Returns)


        XERC=riskParity(Sigma,Returns)

        XERCS=riskParity(shrink,Returns)





        #print(Xoneovern[0])
        #print(X[0])
        #print(XShrinkage[0])
        #print(XERC)
        #print(XERCS)








        for i in range(0, AssetsTest.shape[1]):
            returnsrolling.append(AssetsTest[:,i].T@X[0])
            returnsshrinkedrolling.append(AssetsTest[:,i].T@XShrinkage[0])
            returnn.append(AssetsTest[:,i].T@Xoneovern[0])
            returnERC.append(AssetsTrain[:,i].T@XERC)
            returnERCS.append(AssetsTrain[:,i].T@XERCS)






        j=j+T+t

        print(j)






    np.save("returns.npy",returnsrolling)

    np.save("returnsshrinked.npy",returnsshrinkedrolling )
    np.save("1Overn.npy",returnn)
    np.save("returnERC.npy", returnERC)
    np.save("returnERCS.npy", returnERCS)
