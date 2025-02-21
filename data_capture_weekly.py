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



if __name__ == "__main__":
    today = datetime.today()
    four_days_ago = today - timedelta(days=4)
    end_dt = today.strftime("%Y-%m-%d")+' 15:00:00'
    start_dt = four_days_ago.strftime("%Y-%m-%d")+' 09:30:00'
    '''伊利'''    
    for i in range(5):
        data_dt = get_date(i)
        print(f"执行任务日期: {data_dt}")
        print("正在获取伊利交易数据")
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sh600887", date=data_dt)
        file_name = "/yili/trade_data/sh600887_trade"+data_dt+'.csv'
        stock_intraday_sina_df.to_csv(file_name, index=False)
        print("CSV 文件保存成功！")
        time.sleep(60)
        
    stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="600887", start_date=start_dt, end_date=end_dt, period="1", adjust="")        
    stock_zh_a_hist_min_em_df.to_csv("/yili/minute_data/sh600887_"+today.strftime("%Y-%m-%d")+".csv", index=False)
    
    '''茅台'''      
    for i in range(5):
        data_dt = get_date(i)
        print(f"执行任务日期: {data_dt}")
        print("正在获取茅台交易数据")
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sh600519", date=data_dt)
        file_name = "/maotai/trade_data/sh600519_trade"+data_dt+'.csv'
        stock_intraday_sina_df.to_csv(file_name, index=False)
        print("CSV 文件保存成功！")
        time.sleep(60)
    stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="600519", start_date=start_dt, end_date=end_dt, period="1", adjust="")        
    stock_zh_a_hist_min_em_df.to_csv("/maotai/minute_data/sh600519_"+today.strftime("%Y-%m-%d")+".csv", index=False)
              
        
    '''纳斯达克'''   
    fund_etf_hist_min_em_df = ak.fund_etf_hist_min_em(symbol="513300", period="1", adjust="", start_date=start_dt, end_date=end_dt)
    fund_etf_hist_min_em_df.to_csv("/nasidake/minute_data/nasidake_"+today.strftime("%Y-%m-%d")+".csv", index=False)
    '''黄金''' 
    fund_etf_hist_min_em_df = ak.fund_etf_hist_min_em(symbol="518880", period="1", adjust="", start_date=start_dt, end_date=end_dt)
    fund_etf_hist_min_em_df.to_csv("/gold/minute_data/gold_"+today.strftime("%Y-%m-%d")+".csv", index=False)
