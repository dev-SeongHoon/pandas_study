import pandas as pd

df=pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
"""
print("#데이터프레임 df의 내용을 일부 확인")
print(df.head(),'\n',df.tail())
"""
"""
print("#df의 모양과 크기 확인:(행의 개수, 열의 개수)를 투플로 반환")
print(df.shape)
print()
"""
"""
print("#데이터프레임 df의 내용확인")
print(df.info())
print()

print("#데이터프레임 df의 자료형 확인")
print(df.dtypes)
print()data_statistics

print("#시리즈(mog 열)의 자료형 확인")
print(df.mpg.dtypes)
print()
"""
"""
print("#데이터프레임 df의 기술통계 정보 확인")
print(df.describe(),'\n',df.describe(include='all'))
"""
