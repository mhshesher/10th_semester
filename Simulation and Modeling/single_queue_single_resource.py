# -*- coding: utf-8 -*-
"""Single Queue Single Resource.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16x1LBx1dLwgO2oX2K-XqnrDAZ2rX88l2
"""

import pandas as pd
import numpy as np

#read 'time between arrival distribution' table
s=input('Enter the file name of "Time Between Arrival Distribution" table: ')
df0=pd.read_csv(s)
df0.columns=['tba','pb','rd']

#create list to map random digits for time between arrival
lst=[]
lst.append((np.nan,np.nan))
for i in range(len(df0)):
    tmp0=df0.iloc[i]['rd'].split('-')
    if i==len(df0)-1:
        tmp0[1]='1'+tmp0[1]
    val=float(df0.iloc[i]['tba'])
    for j in range(int(tmp0[0]),int(tmp0[1])+1):
        if j==1:
            continue;
        lst.append((j,val))
dt0=dict(lst)

#read 'service time distribution' table
s=input('Enter the file name of "Service Time Distribution" table: ')
df1=pd.read_csv(s)
df1.columns=['st','pb','rd']

#create list to map random digits for service time
lst=[]
for i in range(len(df1)):
    tmp0=df1.iloc[i]['rd'].split('-')
    if i==len(df1)-1:
        tmp0[1]='1'+tmp0[1]
    val=float(df1.iloc[i]['st'])
    for j in range(int(tmp0[0]),int(tmp0[1])+1):
        lst.append((j,val))
dt1=dict(lst)

#read random digits for time between arrival
s=input('Enter the file name of "Random Digits for Inter Arrival Time": ')
f=open(s,'r+')
s=f.read()
tmp0=s.split(',')
randt=[]
randt.append(np.nan)
for i in tmp0:
    randt.append(float(i))
    
#read random digits for service time
s=input('Enter the file name of "Random Digits for Service Time": ')
f=open(s,'r+')
s=f.read()
tmp0=s.split(',')
rands=[]
for i in tmp0:
    rands.append(float(i))

#algorithm
df2=pd.DataFrame()
lst=[i for i in range(1,len(randt)+1)]
df2['CN.']=lst
df2['RDA']=randt
df2['TSLA']=randt
for i in range(1,len(df2)):
    tmp=df2.iloc[i]['TSLA']
    df2['TSLA']=df2['TSLA'].replace({tmp:dt0[tmp]})
lst=[df2.iloc[:i+1]['TSLA'].sum() for i in range(len(df2))]
df2['AT']=lst
df2['RDS']=rands
df2['ST']=rands
lst=[]
for i in range(0,len(df2)):
    tmp=df2.iloc[i]['ST']
    lst.append(dt1[tmp])
df2['ST']=lst
tsb=[]
que=[]
tse=[]
ss=[]
si=[]
busy=0
for i in range(len(df2)):
    at=df2.iloc[i]['AT']
    st=df2.iloc[i]['ST']
    if at>=busy:
        tsb.append(at)
        que.append(0)
        tse.append(at+st)
        ss.append(st)
        si.append(at-busy)
        busy=at+st
    else:
        tsb.append(busy)
        que.append(busy-at)
        tse.append(busy+st)
        ss.append(st+(busy-at))
        si.append(0)
        busy=busy+st

df2['TSB']=tsb
df2['TCWQ']=que
df2['TSE']=tse
df2['TCSS']=ss
df2['ITS']=si

print('Single Queue Single Resource Simulation Table')
print(df2)