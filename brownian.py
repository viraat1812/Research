from GBM import*
import numpy as np



def generateSynthetic(drift_low, drift_high, volatility_low, volatility_high,n):

    covr=np.load("assets_.npy")


    covr=covr[0:n,:]


    mu=np.random.randint(drift_low,drift_high,size=(1,n))*np.ones([1,n])
    sigma=np.random.randint(volatility_low,volatility_high, size=(1,n))*np.ones([1,n])


    Assets= gbm(mu,sigma,np.zeros([1,n]),np.ones([1,n]),np.corrcoef(covr),100*np.ones([1,n]),300,10**-5)
    delta=[]


    for i in range(1,Assets.shape[0]):

        delta.append((Assets[i,:]-Assets[i-1,:])/Assets[i-1,:])


    delta=np.array(delta)
    np.save("AssetsSim.npy",delta)


    plt.xlabel("t")
    plt.ylabel("Sim")


    plt.plot(range(0,Assets.shape[0]),Assets[:,:])


    plt.show()
