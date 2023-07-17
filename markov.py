from GBM import*
import numpy as np
covr=np.load("assets_.npy")

rates=np.array([[1,10,0.001,0.1]])


t=0
N=10
covr=covr[0:N,:]
T=1000
I0=100*np.ones([1,N])
AssetsMarkov=np.zeros([N,1])

time=[]

while t<T:
    seed=np.random.rand()


    if seed<=0.25:
        dt= 1+np.random.exponential(scale=1/rates[0,0])
        Assets= gbm(40*np.random.rand(1,N)*np.ones([1,N]),40*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(dt),10**-5)

    if 0.25<=seed and seed<=0.50:
        dt= 1+np.random.exponential(scale=1/rates[0,1])
        Assets= gbm(40*np.random.rand(1,N)*np.ones([1,N]),5*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(dt),10**-5)

    if  0.50<=seed and seed<=0.75:
        dt= 1+np.random.exponential(scale=1/rates[0,2])
        Assets= gbm(10*np.random.rand(1,N)*np.ones([1,N]),40*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(dt),10**-5)

    if  0.75<=seed:
        dt= 1+np.random.exponential(scale=1/rates[0,3])
        Assets= gbm(10*np.random.rand(1,N)*np.ones([1,N]),5*np.random.rand(1,N)*np.ones([1,N]),np.zeros([1,N]),np.ones([1,N]),np.corrcoef(covr),I0,round(dt),10**-5)

    Assets=Assets.T


    I0=Assets[:,Assets.shape[1]-1]




    AssetsMarkov=np.concatenate((AssetsMarkov,Assets), axis=1)

    t=t+dt

    time.append(t)

AssetsMarkov=AssetsMarkov[:,1:]

delta=[]

for i in range(1,AssetsMarkov.shape[1]):

    delta.append((AssetsMarkov[:,i]-AssetsMarkov[:,i-1])/AssetsMarkov[:,i-1])


delta=np.array(delta)
np.save("AssetsSim.npy",delta)

print(delta.shape)

plt.xlabel("t")
plt.ylabel("Sim")

AssetsMarkov=AssetsMarkov.T

plt.plot(range(0,AssetsMarkov.shape[0]),AssetsMarkov[:,0:N])


#plt.plot(range(0,returns.shape[0]),returns*100,label='MVO')
#plt.plot(range(0,returnsshrinked.shape[0]),returnsshrinked*100,label='MVOW')
plt.show()
