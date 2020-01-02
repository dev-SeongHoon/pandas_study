import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

df=pd.read_excel('./남북한발전전력량.xlsx')

df_ns=df.iloc[[0,5],3:]
df_ns.index=['South','North']
df_ns.columns=df_ns.columns.map(int)
print(df_ns.head())
print()

tdf_ns=df_ns.T

"""
df_ns.plot(title="drawing Line graph")

print(tdf_ns.head())

tdf_ns.plot(title='rows, columns transper drawing')

plt.show()
"""
tdf_ns.plot(kind='bar', title="한글")

plt.show()

tdf_ns.plot(kind='hist',title='Power generation')

plt.show()