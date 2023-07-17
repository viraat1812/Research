import numpy as np
from browniantest import*

simulations=[]

#change23

l=0

dmax=40
dmin=10

vmax=50
vmin=2
simulationReturn=np.zeros([dmax-dmin,vmax-vmin])
simulationReturnShrinked=np.zeros([dmax-dmin,vmax-vmin])

for i in range(dmin,dmax):


    for j in range(vmin,vmax):



        values=synthetic(i,j)


        simulationReturn[i-dmin,j-vmin]=values[0]
        simulationReturnShrinked[i-dmin,j-vmin]=values[1]

        print(l)

        l=l+1

np.save("gridsearch.npy",simulationReturn)
np.save("gridsearchShrinked.npy",simulationReturnShrinked)
np.save("driftRange.npy",range(dmin,dmax))
np.save("volatilityRange.npy", range(vmin,vmax))
