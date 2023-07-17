import numpy as np

import matplotlib.pylab as plt

import math


returns=np.load("gridsearch.npy")
returnsshrinked=np.load("gridsearchShrinked.npy")

PerformanceRatio=[]


for i in range(0, returns.shape[1]):
    Sample=0
    Shrink=0
    for j in range(0, returns.shape[0]):
        if returns[j,i]>=returnsshrinked[j,i]:
            Sample+=1
        else:
            Shrink+=1
    PerformanceRatio.append(Sample/Shrink)

vol=np.load("volatilityRange.npy")


plt.xlabel("volatility")
plt.ylabel("average performance")

plt.plot(vol,PerformanceRatio)
plt.plot(vol, np.ones(vol.shape[0]))

plt.show()
