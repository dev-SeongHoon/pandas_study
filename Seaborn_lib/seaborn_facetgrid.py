import matplotlib.pyplot as plt
import seaborn as sns

titanic=sns.load_dataset('titanic')
sns.set_style('whitegrid')
"""
g=sns.FacetGrid(data=titanic,col='who',row='survived')

g=g.map(plt.hist,'age')
"""
titanic_pair=titanic[['age','pclass','fare']]

g=sns.pairplot(titanic_pair)
plt.show()