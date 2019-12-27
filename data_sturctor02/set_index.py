import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],
             '영어':[98,89,95],
             '음악':[85,95,100],
             '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

print("#특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정")
ndf = df.set_index(['이름'])
print(ndf)
print()
ndf2 = ndf.set_index('음악')
print(ndf2)
print()
ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)

#콘솔에서 아래와 같이 입력하면 결과가 영어 89, 체육 90 이 출력됩니다.
ndf3.loc[(80,95)]
#콘솔에서 아래와 같이 입력하면 결과는 90이 출력됩니다.
ndf3.loc[(80,95), '체육']
