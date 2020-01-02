import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

#그래프그리기-선형회귀선 표시(fit_reg=True)
sns.regplot(x='age', y='fare', data=titanic, ax=ax1)

#그래프그리기-선형회귀선 미표시(fit_reg=False)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2, fit_reg=False)

plt.show()