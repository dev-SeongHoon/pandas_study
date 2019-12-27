import pandas as pd        

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})

print(student1)
print()
print(student2)
print()

print(" # 두 학생의 과목별 점수로 사칙연산 수행")
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))

print(" # 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)")
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
result2 = pd.DataFrame([addition, subtraction, multiplication, division])
print(result)
print()
result = result.transpose()
print(result)