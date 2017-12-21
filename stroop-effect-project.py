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

#Let's perform some statistical analysis
#First we will use bootstrapping to create an array of sample means
diffs = []
conmeans = []
inconmeans = []
for _ in range(10000):
    congruent_mean = df['Congruent'].sample(df['Congruent'].shape[0], replace=True).mean()
    incongruent_mean = df['Incongruent'].sample(df['Incongruent'].shape[0], replace=True).mean()
    diff = (congruent_mean - incongruent_mean)
    conmeans.append(congruent_mean)
    inconmeans.append(incongruent_mean)
    diffs.append(diff)

diffs = np.asarray(diffs)
conmeans = np.asarray(conmeans)
inconmeans = np.asarray(inconmeans)

# Now let's plot the data to confirm it looks normal
obs_diff = df['Congruent'].mean() - df['Incongruent'].mean()
plt.hist(diffs)
plt.axvline(obs_diff, color='r')
plt.savefig('samplemeans.png')
plt.show()
plt.clf()

#Calculate a 95% confidence interval
confintv = ((np.percentile(diffs, 2.5)), (np.percentile(diffs, 97.5)))
print(confintv)