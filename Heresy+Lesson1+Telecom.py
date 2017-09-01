
# coding: utf-8

# In[4]:

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import warnings
warnings.simplefilter('ignore')
import pandas as pd
import numpy as pr
df = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/telecom_churn.csv")
"""
df.head()                                    # возвращает первые 5 строк из файла
"""
"""
pd.set_option('display.max_columns', 100)    # изменяет максимальное число выводимых столбцов
pd.set_option('display.max_rows', 100)       # изменяет максимальное число выводимых строк
"""
print(df.shape)                              # возвращает (3333, 20) - (строки, столбцы)


# In[5]:

print(df.columns)                            # возвращает название столбцов


# In[6]:

print(df.info())                             # общая информация по дата фрейму


# In[7]:

df['Churn'] = df['Churn'].astype('int64')
df.describe()                                # общая стата по основным числовым характеристикам


# In[8]:

df.describe(include=['object', 'bool'])      # возвращает статистику по нечисловым признакам


# In[9]:

df['Churn'].value_counts()                   # распределение данных по переменной Churn


# In[10]:

df.sort_values(by='Total day charge',        # сортировка по признаку Total day charge
        ascending=False).head()              # ascending=False для сортировки по убыванию 


# In[11]:

df.sort_values(by='Total day minutes',       # сортировка по признаку Total day minutes
        ascending=False).head() 


# In[12]:

df.sort_values(by=['Churn', 'Total day charge'],  # сортировка по группе столбцов
        ascending=[True, False]).head()


# In[13]:

df['Churn'].mean()      # возвращает долю нелояльных клиентов в датафрейме


# In[14]:

df[df['Churn'] == 1].mean()                  # возвращает средние значения числовых признаков в Churn(1)


# In[15]:

df[df['Churn'] == 0].mean()                  # возвращает средние значения числовых признаков в Churn(0)


# In[16]:

df[df['Churn'] == 1]['Total day minutes'].mean()  # возвращает среднее время разговора в среде Churn(1)


# In[17]:

df[df['Churn'] == 0]['Total day minutes'].mean()  # возвращает среднее время разговора в среде Churn(0)


# In[18]:

df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max()


# In[19]:

df[(df['Churn'] == 1) & (df['International plan'] == 'No')]['Total intl minutes'].max()


# In[20]:

df.loc[0:5, 'State':'Area code']             # возвращает значение 6 строк в столбцах от Стате до Ареа 


# In[21]:

df.iloc[0:5, 0:3]                            # возвращает значение первых пяти строк в первых 3 столбцах


# In[22]:

df[-1:]                                      # последняя строка дата фрейма


# In[23]:

df.apply(pr.max)                             # ищет и возвращает аккаунт с максимальными значения по всему датафрейму 


# In[24]:

df.apply(pr.min)                             # ищет и возвращает аккаунт с минимальныни значенияи по всему даатфрейму


# In[25]:

d = {'No' : False, 'Yes' : True}             # на что меняем значения в колонке 
df['International plan'] = df['International plan'].map(d)      # в какой колонке меняем значения (типа .format)
df.head()                                    # возвращает всю информацию по фрейму с заменой значений в International plan


# In[26]:

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']      #  см коммент на 422
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])


# In[27]:

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes'] 
df.groupby(['Churn'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])


# In[28]:

pd.crosstab(df['Churn'], df['International plan'])  


# In[29]:

pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True)


# In[30]:

df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['Area code'], aggfunc='mean').head(10)


# In[31]:

df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['International plan'], aggfunc='min').head()


# In[34]:

pd.crosstab(df['Churn'], df['International plan'], margins=True)    


# In[35]:

pd.crosstab(df['Churn'], df['Customer service calls'], margins=True)


# In[37]:

df['Many_service_calls'] = (df['Customer service calls'] > 3).astype('int') 
pd.crosstab(df['Many_service_calls'], df['Churn'], margins=True) 


# In[38]:

pd.crosstab(df['Many_service_calls'] & df['International plan'] , df['Churn'])


# In[ ]:



