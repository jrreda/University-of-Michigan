# # Assignment 3 - Building a Custom Visualization

# Use the following data for this assignment:
get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
#Get means for bar chart
meanValues = [(df.loc[1992]).mean(axis = 0), (df.loc[1993]).mean(axis = 0), (df.loc[1994]).mean(axis = 0), (df.loc[1995]).mean(axis = 0)]

#calculate 95% confidence intervals
z = 1.960
standardDeviations = [(df.loc[1992]).std(axis = 0), (df.loc[1993]).std(axis = 0), (df.loc[1994]).std(axis = 0), (df.loc[1995]).std(axis = 0)]
n = (len(df.loc[1992]))**(0.5)
confidenceIntervals = [(i /n)*z for i in standardDeviations]
#calculate value ranges for intervals
upperRange = [m + u for m, u in zip(meanValues, confidenceIntervals)]
lowerRange = [m - u for m, u in zip(meanValues, confidenceIntervals)]

#Set up colors
barColors = []

#Color based on y value selected
selectedY = 43000

valueRanges = list(zip(upperRange, lowerRange))
for i,j in valueRanges:
    if i < selectedY:
        barColors.append('steelblue')
    if j > selectedY:
        barColors.append('tomato')
    if i > selectedY > j:
        barColors.append('w')

#plot means with error bars
plt.figure()
xvals = df.index
plt.bar(xvals, meanValues, width = 0.3, color = barColors, yerr = confidenceIntervals, edgecolor = 'black', linewidth = 1)

#set x axis ticks
plt.xticks(np.arange(min(xvals), max(xvals)+1, 1.0))

#plot line at selected y value
plt.axhline(y=selectedY, color='g', linestyle='-')
plt.text(1995.35, selectedY, selectedY, fontdict=None, withdash=False)
plt.xlabel('Year')



