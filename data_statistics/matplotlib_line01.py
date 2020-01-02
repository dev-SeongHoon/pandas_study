import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0,header=0)

pd.set_option('display.max_columns',10)
pd.set_option('display.max_colwidth',20)
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',600)

print(df.head())

df=df.fillna(method='ffill')
print(df.head())

mask=(df['전출지별']=='서울특별시')&(df['전입지별']!='서울특별시')
df_seoul=df[mask]
df_seoul=df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True)
df_seoul.set_index('전입지',inplace=True)

print(df_seoul.head())

sr_one=df_seoul.loc['경기도']
print(sr_one.head())

plt.plot(sr_one.index,sr_one.values)
plt.xticks(rotation=45)
# plt.show()

plt.xticks(rotation=45)
plt.plot(sr_one)
# plt.show()

plt.plot(sr_one)

plt.title('서울 -> 경기 인구 이동')

plt.xlabel('기간')
plt.ylabel('이동 인구수')

# plt.show()

from matplotlib import font_manager, rc
font_path="gulim.ttf"
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)
# matplotlib.rcParams['font.family'] = 'malgun'
# matplotlib.rcParams['axes.unicode_minus'] = False

plt.legend(labels=['서울 -> 경기'],loc='best')

plt.show()
