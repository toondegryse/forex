# Standard import
import numpy as np 
import pandas as pd 
from pandas import DataFrame
from numpy.random import randn
from cStringIO import StringIO
import datetime

# Stats
from scipy import stats 

# Plotting
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Directory access
from os import listdir
from os.path import isfile, join

# select all input files: daily currency exchange rate at the end of the day from eoddata.com
stockfiles = [f for f in listdir('/home/user/Documents/forex/input') if isfile(join('/home/user/Documents/forex/input', f))]
stockfiles = sorted(stockfiles)

# DataFrame for each currency and the date
eurdf = DataFrame(columns=['value','date'])
caddf = DataFrame(columns=['value','date'])
gbpdf = DataFrame(columns=['value','date'])

# Get the target currencies out of each file
for inf in stockfiles:
	# read each source file in a dataframe and add a column with average per currency
	forexdfFile = pd.DataFrame(pd.read_csv('/home/toon/Documents/python_analytics/input/'+inf,header=0,sep=',',parse_dates=True))
	forexdfFile['mean'] = (forexdfFile['High'] + forexdfFile['Low'])/2

	# find and append all target values
	forexdf = pd.DataFrame()
	df =forexdfFile.set_index('Symbol')
	eurdf = eurdf.append({'value': df.loc['USDEUR','mean'], 'date': int(inf.split('_')[1].split('.')[0][-2:])}, ignore_index=True)
	caddf = caddf.append({'value': df.loc['USDCAD','mean'], 'date': int(inf.split('_')[1].split('.')[0][-2:])}, ignore_index=True)
	gbpdf = gbpdf.append({'value': df.loc['USDGBP','mean'], 'date': int(inf.split('_')[1].split('.')[0][-2:])}, ignore_index=True)

# Plot the currencies
plot = sns.regplot(x="date", y="value", data=eurdf)
plot = sns.regplot(x="date", y="value", data=caddf)
plot = sns.regplot(x="date", y="value", data=gbpdf)
plot.set(xlabel='Day',ylabel='Currency', title='Currency Exchange Rates in June 2016')
plt.show()