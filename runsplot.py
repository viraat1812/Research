import numpy as np
from browniantest import*



simret=np.load("simsReturns.npy")

simretshrink=np.load("simsReturnsShrinked.npy")

simretn=np.load("simsReturnn.npy")

simretERC=np.load("simsReturnERC.npy")

drift=np.load("driftRange.npy")


print(simret.shape)
plt.xlabel("drift")
plt.ylabel("average portfolio value")
plt.plot(drift,np.sum(simret[:,:],axis=1)/simret.shape[1],label='MVO')
plt.plot(drift,np.sum(simretshrink[:,:],axis=1)/simretshrink.shape[1],label='MVOW')
#plt.plot(drift,np.sum(simretn[:,:],axis=1)/simretn.shape[1],label='1/n')



#plt.plot(drift,simret)
#plt.plot(drift,simretshrink)



plt.legend()
plt.show()
