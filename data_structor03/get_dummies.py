import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight', 'acceleration','model year','origin','name']

#디스플레이 설정 변경
pd.set_option('display.max_columns',len(df.columns))                         #출력할 최대 열의 개수
pd.set_option('display.max_colwidth',int(df['name'].apply(len).max()))       #출력할 열의 너비
pd.set_option('display.unicode.east_asian_width',True)                       #유니코드 사용 너비 조정
pd.set_option('display.width', 600)                                          #콘솔 출력 너비

print('df.head()', '\n', df.head(), '\n')