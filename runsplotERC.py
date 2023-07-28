import numpy as np
import matplotlib.pyplot as plt





simretERC=np.load("simsReturnERC.npy")
simretERCS=np.load("simsReturnERCS.npy")

drift=np.load("driftRange.npy")



plt.xlabel("drift")
plt.ylabel("average portfolio value")
plt.plot(drift,np.sum(simretERC[:,:],axis=1)/simretERC.shape[1],label='ERC')
plt.plot(drift,np.sum(simretERCS[:,:],axis=1)/simretERCS.shape[1],label='ERCS')



plt.legend()
plt.show()
