import numpy as np
from browniantest import*
from backtestingERC import*

def simrunsERC(dmax,dmin,vol,sims):

    simulations=[]


    l=0
    simulationReturnERC=np.zeros([dmax-dmin, sims])
    simulationReturnERCS=np.zeros([dmax-dmin, sims])




    for i in range(dmin,dmax):




        for j in range(0,sims):



            values=testingERC(synthetic(i,vol))



            simulationReturnERC[i-dmin,j]=values[0]
            simulationReturnERCS[i-dmin,j]=values[1]



            print(l)

            l=l+1

    np.save("simsReturnERC.npy",simulationReturnERC)
    np.save("simsReturnERCS.npy",simulationReturnERCS)

    np.save("driftRange.npy",range(dmin,dmax))

dmax=40
dmin=30

vol=50


sims=20

simrunsERC(dmax,dmin,vol,sims)
