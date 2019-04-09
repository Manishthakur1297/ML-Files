
# coding: utf-8

# In[4]:


import pandas as pd
import quandl


# In[6]:


df=quandl.get("WIKI/GOOGL")
df.head()


# In[10]:


df1=pd.read_csv(r"C:\Users\admin\Documents\AAPL.csv")
df1.head()


# In[13]:


type(df1.Date[0])


# In[14]:


df1.Date[1]-df1.Date[1]


# In[15]:


pd.to_datetime(df1.Date)


# In[18]:


df1.set_index("Date",inplace=True)


# In[24]:


dt=pd.to_datetime(df1.index)
dt


# In[25]:


type(dt[0])


# In[31]:


dt[1]


# In[32]:


dt[5]


# In[34]:


(dt[5]-dt[1]).days


# In[35]:


type(df1.index[0])


# In[36]:


df1.index=dt


# In[37]:


df1.head()


# In[38]:


type(df1.index[0])


# In[42]:


df1.head()


# In[48]:


type(df1.index[0])


# In[49]:


df1.info()


# In[53]:


t=pd.date_range('2018-05-14',periods=22,freq='B')


# In[54]:


df1.index=t
df1.head()


# In[56]:


type(df1.index[0])


# In[60]:


df1['2018-05-14':'2018-05-18']


# In[62]:


df1['2018-05-14':'2018-05-18'].Close.mean()


# In[67]:


get_ipython().run_line_magic('matplotlib', 'inline')
df1['2018-05-14':'2018-05-18'].Close.plot(kind='pie')


# In[74]:


p=pd.Period("2018")
p


# In[75]:


p+5


# In[76]:


p=pd.Period("2018",freq="D")
p


# In[77]:


p+6


# In[78]:


p=pd.Period("2018",freq="H")
p


# In[80]:


p+30


# In[81]:


p=pd.Period("2018",freq="Q")
p


# In[85]:


p+4


# In[86]:


# import requests
import urllib.request as ur


# In[87]:


conn=ur.urlopen("https://api.themoviedb.org/3/movie/now_playing?api_key=470727176eb42bd2a9aa9c3e07a16037&language=en-US&page=1")
data=conn.read().decode("utf-8")
data


# In[89]:


type(data)


# In[90]:


import json


# In[91]:


data=json.loads(data)
data


# In[93]:


d=data['results']


# In[95]:


df=pd.DataFrame(d)
df.head()


# In[97]:


df.id.values


# In[98]:


from sklearn.datasets import load_iris
from sklearn import cluster


# In[105]:


data=load_iris()
data=data['data']


# In[106]:


X=data[:,[1,0]]
X


# In[111]:


import matplotlib.pyplot as plt
plt.scatter(X[:,0],X[:,1])


# In[112]:


clf=cluster.KMeans(n_clusters=3)
c=clf.fit(X)


# In[116]:


p=clf.cluster_centers_


# In[117]:


import matplotlib.pyplot as plt
plt.scatter(X[:,0],X[:,1])
plt.scatter(p[:,0],p[:,1],c="red",s=150)

