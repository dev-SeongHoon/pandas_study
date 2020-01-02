import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df=pd.read_csv('./auto-mpg.csv',header=None)

df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

df.plot(x='weight',y='mpg',kind='scatter', title='무게(weight)와 연비(mpg)의 관계')
plt.show()

df[['mpg','cylinders']].plot(kind='box',title='연비의 분포 및 실린더개수 분포')
plt.show()