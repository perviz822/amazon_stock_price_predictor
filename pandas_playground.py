import pandas as pd
l = [1,2,3,4,5,6,7]
l2  = [1,23,45,56,23,2,2]
#usage of data_range
date_range = pd.date_range(start ='2022-12-01', end ='2022-12-07', freq='D')
df =  pd.DataFrame(data = {'Sales':l ,'Values':l2}, index=date_range)
print(df)