
# coding: utf-8

# In[1]:

import pandas as pd
# чтоб картинки рисовались в тетрадке
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 8)


# In[2]:

import numpy as pr
data = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
data.head()                                    # возвращает первые 5 строк из файла - просто проверяем.


# In[4]:

print(data.shape)                              # возвращает (32561, 15) - 32561 строка в 15 столбцах


# In[5]:

print(data.columns)                            # возвращает название столбцов


# In[6]:

print(data.info())                             # общая информация по дата фрейму


# In[7]:

data.describe()                                  # общая стата по основным числовым характеристикам 


# In[8]:

""" проведём сортировку датафрейма по числовм признакам, используем метод сортировки по убиванию ascending=False """ 
data.sort_values(by="age",                       # сортировка по признаку Age
        ascending=False).head()   


# In[9]:

data.sort_values(by="fnlwgt",                    # сортировка по признаку fnlwgt
        ascending=False).head() 


# In[10]:

data.sort_values(by="education-num",             # сортировка по признаку education-num 
        ascending=False).head() 


# In[11]:

data.sort_values(by="capital-gain",              # сортировка по признаку capital-gain 
        ascending=False).head() 


# In[12]:

data.sort_values(by="capital-loss",              # сортировка по признаку capital-loss 
        ascending=False).head()


# In[13]:

data.sort_values(by="hours-per-week",            # сортировка по признаку hours-per-week 
        ascending=False).head() 


# In[14]:

data.describe(include=['object', 'bool'])         # возвращает статистику по нечисловым признакам


# In[15]:

""" проведём сортировку датафрейма по нечисловм признакам, используем метод сортировки по убиванию ascending=False """
data.sort_values(by="workclass",                       # сортировка по признаку workclass
        ascending=False).head() 


# In[16]:

data.sort_values(by="education",                       # сортировка по признаку education
        ascending=False).head() 


# In[17]:

data.sort_values(by="marital-status",                  # сортировка по признаку marital-status
        ascending=False).head() 


# In[27]:

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


# In[19]:

data.sort_values(by="occupation",                      # сортировка по признаку occupation
        ascending=False).head()


# In[20]:

data.sort_values(by="relationship",                    # сортировка по признаку relationship
        ascending=False).head() 


# In[21]:

data.sort_values(by="race",                            # сортировка по признаку race
        ascending=False).head()


# In[22]:

data.sort_values(by="sex",                             # сортировка по признаку sex
        ascending=False).head() 


# In[23]:

data.sort_values(by="native-country",                  # сортировка по признаку native-country
        ascending=False).head()  


# In[24]:

data.sort_values(by="salary",                          # сортировка по признаку salary
        ascending=False).head()  


# In[25]:

""" посмотрим на распределение данных в отношении объектов датафрейма"""
data['sex'].value_counts()                             # вывод чисел по признаку Sex 


# In[26]:

data['workclass'].value_counts()                       # вывод чисел по признаку workclass 


# In[27]:

data['education'].value_counts()                       # вывод чисел по признаку education 


# In[28]:

data['marital-status'].value_counts()                  # вывод чисел по признаку marital-status 


# In[29]:

data['occupation'].value_counts()                      # вывод чисел по признаку occupation


# In[30]:

data['relationship'].value_counts()                    # вывод чисел по признаку relationship


# In[31]:

data['race'].value_counts()                            # вывод чисел по признаку race


# In[32]:

data['native-country'].value_counts()                  # вывод чисел по признаку native-country


# In[33]:

data['salary'].value_counts()                          # вывод чисел по признаку salary


# In[34]:

""" посмотрим на распределение данных по числовым объектам """
data['age'].value_counts()                             # вывод чисел по признаку age


# In[35]:

data['fnlwgt'].value_counts()                          # вывод чисел по признаку fnlwgt


# In[36]:

data['education-num'].value_counts()                   # вывод чисел по признаку education-num 


# In[37]:

data['capital-gain'].value_counts()                    # вывод чисел по признаку capital-gain 


# In[38]:

data['capital-loss'].value_counts()                    # вывод чисел по признаку capital-loss 


# In[39]:

data['hours-per-week'].value_counts()                  # вывод чисел по признаку hours-per-week 


# In[40]:

""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['sex', 'workclass'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, False]).head()


# In[41]:

data.sort_values(by=['sex', 'workclass'],                # сортировка по группе столбцов в отношении Male
        ascending=[False, False]).head()


# In[42]:

