from GBM import*
from backtesting import*
import numpy as np

def synthetic(drift, volatility):
    covr=np.load("assets_.npy")
    covr=covr[0:10,:]

    drift_high=drift
    drift_low=round(0.95*drift)-1

    volatility_high=volatility
    volatility_low=round(0.95*volatility)-1



    mu=np.random.randint(drift_low,drift_high,size=(1,10))*np.ones([1,10])
    sigma=np.random.randint(volatility_low,volatility_high, size=(1,10))*np.ones([1,10])


    Assets= gbm(mu,sigma,np.zeros([1,10]),np.ones([1,10]),np.corrcoef(covr),100*np.ones([1,10]),300,10**-5)
    delta=[]


    for i in range(1,Assets.shape[0]):

        delta.append((Assets[i,:]-Assets[i-1,:])/Assets[i-1,:])


    delta=np.array(delta)

    return testing(delta)
