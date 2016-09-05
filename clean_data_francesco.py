#f=open('C:\\Users\\okoFM\\Downloads\\INVENTOR_12.TXT')
#f=open('Y:\\okofm\\INVENTOR_12.TXT')
f=open('C:\\Users\\okoFM\\INVENTOR_12.TXT')

myList = []
for line in f:
    myList.append(line)

#print(myList[4])


num_lines = sum(1 for line in open('C:\\Users\\okoFM\\INVENTOR_12.TXT'))
num_lines

list=[]
final_list=[]
for i in range(num_lines+1):
    list.append(myList[i][0:7])
    list.append(myList[i][7:11])
    list.append(myList[i][12:32])
    list.append(myList[i][33:48])
    list.append(myList[i][49:68])
    list.append(myList[i][69:99])
    list.append(myList[i][100:120])
    list.append(myList[i][121:124])
    list.append(myList[i][125:130])
    final_list.append(list)
    list=[]
              
#print(final_list)
#final_list

import pandas as pd
df = pd.DataFrame(final_list, columns=['var1', 'var2','var3', 'var4','var5', 'var6','var7', 'var8','var9'])

#df

df.to_csv('C:\\Users\\okoFM\\data.csv')