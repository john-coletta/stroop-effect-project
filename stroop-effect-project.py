#First set up the imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#Read in data
df = pd.read_csv('stroopdata.csv')

#Build some visualizations here
plt.scatter(range(1, df.shape[0] + 1), df['Congruent'])
plt.axhline(df['Congruent'].mean(), color='r')
plt.xlabel('Task Number')
plt.ylabel('Time (s)')
plt.title('Time to Complete Congruent Test')
plt.savefig('congruentplot.png')
plt.show()
plt.clf()

#Now the incongruent data
plt.scatter(range(1, df.shape[0] + 1), df['Incongruent'])
plt.axhline(df['Incongruent'].mean(), color='r')
plt.xlabel('Task Number')
plt.ylabel('Time (s)')
plt.title('Time to Complete Incongruent Test')
plt.savefig('incongruentplot.png')
plt.show()
plt.clf()