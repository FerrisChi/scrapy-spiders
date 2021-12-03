import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.read_csv('BeijingPM20100101_20151231.csv', encoding='utf-8', dtype=str)
print(df.info())

for i in tqdm(range(len(df['No']))):
    sum = count = sumt = countt = 0
    if not (df['PM_Dongsihuan'][i] is np.nan):
        sum += int(df['PM_Dongsihuan'][i])
        count += 1
    if not (df['PM_US Post'][i] is np.nan):
        sum += int(df['PM_US Post'][i])
        count += 1
    if not (df['PM_Dongsi'][i] is np.nan):
        sum += int(df['PM_Dongsi'][i])
        count += 1

    try:
        df.loc[i, 'PM_AVG'] = round(sum / count, 2)
    except:
        pass

df['year'] = df['year'].astype('int')
df['month'] = df['month'].astype('int')
df['TEMP_AVG'] = df['TEMP'].astype('float')

newdf = df.groupby(by=['year', 'month']).agg({'PM_AVG': 'mean', 'TEMP_AVG': 'mean'}, sort=True)
newdf.to_csv('result.csv', float_format='%.4f', encoding = 'utf-8')
print(newdf)