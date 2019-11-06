# %matplotlib notebook

# Even harder

# Use the following data for this assignment:
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np
import scipy.stats as st

# Load data
np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

# Initiate value of y_input
y_input = 0


# Create statistics
df['mean'] = df.mean(axis=1)
df['std']  = df.std(axis=1, ddof=1) #standard deviation for sample
df['sem']  = (df['std'] * 1.96) / np.sqrt(3650) #std error mean sample times constant 1.96 for normal distribution and 95% CI.
df['prob'] = st.norm.cdf((y_input - df['mean'])/(df['sem']))

# Plot figure
plt.close()
plt.figure(dpi=150)
plt.axes(frameon=False)
bplot = plt.bar(df.index, df['mean'], yerr=df['sem'], color=cm.RdBu_r(df['prob']), capsize=5, edgecolor='black')


# Plot cleaning
plt.xticks(df.index, df.index.values.astype(str))
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sample Mean', fontsize=12)
plt.title('Normal distributions with 95% confidence intervals on mean.\n')

# Define function to run when event is triggered
def onclick(event):
    y_input = event.ydata.astype(np.int64)
    df['prob'] = st.norm.cdf((y_input - df['mean'])/(df['sem']))
    bplot = plt.bar(df.index, df['mean'], yerr=df['sem'], color=cm.RdBu_r(df['prob']), capsize=5, edgecolor='black')
    plt.gca().set_title('Normal distributions with 95% confidence intervals on mean.\nSelected y-value: {}'.format(y_input))
    plt.savefig('Week3.png')

# Tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plt.show()
