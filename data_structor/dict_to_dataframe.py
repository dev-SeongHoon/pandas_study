import pandas as pd

dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[10, 11, 12], 'c4':[13, 14, 15]}

df = pd.DataFrame(dict_data)

print(type(df), df, sep='\n')