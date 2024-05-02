import numpy as np
import pandas as pd

path = 'rawdata/stations.csv'

df = pd.read_csv(path, index_col='번호')
df = df.astype({'구분': 'str',
                '대여소명': 'str',
                '구': 'str',
                '동': 'str',
                '위도': 'float32',
                '경도': 'float32'})

df.to_pickle('tashu_dataset-station_information.pkl')