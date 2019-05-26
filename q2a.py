#!/usr/bin/env python3


#imports
import pandas as pd
#import numpy as np


#read input file
df = pd.read_csv('/home/aa/CPSC4810/flightdelays.csv')

#filter by Origin = SFO
df=df.loc[df['Origin']=='SFO',:]

#output to file
df[['ArrDelay','Origin']].head(3).to_csv('SFOpy.csv')

#print(df[['ArrDelay','Origin']].head(3))

print(open('SFOpy.csv').read())
