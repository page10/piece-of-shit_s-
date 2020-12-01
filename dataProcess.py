print('please wait. importing files...')
import pandas as pd 
import numpy as np 

filePath = input('please input the data file position.an example: e:/python/True100transportPoint.csv:')
filePath = filePath.lstrip(' ').rstrip(' ').rstrip(':')
numPoints = input('please input the number of points in the file. an example:1104:') 
numPoints.lstrip(' ').rstrip(' ').rstrip(':')
numPoints = int(numPoints)
whole_data = pd.read_csv(filePath)
res = []  #存储每个点第一次出现小于37的数的位置的数组
for pointNum in range(1,numPoints + 1):  
    numStr = str(pointNum)  #第numStr个点
    tempPoint = whole_data.loc[:,numStr]
    i = 2 
    while i < len(tempPoint):
        if float(tempPoint[i]) <= 37:
            break 
        i += 1
    res.append(i)
#print(res)
with open("testWriteData.txt","w") as f:
        f.write(str(res))