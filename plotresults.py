import numpy as np

import matplotlib.pylab as plt

import math

volatilityindex=45

returns=np.load("gridsearch.npy")
print(returns.shape)
returnsshrinked=np.load("gridsearchShrinked.npy")
volatility=np.load("volatilityRange.npy")


"""
rows=round(volatilityindex/2)
cols=2

fig, axes = plt.subplots(rows,cols, figsize=(28,12))

l=0
plt.xlabel("drift")
plt.ylabel("Value")
for i in range(rows):




    for j in range(cols):

        if l==returns.shape[1]:
            l=0
            continue





        axes[i][j].plot(range(0,returns.shape[0]),returns[:,l])
        axes[i][j].plot(range(0,returnsshrinked.shape[0]),returnsshrinked[:,l])
        plt.xlabel("drift")
        plt.ylabel("Portfolio Value")




        l+=1

plt.show()


"""
plt.xlabel("Drift")
plt.ylabel("End Portfolio Value")
plt.title("volatility"+"="+str(volatility[volatilityindex]))

plt.plot(np.load("driftRange.npy"),returns[:,volatilityindex], label="MVO")
plt.plot(np.load("driftRange.npy"),returnsshrinked[:,volatilityindex], label="MVOW")


plt.legend()

plt.show()

#"""
