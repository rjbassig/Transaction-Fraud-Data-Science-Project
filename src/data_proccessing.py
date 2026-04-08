#Libraries Set Up
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))


#Data Set Print
def load_data(path):
    return pd.read_csv(path)

df = load_data("../Credit Data/creditcard.csv")

#Data Set Info
df.head()
df.info()

df['Class'].value_counts()