data.sort_values(by=['sex', 'workclass'],                # сортировка по группе столбцов в отношении Male
        ascending=[False, False])


# In[43]:

""" процедура извлечения данных (индексации) из отдельных столбцов, рабоатет только с численными типами объектов """
data['age'].mean()                                       # средний возвраст 38.58164675532078


# In[44]:

data['fnlwgt'].mean()                                    # 189778.36651208502 


# In[45]:

data['education-num'].mean()                             # 10.0806793403151


# In[46]:

data['capital-gain'].mean()                              # 1077.6488437087312


# In[47]:

data['capital-loss'].mean()                              # 87.303829734959


# In[48]:

data['hours-per-week'].mean()                            # 40.437455852092995


# In[49]:

""" процедура извлечения логической индексации из отдельных столбцов, рабоатет только с НЕчисленными типами объектов """
data['workclass'] = data['workclass'].astype('bool') 
data['workclass'] = data['workclass'].astype('int64')   
data[data['workclass'] == 1].mean()  


# In[50]:

data['education'] = data['education'].astype('bool') 
data['education'] = data['education'].astype('int64')   
data[data['education'] == 1].mean() 


# In[51]:

data['marital-status'] = data['marital-status'].astype('bool') 
data['marital-status'] = data['marital-status'].astype('int64')   
data[data['marital-status'] == 1].mean()  


# In[52]:

data['occupation'] = data['occupation'].astype('bool') 
data['occupation'] = data['occupation'].astype('int64')   
data[data['occupation'] == 1].mean() 


# In[53]:

data['relationship'] = data['relationship'].astype('bool') 
data['relationship'] = data['relationship'].astype('int64')   
data[data['relationship'] == 1].mean() 


# In[54]:

data['race'] = data['race'].astype('bool') 
data['race'] = data['race'].astype('int64') 
data[data['race'] == 1].mean()


# In[55]:

data['sex'] = data['sex'].astype('bool') 
data['sex'] = data['sex'].astype('int64') 
data[data['sex'] == 1].mean()


# In[56]:

data['native-country'] = data['native-country'].astype('bool') 
data['native-country'] = data['native-country'].astype('int64')   
data[data['native-country'] == 1].mean()


# In[57]:

data['salary'] = data['salary'].astype('bool') 
data['salary'] = data['salary'].astype('int64')   
data[data['salary'] == 1].mean()


# In[60]:

"""data[data['workclass'] == 0].mean() и другие строки с == 00 возвращают - NaN (None) типа нету такого объекта """ 
data.apply(pr.max)                             # ищет и возвращает аккаунт с максимальными значения по всему датафрейму


# In[61]:

data.apply(pr.min)                             # ищет и возвращает аккаунт с минимальными значения по всему датафрейму


# In[62]:

data.loc[0:5, 'sex':'salary']                  # возвращает значение 6 строк в столбцах от sex до salary


# In[63]:

data.loc[0:5, 'age':'race']                    # возвращает значение 6 строк в столбцах от age до race


# In[64]:

data[100:101]                                  # возвращает 100 строку датафрейма


# In[65]:

"""посмотрим максимальные значения датафрейма по числовым признакам, с нечисловыми типами естественно не работает"""
data['age'].max()                              # возвращает 90


# In[66]:

data['fnlwgt'].max()                           # 1484705


# In[67]:

data['education-num'].max()                    # 16


# In[68]:

data['capital-gain'].max()                     # 99999


# In[69]:

data['capital-loss'].max()                     # 4356


# In[70]:

data['hours-per-week'].max()                   # 99


# In[71]:

"""data['salary'].max()/min() - возвращет 1 поскольку это объект, а не int64 == даже если преобразовать .astype"""
data['race'] = data['race'].astype('bool') 
print(data.info())


# In[74]:

data.head()                  # тут можно посмотерть как успешно я запарол датафрейм проводя процедуру логической индексации


# In[75]:

data = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
data.head()                 # загружу как я его снова                  


# In[76]:

print(data.info())                             # общая информация по дата фрейму


# In[78]:

data.sort_values(by=['sex', 'age'],                # сортировка по группе столбцов в отношении FeMale
        ascending=[True, False])


# In[81]:

columns_to_show = ['age', 'sex']
data.groupby(['sex'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])  


# In[82]:

data['native-country'].value_counts()  


# In[84]:

data['sex'].value_counts()  


# In[86]:

plt.figure();
data['age'].diff().hist();


