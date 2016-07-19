# coding: utf-8

# In[26]:

# check missing value function, needed in step 3
def missingcheck(obj):
    flag="No missing!"
    for bool in obj:
        if bool==True:
          flag="missing entry detected!"  
    print(flag)  

# check whether the date meets the requirments
def datecheck(startm,startd,ele,ds_monct):
    str="".join(ele)
    date=time.strptime(str,"%Y-%m-%d %H:%M:%S")
    if not (date[0]==startm and date[1]==startd):
        ds_monct.append(0)
    elif date[0]==startm and date[1]==startd:
        ds_monct.append(1)
    return ds_monct

# In[2]:

# step 2: modify dataframe
se=pd.Series(ds["uid"])
ds.index=se
ds=ds.drop("uid",axis=1)
print(ds)


# In[1]:

##step 1 : import original data
import pandas as pd
import json as js

path = r"C:\Users\Changlin Li\Desktop\user.json\user.json"
record=[js.loads(line) for line in open(path)]
ds=pd.DataFrame(record)
print(ds)


# In[34]:

# step 3: check null values, use fun in the beginning
counter=pd.isnull(ds)
missingcheck(counter["app"]) 
missingcheck(counter["appfile"])
missingcheck(counter["activity_time"])
missingcheck(counter["label"])
missingcheck(counter["category_id"])
   


# In[35]:

# step 4 check duplicate UID
ds1=pd.DataFrame(ds.index)
booleans=ds1.duplicated()
flag="No duplicated!"
for bool in booleans:
    if bool==True:
      flag="duplicate entry detected!"  
print(flag)


# In[3]:

# step 5 sort dataframe accroding to uid
ds=ds.sort_index(axis=0)
print(ds)


# In[17]:

# step 6 sort dataframe accroding to activity_time
ds=ds.sort_values(by="activity_time")
print(ds)


# In[6]:

# step 7, sub-step 1： get total entries, training sets , small sample test(300 units)
ds_sample=ds[:300]
ds_sample=ds_sample[ds_sample["label"]>0]
ds_sample=ds_sample.dropna() 
length=len(ds_sample)
# clear na value
ds_sample.sort_values(by="category_id")
count1=0
print(ds_sample["category_id"])
for ele in ds_sample["category_id"]:
    if ele==[]:
        count1+=1
print(count1)
appPerc=count1/length
print(appPerc)


# In[4]:

# sub-step2: compute the weight of non-empty category_id user in all VIP-purchase group
ds=ds[ds["label"]>0]
ds=ds.dropna()  
# clear na value
length=len(ds) 
ds=ds.sort_values(by="category_id")
count1=0
for ele in ds["category_id"]:
    if ele==[]:
        count1+=1
appPerc=count1/length
print(appPerc)
# conclusion: there is no possibility to remove empty category_id users.

#step 8: extract date, the analysis date starts from 2015/05
import time
import pandas as pd
ds_sample=ds[:300]
ds_monct=[]
startm=2015
startd=5

for ele in ds_sample["activity_time"]:
    if len(ele)==1:
        ds_monct=datecheck(startm,startd,ele,ds_monct)
    else:                                 
#        for multiple date , assuming the first one valid. 
        ds_monct=datecheck(startm,startd,ele[0],ds_monct)
                        
print(ds_monct)
#step 8, sub-step2: category_id of most frequency
ds_cate_id=ds_sample.sort_values(by="category_id")
ds_cateRe=[]
for ele in ds_cate_id["category_id"]:
    ds_cateRe.append(len(ele))
print(ds_cateRe)
print(len(ds_cateRe))

# get frequency from the data list
checklist=[]
for ele in ds_cate_id["category_id"]:
    checklist.extend(ele)
# change the type of char in "checklist" into int
for i in range(0,len(checklist)):
    checklist[i]=int (checklist[i])
a=max(checklist)
b=min(checklist)
print(a)                       
print(b)
# the range is (1,58) from the code above
def countcheck(checklist):
    loaddict={}
    for i in range(0,59):
        loaddict[i]=checklist.count(i)
    return loaddict
loaddict= countcheck(checklist)   
print (sorted(loaddict.items(), key=lambda d: d[1],reverse=True))

# update full customer category_id list
list1=[]
for ele in ds_cate_id["category_id"]:
    list1.append(list(set(ele)))
for ele in list1:
    print(ele)


