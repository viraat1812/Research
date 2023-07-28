import numpy as np
from browniantest import*
from backtesting import*


def simruns(dmax,dmin,vol,sims):

    simulations=[]

    l=0

    simulationReturn=np.zeros([dmax-dmin,sims])
    simulationReturnShrinked=np.zeros([dmax-dmin, sims])
    simulationReturnn=np.zeros([dmax-dmin, sims])


    for i in range(dmin,dmax):




        for j in range(0,sims):



            values=testing(synthetic(i,vol))


            simulationReturn[i-dmin,j]=values[0]
            simulationReturnShrinked[i-dmin,j]=values[1]
            simulationReturnn[i-dmin,j]=values[2]


            print(l)

            l=l+1

    np.save("simsReturns.npy",simulationReturn)
    np.save("simsReturnsShrinked.npy",simulationReturnShrinked)
    np.save("simsReturnn.npy",simulationReturnn)


    np.save("driftRange.npy",range(dmin,dmax))



dmax=60
dmin=30

vol=40

sims=50

simruns(dmax,dmin,vol,sims)
