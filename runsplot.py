import numpy as np
from browniantest import*



simret=np.load("simsReturns.npy")

simretshrink=np.load("simsReturnsShrinked.npy")
drift=np.load("driftRange.npy")


plt.xlabel("drift")
plt.ylabel("average portfolio value")
plt.plot(drift,np.sum(simret[:,:],axis=1)/simret.shape[1],label='MVO')
plt.plot(drift,np.sum(simretshrink[:,:],axis=1)/simretshrink.shape[1],label='MVOW')

plt.legend()
plt.show()
