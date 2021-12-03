import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.read_csv('BeijingPM20100101_20151231.csv', encoding='utf-8', dtype=str)

for i in tqdm(range(len(df['No']))):
    sum = count = 0
    if not (df['PM_Dongsihuan'][i] is np.nan):
        sum += int(df['PM_Dongsihuan'][i])
        count += 1
    if not (df['PM_US Post'][i] is np.nan):
        sum += int(df['PM_US Post'][i])
        count += 1
    if not (df['PM_Dongsi'][i] is np.nan):
        sum += int(df['PM_Dongsi'][i])
        count += 1
        
    if not (df['PM_Nongzhanguan'][i] is np.nan):
        sum += int(df['PM_Nongzhanguan'][i])
        count += 1

    if count != 0:
        df.loc[i, 'avg'] = round(sum / count, 2)
    else:
        df.loc[i, 'avg'] = None

df = df.groupby("year").mean()
print(df)
