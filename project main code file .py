#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


d = pd.read_csv("C:/Users/YAMINI PARIKH/Desktop/Python310/Dataset/17_DS_Dataset.csv")


# In[4]:


d.head()


# In[5]:


d.shape


# In[6]:


d.columns


# In[7]:


d.isnull()


# In[8]:


d.isnull().any()


# In[9]:


d.dtypes


# In[10]:


d.describe()


# #finding A,B abd C for SmartPhone

# In[11]:


d["Q1. Smartphone with decoy"]= d["Q1. Smartphone with decoy"].replace('A ', 'A')


# In[12]:


( d.iloc[:,4]=='A').sum()


# In[13]:


d["Q1. Smartphone with decoy"]= d["Q1. Smartphone with decoy"].replace('B ', 'B')


# In[14]:


( d.iloc[:,4]=='B').sum()


# In[15]:


d["Q1. Smartphone with decoy"]= d["Q1. Smartphone with decoy"].replace('C ', 'C')


# In[16]:


( d.iloc[:,4]=='C').sum()


# In[17]:


d.shape[0]


# #finding A,B abd C for Laptop 

# In[18]:


d.iloc[:,6].values


# In[19]:


(d.iloc[:,6]=='A').sum()


# In[20]:


(d.iloc[:,6]=='B').sum()


# In[21]:


(d.iloc[:,6]=='C').sum()


# #Finding A,B,C for dataplan

# In[22]:


d.iloc[:,8].values


# In[23]:


(d.iloc[:,8]=='A').sum()


# In[24]:


(d.iloc[:,8]=='B').sum()


# In[25]:


(d.iloc[:,8]=='C').sum()


# #Finding A,B,C for magazine

# In[26]:


d.iloc[:,10].values


# In[27]:


(d.iloc[:,10]=='A').sum()


# In[28]:


(d.iloc[:,10]=='B').sum()


# In[29]:


(d.iloc[:,10]=='C').sum()


# In[30]:


from tabulate import tabulate


# In[32]:


data = [
    ["A" , "41", "45", "35", "35"],
    ["B", "13", "30", "53", "47"],
    ["C" , "43", "22", "9", "15"]
]
head = ["Options" , "Smartphone" , "Television" , "Dataplan" , "Magazine"]
print(tabulate(data, headers=head, tablefmt="grid"))


# In[35]:


(d.iloc[:,2]=='15-25').sum()


# In[36]:


(d.iloc[:,2]=='25-35').sum()


# In[37]:


(d.iloc[:,2]=='35-45').sum()


# In[38]:


(d.iloc[:,2]=='45 & Above').sum()


# # Age 

# In[39]:


d["Age"].value_counts(normalize="False").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=90)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Age = ['15-25','25-35','35-45','45 & Above']

plt.legend(labels=Age,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[40]:


Age = ['15-25','25-35','35-45','45 & Above']
Value = [64,7,10,16]
bar_width = 0.35
color = ['orange','blue','green','red']
plt.bar(Age,Value,bar_width,color= color,edgecolor='black')
plt.xticks(Age)
plt.xlabel('Age', fontsize=16)
plt.ylabel('No. of People', fontsize=16)
plt.legend()
plt.show()


# In[41]:


ax = sns.barplot(Age,Value,hue=Age)
plt.show()


# # Gender

# In[42]:


d["Gender"].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Gender = ['Male','Female']

plt.legend(labels=Gender,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[43]:


by_gender = d.groupby('Gender')


# In[44]:


by_gender.size()


# In[45]:


my_colors = ['orange','blue']
by_gender.size().plot(kind='bar',color=my_colors)


# # Age & Gender

# In[46]:


by_cat_gen = d.groupby(['Age','Gender'])

by_cat_gen.get_group(('15-25', 'Female'))


# In[47]:


by_cat_gen.size().unstack().plot(kind='bar')


# In[48]:


by_cat_gen.size()


# In[49]:


cat_gen_sz = by_cat_gen.size().unstack()
cat_gen_sz['total'] = cat_gen_sz.sum(axis=1) 
cat_gen_sz = cat_gen_sz.sort_values(by='Female', ascending=True) 
cat_gen_sz[['Female', 'total', 'Male']].plot(kind='bar')


# # With and without decoy graph

# # For Smartphone

# #PIE CHART with Decoy

# In[50]:


d["Q1. Smartphone with decoy"].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=360)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B','C']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# #Pie Chart without decoy

# In[51]:


d["Q2. smart phone without decoy"]= d["Q2. smart phone without decoy"].replace('B ', 'B')


# In[52]:


d.iloc[:,5].values


# In[53]:


d["Q2. smart phone without decoy"].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=360)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# #BAR CHART WITH DECOY

# In[54]:


by_sm = d.groupby('Q1. Smartphone with decoy')
my_colors = ['orange','blue','green']
by_sm.size().plot(kind='bar',color=my_colors)


# In[55]:


by_sm.size()


# #BAR CHART WITHOUT DECOY

# In[56]:


by_sm_d = d.groupby('Q2. smart phone without decoy')
my_colors = ['orange','blue']
by_sm_d.size().plot(kind='bar',color=my_colors)


# In[54]:


by_sm_d.size()


# # FOR TV

# In[60]:


d['Q3. TV (decoy)'].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B','C']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[61]:


d['Q4. TV (without decoy)'].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[62]:


by_lap = d.groupby('Q3. TV (decoy)')
my_colors = ['orange','blue','green']
by_lap.size().plot(kind='bar',color=my_colors)


# In[63]:


by_lap.size()


# In[64]:


by_lap_d = d.groupby('Q4. TV (without decoy)')
color = ('orange','blue')
by_lap_d.size().plot(kind='bar',color=color)


# In[65]:


by_lap_d.size()


# # For Dataplan

# In[66]:


d['Q5. dataplan (with decoy)'].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B','C']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[67]:


d['Q6. dataplan (without decoy) '].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[68]:


by_data = d.groupby('Q5. dataplan (with decoy)')
my_colors = ['orange','blue','green']
by_data.size().plot(kind='bar',color=my_colors)


# In[69]:


by_data.size()


# In[70]:


by_data_d = d.groupby('Q6. dataplan (without decoy) ')
my_colors = ['orange','blue']
by_data_d.size().plot(kind='bar',color=my_colors)


# In[71]:


by_data_d.size()


# # For Magazine

# In[72]:


d['Q7. Magazine (with decoy)'].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B','C']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[73]:


d['Q8. Magazine (Without decoy)'].value_counts(normalize="True").plot(kind='pie',autopct="%.2f%%",figsize=(10,6),shadow=True,startangle=120)
plt.tight_layout()
plt.rcParams['font.size'] = 13
Options = ['A','B']

plt.legend(labels=Options,loc='upper center',bbox_to_anchor=(0.5, -0.04),ncol=2,fontsize=15) 


# In[74]:


by_mag = d.groupby('Q7. Magazine (with decoy)')
my_colors = ['orange','blue','green']
by_mag.size().plot(kind='bar',color=my_colors)


# In[75]:


by_mag.size()


# In[76]:


by_mag_d = d.groupby('Q8. Magazine (Without decoy)')
my_colors = ['orange','blue','green']
by_mag_d.size().plot(kind='bar',color=my_colors)


# In[77]:


by_mag_d.size()


# In[ ]:





# In[ ]:




