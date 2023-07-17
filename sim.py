import numpy as np
import matplotlib.pyplot as plt

returns=np.load("returns.npy")
returnsshrinked=np.load("returnsshrinked.npy")
returnsOptimal=np.load("Optimal.npy")



returns=returns[np.logical_not(np.isnan(returns))]
returnsshrinked=returnsshrinked[np.logical_not(np.isnan(returnsshrinked))]
returnsOptimal=returnsOptimal[np.logical_not(np.isnan(returnsOptimal))]


returns=returns[np.logical_not(np.isinf(returns))]
returnsshrinked=returnsshrinked[np.logical_not(np.isinf(returnsshrinked))]
returnsOptimal=returnsOptimal[np.logical_not(np.isinf(returnsOptimal))]

sharpe=np.load("Sharpe.npy")
sharpeshrinked=np.load("SharpeShrinked.npy")




I0=1
portfolioVal=[]
portfolioValShrinked=[]
portfolioValOptimal=[]

for i in range(0,returns.shape[0]):
    I0=(1+returns[i])*I0
    portfolioVal.append(I0)

I0=1

for i in range(0,returnsshrinked.shape[0]):
    I0=(1+returnsshrinked[i])*I0
    portfolioValShrinked.append(I0)

I0=1

for i in range(0,returnsOptimal.shape[0]):
    I0=(1+returnsOptimal[i])*I0
    portfolioValOptimal.append(I0)


portfolioVal=np.array(portfolioVal)
portfolioValShrinked=np.array(portfolioValShrinked)
portfolioValOptimal=np.array(portfolioValOptimal)










plt.xlabel("t")
plt.ylabel("Portfolio Value")

plt.plot(range(0,portfolioVal.shape[0]),portfolioVal,label='MVO')
plt.plot(range(0,portfolioValShrinked.shape[0]),portfolioValShrinked,label='MVOW')
#plt.plot(range(0,portfolioVal.shape[0]),2*portfolioVal,label='2*MVO')
#plt.plot(range(0,portfolioValOptimal.shape[0]),portfolioValOptimal,label='Optimal MVO')

#plt.plot(range(0,returns.shape[0]),returns*100,label='MVO')
#plt.plot(range(0,returnsshrinked.shape[0]),returnsshrinked*100,label='MVOW')
plt.legend()
plt.show()





print(np.sum(returns*10**2)/returns.shape[0])
print(np.sum(returnsshrinked*10**2)/returnsshrinked.shape[0])
print(np.sum(returnsOptimal*10**2)/returnsOptimal.shape[0])

print(portfolioVal.shape)
print(portfolioValOptimal.shape)
print(portfolioVal[portfolioVal.shape[0]-1])
print(portfolioValShrinked[portfolioValShrinked.shape[0]-1])
