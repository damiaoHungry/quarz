# -*- coding: UTF-8 -*-
import pandas as pd;

"""""""""""""""""""""""""""""""""""""""
         计算每个股票的5分钟均价
"""""""""""""""""""""""""""""""""""""""

#第一列第二列作为时间戳，并作为联合索引
ds = pd.read_csv("../../resource/stk20160307.csv",parse_dates=[[1,2]],index_col=['date_time']);
#五分钟重采样平均价
ds_mean = ds.groupby("stk_d_code").resample("5Min").mean()
#五分钟重采样求和
ds_sum = ds.groupby("stk_d_code").resample("5Min").sum()

ds_mean['price']=ds_sum['money']/ds_sum['vol']
ds_mean.to_csv("../../file/mean.csv");
