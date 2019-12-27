import pandas as pd

dates = ['2019-01-01','2020-03-01','2021-06-01']

print("#문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환")
ts_dates=pd.to_datetime(dates)
print(ts_dates)
print('\n')

print("#Timestamp를 Period로 변환")
pr_day=ts_dates.to_period(freq='D')
print(pr_day)
pr_month=ts_dates.to_period(freq='M')
print(pr_month)
pr_year=ts_dates.to_period(freq='A')
print(pr_year)
