import numpy as np
import matplotlib.pyplot as plt
from port import*
from brownian import*




def simulateMVO(dataset,drift_low, drift_high, volatility_low, volatility_high,n):




    if dataset=='ask2':
        Assets=np.load('assets_.npy')
        Assets=Assets[:,1000:2000]

    else:
        generateSynthetic(drift_low, drift_high, volatility_low, volatility_high,n)
        Assets=np.load('AssetsSim.npy')
        Assets=Assets.T


    rollingportfolio(Assets)


    returns=np.load("returns.npy")
    returnsshrinked=np.load("returnsshrinked.npy")
    
    returnn=np.load("1Overn.npy")
    returnERC=np.load("returnERC.npy")
    returnERCS=np.load("returnERCS.npy")




    returns=returns[np.logical_not(np.isnan(returns))]
    returnsshrinked=returnsshrinked[np.logical_not(np.isnan(returnsshrinked))]
   
    returnn=returnn[np.logical_not(np.isnan(returnn))]
    returnERC=returnERC[np.logical_not(np.isnan(returnERC))]
    returnERCS=returnERCS[np.logical_not(np.isnan(returnERCS))]



    returns=returns[np.logical_not(np.isinf(returns))]
    returnsshrinked=returnsshrinked[np.logical_not(np.isinf(returnsshrinked))]
    
    returnn=returnn[np.logical_not(np.isinf(returnn))]
    returnERC=returnERC[np.logical_not(np.isinf(returnERC))]
    returnERCS=returnERCS[np.logical_not(np.isinf(returnERCS))]







    I0=1
    portfolioVal=[]
    portfolioValShrinked=[]
  
    portfolioValn=[]
    portfolioValERC=[]
    portfolioValERCS=[]


    for i in range(0,returns.shape[0]):
        I0=(1+returns[i])*I0
        portfolioVal.append(I0)

    I0=1

    for i in range(0,returnsshrinked.shape[0]):
        I0=(1+returnsshrinked[i])*I0
        portfolioValShrinked.append(I0)



    I0=1

    for i in range(0,returnn.shape[0]):
        I0=(1+returnn[i])*I0
        portfolioValn.append(I0)

    I0=1

    for i in range(0,returnERC.shape[0]):
        I0=(1+returnERC[i])*I0
        portfolioValERC.append(I0)

    I0=1

    for i in range(0,returnERCS.shape[0]):
        I0=(1+returnERCS[i])*I0
        portfolioValERCS.append(I0)



    portfolioVal=np.array(portfolioVal)
    portfolioValShrinked=np.array(portfolioValShrinked)
    
    portfolioValn=np.array(portfolioValn)
    portfolioValERC=np.array(portfolioValERC)
    portfolioValERCS=np.array(portfolioValERCS)











    plt.xlabel("t")
    plt.ylabel("Portfolio Value")

    plt.plot(range(0,portfolioVal.shape[0]),portfolioVal,label='MVO')
    plt.plot(range(0,portfolioValShrinked.shape[0]),portfolioValShrinked,label='MVOW')
    plt.plot(range(0,portfolioValERC.shape[0]),portfolioValERC,label='ERC')
    plt.plot(range(0,portfolioValERCS.shape[0]),portfolioValERCS,label='ERCS')


    

    plt.legend()
    plt.show()







    print(portfolioVal[portfolioVal.shape[0]-1])
    print(portfolioValShrinked[portfolioValShrinked.shape[0]-1])
    print(portfolioValn[portfolioValn.shape[0]-1])
    print(portfolioValERC[portfolioValERC.shape[0]-1])
    print(portfolioValERCS[portfolioValERCS.shape[0]-1])


    print(np.sum(portfolioValERCS-portfolioValERC)/portfolioVal.shape[0])



drift_high=35
drift_low=30
volatility_high=45
volatility_low=40




simulateMVO('sim',drift_low, drift_high, volatility_low, volatility_high,20)
