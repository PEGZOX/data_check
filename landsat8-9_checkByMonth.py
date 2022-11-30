import os
import pandas as pd
import numpy as np

#该程序用于检查landsat8-9数据中是否有要求的月份
#如果没有month_need中月份的数据，则以 '142036_06'形式输出，其中142036是行列号，06是月份
#作为输入的表格landsat_excel中包含的是已下载的landsat数据ID
#输入数据需要按照行列号-月份的优先级排序

landsat_excel = r'C:\Users\17510\Desktop\landsat_find\Landsat_XJ.xlsx'
landsat_missing = r'C:\Users\17510\Desktop\landsat_find\Landsat_missing.xlsx'

month_need = ['06','07','08','09','10']  #可根据需求修改需求月份
landsat_missing_list = []

landsat_list = pd.read_excel(landsat_excel)
tmp = np.array(landsat_list).tolist()

count = 0
for landsat_tmp in tmp:
    #根据landsat数据ID提取行列号和月份，如果数据不同需要对应修改
    landsat = landsat_tmp[0]
    landsat_pathrow = landsat.split('_')[2]
    landsat_month = landsat.split('_')[3][4:6]
    
    if(count==0):
        landsat_pathrow_tmp = landsat_pathrow
        if(landsat_month in month_need):
                month_need.remove(landsat_month)
    else:
        if(landsat_pathrow==landsat_pathrow_tmp):
            #说明还是这个pathrow
            if(landsat_month in month_need):
                month_need.remove(landsat_month)
        else:
            #说明是新的pathrow
            if(len(month_need)):
                for month_missing in month_need:
                    landsat_missing_list.append(landsat_pathrow_tmp+'_'+month_missing)
            landsat_pathrow_tmp = landsat_pathrow
            month_need = ['06','07','08','09','10']
            if(landsat_month in month_need):
                month_need.remove(landsat_month)
    
    count+=1

print(landsat_missing_list)


