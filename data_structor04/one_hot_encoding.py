import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv',header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower']=df['horsepower'].astype('float')

count, bin_dividers=np.histogram(df['horsepower'],bins=3)
bin_names=['저출력','보통출력','고출력']