#!/usr/bin/env python3

#imports

import pandas as pd
import numpy as np

#read relevant columns from file
df = pd.read_csv('/home/aa/CPSC4810/flightdelays.csv',usecols=['Dest','FlightNum'])

#group records according to destination airport
dest_counts=df['Dest'].value_counts()

#display top 3 destination airports
print(dest_counts.head(3))
