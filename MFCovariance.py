import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/Viraat/Downloads/all_mf_returns.csv")

df=df.iloc[:,1:]
assets=df.to_numpy()

assets=assets.T
np.save('assets_.npy',assets)
