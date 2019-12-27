import pandas as pd

print("#Period배열 만들기 - 1개월 길이(간격)")
pr_m=pd.period_range(start='2019-01-01',
                     end=None,
                     periods=3,            #생성할 개수
                     freq='M')             #기간의 단위(M:월)
print(pr_m,'\n')

print("#Period배열 만들기 - 1시간 길이(간격)")
pr_h=pd.period_range(start='2019-01-01',
                     end=None,
                     periods=3,            #생성할 개수
                     freq='H')             #기간의 단위(H:시간)
print(pr_h,'\n')

print("#Period배열 만들기 - 2시간 길이(간격)")
pr_2h=pd.period_range(start='2019-01-01',  #생성할 날짜범위의 시작
                     end=None,             #날짜범위의 끝
                     periods=3,            #생성할 개수
                     freq='2H')            #기간의 단위(M:월)
print(pr_2h,'\n')

