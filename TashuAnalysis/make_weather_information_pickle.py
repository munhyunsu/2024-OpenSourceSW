import numpy as np
import pandas as pd

data_path = ['rawdata/weathers.csv']

df = pd.DataFrame()
for path in data_path:
    tdf = pd.read_csv(path)
    df = pd.concat([df, tdf], ignore_index=True)
df.fillna(0, inplace=True)

df = df.astype({'지점': 'int16', '지점명': 'str', '일시': 'str',
                '평균기온(°C)': 'float32', '일강수량(mm)': 'float32'})

df.to_pickle('weather.pkl')