# -*- coding: UTF-8 -*-
import pandas as pd;
import numpy as np;

"""""""""""""""""""""""""""""""""""""""
   计算每个股票每分钟已实现的日内回报
"""""""""""""""""""""""""""""""""""""""

def compare(x):
    return (x-x['2016-03-07 09:31:00'])/x['2016-03-07 09:31:00']*100

#第一列第二列作为时间戳，并把时间戳和股票作为联合索引
dataBase = pd.read_csv("../../resource/stk20160307.csv",parse_dates=[[1,2]],index_col=['date_time','stk_d_code']);
dataBase['price_delta']=dataBase['money']/dataBase['vol']
#计算每个股票每分钟已实现的日内回报
dataBase.groupby("stk_d_code")['price_delta'].apply(compare).to_csv("../../file/price_delta_percent.csv");
