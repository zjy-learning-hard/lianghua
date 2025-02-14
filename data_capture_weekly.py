# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:05:29 2025

@author: 17317
"""

import time
import akshare as ak
from datetime import datetime, timedelta

def get_date(days_diff=0):
    """获取与当前日期相差指定天数的日期
    :param days_diff: 天数差（正数为未来，负数为过去）
    :return: 格式为yyyymmdd的日期字符串
    """
    target_date = datetime.now() - timedelta(days=abs(days_diff))
    return target_date.strftime("%Y%m%d")


def get_3second_data_weekly():
    for i in range(5):
        data_dt = get_date(i)
        print(f"执行任务日期: {data_dt}")
        print("正在获取数据")
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sh600751", date=data_dt)
        file_name = 'sh600751_'+data_dt+'.csv'
        stock_intraday_sina_df.to_csv(file_name, index=False)
        print("CSV 文件保存成功！")
        time.sleep(60)
        




