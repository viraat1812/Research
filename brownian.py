from GBM import*
import numpy as np
covr=np.load("assets_.npy")

n=10

covr=covr[0:n,:]

drift_high=25
drift_low=20
volatility_high=50
volatility_low=49


mu=np.random.randint(drift_low,drift_high,size=(1,n))*np.ones([1,n])
sigma=np.random.randint(volatility_low,volatility_high, size=(1,n))*np.ones([1,n])


print(mu)
print(sigma)


Assets= gbm(mu,sigma,np.zeros([1,n]),np.ones([1,n]),np.corrcoef(covr),100*np.ones([1,n]),600,10**-5)
delta=[]


for i in range(1,Assets.shape[0]):

    delta.append((Assets[i,:]-Assets[i-1,:])/Assets[i-1,:])


delta=np.array(delta)
np.save("AssetsSim.npy",delta)


plt.xlabel("t")
plt.ylabel("Sim")

plt.plot(range(0,Assets.shape[0]),Assets[:,:])


#plt.plot(range(0,returns.shape[0]),returns*100,label='MVO')
#plt.plot(range(0,returnsshrinked.shape[0]),returnsshrinked*100,label='MVOW')
plt.show()