# In[89]:

plt.figure();
data['education-num'].diff().hist();


# In[90]:

plt.figure();
data['education-num'].diff().hist(bins=50);


# In[92]:

data['education'] = data['education'].astype('bool') 
data['education'] = data['education'].astype('int64')  
plt.figure();
data['education'].diff().hist();                   # фигня какая то - похоже что строить графики можно тока из чисел


# In[5]:

columns_to_show = ['age', 'capital-gain', 'capital-loss'] 
data.groupby(['native-country'])[columns_to_show].describe(percentiles=[])


# In[6]:

columns_to_show = ['age', 'capital-gain', 'capital-loss'] 
data.groupby(['sex'])[columns_to_show].describe(percentiles=[])


# In[8]:

columns_to_show = ['native-country'] 
data.groupby(['sex'])[columns_to_show].describe(percentiles=[])


# In[9]:

columns_to_show = ['native-country'] 
data.groupby(['sex'])[columns_to_show].describe()


# In[10]:

columns_to_show = ['sex'] 
data.groupby(['native-country'])[columns_to_show].describe()


# In[17]:

columns_to_show = ['age'] 
data.groupby(['native-country'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])


# In[18]:

columns_to_show = ['age'] 
data.groupby(['native-country'])[columns_to_show].count()


# In[19]:

columns_to_show = ['age'] 
data.groupby(['native-country', "sex"])[columns_to_show].count()


# In[20]:

pd.crosstab(data['sex'], data['native-country'])


# In[21]:

pd.crosstab(data['sex'], data['native-country'], normalize=True)


# In[23]:

pd.crosstab(data['age'], data['native-country'], normalize=True)


# In[31]:

data.pivot_table(['age'], ['capital-loss'], aggfunc='mean').head(10)


# In[32]:

data.pivot_table(['capital-loss'], ['age'], aggfunc='mean').head(10)


# In[35]:

data.pivot_table(['capital-loss'], ['age'], aggfunc='mean')


# In[36]:

data.pivot_table(['capital-loss', "capital-gain"], ['age'], aggfunc='mean')


# In[38]:

data.pivot_table(['capital-loss', "capital-gain"], ['age', "sex"], aggfunc='mean')


# In[39]:

data.pivot_table(['capital-loss', "capital-gain", "native-country"], ['age', "sex"], aggfunc='mean')


# In[42]:

data.pivot_table(['capital-loss', "capital-gain"], ['age', "sex","workclass"], aggfunc='mean') 


# In[44]:

data.pivot_table(['capital-loss', "capital-gain"], ['age', "sex","workclass", "native-country"], aggfunc='mean') 


# In[45]:

pd.crosstab(data['age'], data['capital-loss'], margins=True)


# In[48]:

pd.crosstab(data["native-country"], data['capital-loss'], margins=True) # больше одного признака в скбоки не влазит - ну никак


# In[49]:

pd.crosstab(data["education-num"], data['capital-gain'], margins=True)


# In[50]:

pd.crosstab(data["education"], data['capital-gain'], margins=True)


# In[52]:

data['Above50K'] = (data['capital-gain'] > 50000).astype('int')


# In[53]:

pd.crosstab(data['Above50K'], data['education'], margins=True) #неправда - есть 2 человека с образованием в 10 классов и доходом больше 50К


# In[63]:

plt.figure();
data['education-num'].diff().hist();


# In[58]:

data['education-num'].describe()


# In[60]:

data['education-num']


# In[61]:

data['education']


# In[64]:

data['Above50K'] = (data['capital-gain'] > 50000).astype('int')
pd.crosstab(data['Above50K'], data['age'], margins=True)


# In[66]:

columns_to_show = ['Above50K']
data.groupby(['age'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])


# In[69]:

data['low50K'] = (data['capital-gain'] < 50000).astype('int')
columns_to_show = ['low50K']
data.groupby(['age'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])


# In[70]:

data.age.var()


# In[71]:

data.age.std()


# In[3]:

data["salary"]


# In[17]:

data["salary"],True


# In[18]:

data["salary"],False


# In[19]:

data["salary"].describe() 


# In[24]:

data.sort_values(by="salary"),True


# In[25]:

data.sort_values(by="salary"),False


# In[32]:

""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['age', 'salary'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, False])


# In[33]:

""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['age', 'salary'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, True])


# In[34]:

""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['salary', 'age'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, True])


# In[35]:

""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['salary', 'age'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, False])


# In[ ]:



