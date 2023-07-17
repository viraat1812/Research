from GBM import*
import numpy as np
covr=np.load("assets_.npy")

rates=np.array([[0.001,.001,1,100]])


t=0
N=10
covr=covr[0:N,:]
T=2000
I0=100*np.ones([1,N])
AssetsMarkov=np.zeros([N,1])

time=[]

regimes=[0.25,0.5,0.75]



while t<T:



    if t<regimes[0]*T:
        Assets= gbm(40*np.random.rand(1,N)*np.ones([1,N]),5*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(0.25*T),10**-5)
        t=regimes[0]*T



    elif regimes[0]*T<=t and t<regimes[1]*T:
        Assets= gbm(40*np.random.rand(1,N)*np.ones([1,N]),30*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(0.25*T),10**-5)
        t=regimes[1]*T



    elif  regimes[1]*T<=t and t<regimes[2]*T:
        Assets= gbm(10*np.random.rand(1,N)*np.ones([1,N]),30*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(0.25*T),10**-5)
        t=regimes[2]*T



    else:
        Assets= gbm(10*np.random.rand(1,N)*np.ones([1,N]),5*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(0.25*T),10**-5)
        t=T




    Assets=Assets.T



    I0=Assets[:,Assets.shape[1]-1]




    AssetsMarkov=np.concatenate((AssetsMarkov,Assets), axis=1)


    time.append(t)

AssetsMarkov=AssetsMarkov[:,1:]

delta=[]

for i in range(1,AssetsMarkov.shape[1]):

    delta.append((AssetsMarkov[:,i]-AssetsMarkov[:,i-1])/AssetsMarkov[:,i-1])


delta=np.array(delta)
np.save("AssetsSim.npy",delta)



plt.xlabel("t")
plt.ylabel("Sim")

AssetsMarkov=AssetsMarkov.T

plt.plot(range(0,AssetsMarkov.shape[0]),AssetsMarkov[:,0:N])


#plt.plot(range(0,returns.shape[0]),returns*100,label='MVO')
#plt.plot(range(0,returnsshrinked.shape[0]),returnsshrinked*100,label='MVOW')
plt.show()
