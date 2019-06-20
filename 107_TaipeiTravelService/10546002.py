#-*- coding: utf-8 -*-
import matplotlib.pyplot  as plt
import numpy as np

# 預設可讀寫
from openpyxl import load_workbook 
from matplotlib.font_manager import FontProperties  

# 圖片大小(寬, 高)
plt.rcParams['figure.figsize'] = (10.0, 5.0)
# data_only 讀檔是否只讀值
wb = load_workbook('107年臺北市旅遊服務中心基礎統計表(OPENDATA).xlsx', data_only=True)
# 儲存格現在位置
ws = wb.active 
# 獲取excel文檔所有的數據,返回的是一個 generator 對象
data = ws.values

#--------------
def Area_ServiceTime():
    # 中文字型設定
    font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=7)
    
    # 取地區
    local = []
    row = list(ws.rows)[2]
    for cell in list(row)[1:13]:
        cell.value = cell.value.replace('\n', '')
        local.append(cell.value)
    print(local)
    # 取月份
    month = []
    column = list(ws.columns)[0]
    for cell in list(column)[4:16]:
        month.append(cell.value)

    # 取各地區服務數總計
    service_list = []
    # 1-12月資料
    for column in list(ws.columns)[1:13]:
        location = column[2].value.replace('\n', '')
        sum_service = 0

        for cell in list(column)[4:16]:
            sum_service += cell.value
        service_list.append(sum_service)
    print(service_list)
    # 取小數後兩位
    print("變異數：", "%.2f" % np.var(service_list, axis = 0)) # 變異數
    print("算術平均：", "%.2f" % np.mean(service_list, axis = 0)) # 算術平均
    print("標準差：", "%.2f" % np.std(service_list, axis = 0)) # 標準差
    print("筆數：", service_list.count (6272)) # 筆數
    print("中位數：", "%.2f" % np.median(service_list, axis = 0)) # 中位數
    print("最大值：", np.max(service_list, axis = 0)) # 最大值
    print("最小值：", np.min(service_list, axis = 0)) # 最小值
    y_pos = np.arange(len(service_list))
    
    # 平面橫條圖
    plt.barh(y_pos, service_list, align='center', alpha=0.4, label = "Total_ServerTime")
    plt.yticks(y_pos, local, rotation=15, fontproperties=font)
    plt.xlabel('Service Times')
    plt.ylabel('local')
    plt.title('ServerTimes of Every Area')
    # 圖例
    plt.legend()
    # 設定圖例位置
    plt.legend(loc='upper right', borderaxespad=0.5) # borderaxespad 坐標軸與圖例間的距離
    # 格線(
    plt.grid(axis="x")
    # 產生圖檔
    plt.savefig('Area_ServiceTime.png', dpi=300, format='png')
    # 預覽畫面
    plt.show()

#--------------
def Month_ServiceTime():
    # 中文字型設定
    font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=18)
    
    # 取月份
    month = []
    column = list(ws.columns)[0]
    for cell in list(column)[4:16]:
        month.append(cell.value)

    # 取各月服務數總計
    service_list = []
    for row in list(ws.rows)[4:16]:
        sum_service = 0
        for cell in list(row)[1:13]:
            sum_service += cell.value
        service_list.append(sum_service)

    # 分佈圖
    plt.scatter(month, service_list, 
                s = 100, # 大小
                c = 'green', # 顏色
                marker = '*', # 形狀
                alpha = 1, 
                label = "Month_ServiceTime" 
                )

    plt.xticks(month, fontproperties=font)
    plt.title('Server Times of Every Month')
    plt.xlabel('month')
    plt.ylabel('Service Times')
    # 圖例
    plt.legend()
    # 設定圖例位置
    plt.legend(loc='upper left', borderaxespad=0.5) # borderaxespad 坐標軸與圖例間的距離
    # 格線(
    plt.grid(axis="x")
    # 產生圖檔
    plt.savefig('Month_ServiceTime.png', dpi=300, format='png')
    # 預覽畫面
    plt.show()

#--------------
def local_compare():
    # 中文字型設定
    font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=14)

    # 取月份
    month = []
    column = list(ws.columns)[0]
    for cell in list(column)[4:16]:
        month.append(cell.value)

    TaipeiStation = []
    # 台北車站各月服務次數
    for column in list(ws.columns)[1:2]:
        for cell in list(column)[4:16]:
            TaipeiStation.append(cell.value)

    MeiTing=[]
    # 梅庭各月服務次數
    for column in list(ws.columns)[10:11]:
        for cell in list(column)[4:16]:
            MeiTing.append(cell.value)

    # 台北車站
    plt.plot(month,
            TaipeiStation,
            linestyle = '-',
            linewidth = 2,
            color = 'steelblue',
            marker = 'o', # 形狀
            markersize = 6, # 大小
            markeredgecolor='black', # 點邊框
            markerfacecolor='steelblue', # 點顏色
            label = 'TaipeiStation')

    # 梅庭
    plt.plot(month, MeiTing, 
            linestyle = '-', 
            linewidth = 2, 
            color = '#ff9999',
            marker = 'o', # 形狀
            markersize = 6, 
            markeredgecolor='black', # 點邊框
            markerfacecolor='#ff9999', # 點顏色
            label = 'MeiTing')

    plt.xticks(month, fontproperties=font)
    plt.ylim(15000, 80000)
    plt.title('台北車站和梅庭每月比較', fontproperties=font)
    plt.xlabel('month')
    plt.ylabel('Service Times')
    # 圖例
    plt.legend()
    # 設定圖例位置
    plt.legend(loc='upper left', borderaxespad=0.5) # borderaxespad 坐標軸與圖例間的距離
    # 格線(
    plt.grid(axis="x")
    # 產生圖檔
    plt.savefig('local_compare.png', dpi=300, format='png')
    # 預覽畫面
    plt.show()

if __name__ == "__main__":
    Area_ServiceTime()
    Month_ServiceTime()
    local_compare()
