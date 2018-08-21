# 7/18/18 Cóbhan Phillipson 
# Liver Disorder GMIT Project

# Import Python libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Use panda to read Bupa Liver Disorders Data Set
df = pd.read_csv('data/bupa-data.csv', names = ['mcv mean corpuscular volume', 'alkphos alkaline phosphotase', 'sgpt alamine aminotransferase', 'sgot aspartate aminotransferase', 'gammagt gamma-glutamyl transpeptidase', 'Daily Alcohol Drinks', 'Selector'])

# Calculate Highest Value in Every Column
print (df['mcv mean corpuscular volume'].max())
print (df['alkphos alkaline phosphotase'].max())
print (df['sgpt alamine aminotransferase'].max())
print (df['sgot aspartate aminotransferase'].max())
print (df['gammagt gamma-glutamyl transpeptidase'].max())
print (df['Daily Alcohol Drinks'].max())

# Calculate Mean Value of Every Column
print (df['mcv mean corpuscular volume'].mean())
print (df['alkphos alkaline phosphotase'].mean())
print (df['sgpt alamine aminotransferase'].mean())
print (df['sgot aspartate aminotransferase'].mean())
print (df['gammagt gamma-glutamyl transpeptidase'].mean())
print (df['Daily Alcohol Drinks'].mean())

# Calculate Minimum Value of Each Column
print (df['mcv mean corpuscular volume'].min())
print (df['alkphos alkaline phosphotase'].min())
print (df['sgpt alamine aminotransferase'].min())
print (df['sgot aspartate aminotransferase'].min())
print (df['gammagt gamma-glutamyl transpeptidase'].min())
print (df['Daily Alcohol Drinks'].min())

#Create a Histogram showing mean corpuscular volume
df.hist('mcv mean corpuscular volume')
plt.title('Histogram of mean corpuscular volume') 
plt.xlabel('results') 
plt.ylabel('mean corpuscular volume')   
plt.show() 

# Create a Histogram for all data columns
df.hist()
plt.savefig('liver_disorder_histogram.png') 
plt.show()

# Create a line chart
df.hist(x='mcv mean corpuscular volume', y='Daily Alcohol Drinks')
plt.show()