import numpy as np
from browniantest import*

simulations=[]

sims=40

l=0

dmax=50
dmin=10

vol=40

simulationReturn=np.zeros([dmax-dmin,sims])
simulationReturnShrinked=np.zeros([dmax-dmin, sims])

for i in range(dmin,dmax):


    for j in range(0,sims):



        values=synthetic(i,vol)


        simulationReturn[i-dmin,j]=values[0]
        simulationReturnShrinked[i-dmin,j]=values[1]

        print(l)

        l=l+1

np.save("simsReturns.npy",simulationReturn)
np.save("simsReturnsShrinked.npy",simulationReturnShrinked)
np.save("driftRange.npy",range(dmin,dmax))
