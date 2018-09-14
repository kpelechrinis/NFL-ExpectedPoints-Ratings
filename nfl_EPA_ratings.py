from matplotlib import pyplot as plt
from scipy.stats import norm
import sys
import os
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import optimize
from numpy import linalg as LA
import nflgame

# The first argument is a file that has every play of the type you are interested to obtain ratings for (e.g., test-data.csv has the passing plays from the 2017 season) 
# There needs to be a column called "Offense" that has the team on offense
# There needs to be a column called "Defense" that has the team on defense
# There needs to be a column called "value" that has the expected points added from the perspective of the offense

df = pd.read_csv(sys.argv[1])



teams = df.Offense.unique()


teams = list(np.sort(teams))

num_oplays = np.zeros(32)
num_dplays = np.zeros(32)

for i in range(len(teams)):
	num_oplays[i] = len([j for j,x in enumerate(df.Offense) if x==teams[i]])
	num_dplays[i] = len([j for j,x in enumerate(df.Defense) if x==teams[i]])

df['oidx'] = df.Offense.apply(lambda x: teams.index(x))
df['didx'] = df.Defense.apply(lambda x: teams.index(x))

avg = np.mean(df.value)

n_teams = len(teams)

def ortg_constr(x):
    return (x[0:32]*num_oplays).sum()/num_oplays.sum()

def drtg_constr(x):
    return (x[32:65]*num_dplays).sum()/num_dplays.sum()


def obj(x):
    pred = avg + df.oidx.apply(lambda i: x[i]) + df.didx.apply(lambda i: x[i+32])
    err = ((df.value-pred)**2).sum()
    return err

x0 = np.zeros(shape=len(teams)*2)

res = optimize.minimize(obj,x0,constraints=[{'type':'eq', 'fun':ortg_constr},{'type':'eq', 'fun':drtg_constr}], method="SLSQP",
                        options={'maxiter':10000,'disp':False})


print "Team , ORating , DRating"
for i,t in enumerate(teams):
	print str(t),",",res.x[i],",",res.x[i+32]
