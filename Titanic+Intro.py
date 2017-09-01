
# coding: utf-8

# In[9]:

import pandas as pd
import matplotlib.pyplot as plt
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


# In[2]:

titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count() # подсчёт выживших женьщин и мужчин


# In[3]:

titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count()       # выживщие по классам кабин (1-2-3 класс)


# In[4]:

titanic_df.groupby(['Age', 'Survived'])['PassengerID'].count()          # выживщие по возрастной группе


# In[10]:

titanic_df.groupby(['Age', 'Survived'])['PassengerID'].count().plot()  
plt.show()

