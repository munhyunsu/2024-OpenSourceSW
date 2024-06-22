import numpy as np
import pandas as pd

data_path = ['rawdata/2016.csv',
             'rawdata/2017.csv',
             'rawdata/2018.csv',
             'rawdata/2019.csv',
             'rawdata/2020.csv',
             'rawdata/2021.csv']

df = pd.DataFrame()
for path in data_path:
    tdf = pd.read_csv(path)
    df = pd.concat([df, tdf], ignore_index=True)
df = df.drop(df[df.isnull().any(axis=1)].index)
df = df.drop(df[(df['대여스테이션'] == 0) | (df['반납스테이션'] == 0)].index)

df = df.astype({'대여스테이션': 'int16', '대여일시': 'str',
                '반납스테이션': 'int16', '반납일시': 'str',
                '이동거리': 'float32', '회원구분': 'int8'})

df['대여일시'] = df['대여일시'].replace(r'\.\d+', '', regex=True)
df['반납일시'] = df['반납일시'].replace(r'\.\d+', '', regex=True)

df = df.sample(frac=0.05, random_state=20240621)
df = df.sort_index()
df = df.reset_index(drop=True)

print(len(df))
df.to_pickle('tashu_dataset-rental_history_sample.pkl')