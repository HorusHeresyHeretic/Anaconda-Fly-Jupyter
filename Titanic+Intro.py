
# coding: utf-8

# In[4]:

import pandas as pd
titanic_df = pd.read_csv("C:/Users/Battlestation/Documents/Visual Studio 2015/Projects/PythonApplication1/PythonApplication1/titanic.csv")
print(titanic_df.head())


# In[5]:

titanic_df


# In[6]:

titanic_df.info()


# In[9]:

titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count()


# In[10]:

titanic_df["Sex"]


# In[11]:

titanic_df["Survived"]


# In[12]:

titanic_df["PassengerID"]


# In[13]:

titanic_df.groupby(["Survived"])["PassengerID"].count()        # простой подсчёт выжавщих, 0 - погибли, 1 - спаслись


# In[14]:

pvt = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
pvt


# In[ ]:



