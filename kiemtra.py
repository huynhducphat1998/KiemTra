# -*- coding: utf-8 -*-
"""kiemtra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PqGGN4-qcvXAhHUFphlx-SwXrUuOL3Zo
"""

#cau1
listA = [1, 10, 20, 5, 60, 30, 10, 9, 10]
listB = []
for x in listA:
  if x!=10:
    listB.append(x)
print(listB)

#câu 2
list1=["A","B","C","D","E","F"]
list2=[1,2,3,4,5,6]
dic={}
for x in range(len(list1)):
		dic[list1[x]] = list2[x]
# print(dic)

#câu 3
person={
			"Name":"Quoc Nam",
			"Age": 28,
			"Salary":8000,
			"City":"Tuy Hoa"
	}
KeyRemove=['Salary','City']
for x in KeyRemove:
		if x in person:
			person.pop(x)
print(person)

#cau4:a)
from google.colab import files
uploaded = files.upload()
print (uploaded['mobile_data.csv'][:200].decode('utf-8') + '...')
import pandas as pd
import io

df = pd.read_csv(io.StringIO(uploaded['mobile_data.csv'].decode('utf-8')))
df

from google.colab import files
uploaded = files.upload()
print (uploaded['mobile_data.csv'][:200].decode('utf-8') + '...')
import pandas as pd
import io

df = pd.read_csv(io.StringIO(uploaded['mobile_data.csv'].decode('utf-8')))
df
mobile_datas_df.head(5)

