import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],
             '영어':[98,89,95],
             '음악':[85,95,100],
             '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
df = df.set_index('이름') #이름을 인덱스로 잡아주는 거에요
print(df)
print()

print("#새로운 행(row)을 추가 - 같은 원소 값을 입력")
df.loc[3] = 0
print(df)
print()

print("#새로운 행(row)을 추가 - 원소값이 여러개인 배열 입력")
df.loc['동규'] = [90,80,70,60]  #이름을 인덱스로 잡아주면 추가할 이름이 df.loc()안으로 들어가야 합니다.
print(df)
print()

print("#새로운 행(row)을 추가 - 기존 행을 복사")
df.loc['행5'] = df.iloc[4]   #인덱스를 이름으로 잡아준후 기존 행 복사하려면 loc(로케이션)을 iloc(아이로케이션)으로 바꿔줘야 합니다.
print(df)