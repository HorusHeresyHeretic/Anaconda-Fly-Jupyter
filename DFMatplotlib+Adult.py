
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
from pandas import date_range,Series,DataFrame,read_csv, qcut
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
from numpy.random import randn
from pylab import *
from matplotlib import rcParams

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'white'
rcParams['font.family'] = 'StixGeneral'

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()


# In[2]:

data = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
print(data.info())  


# In[4]:

# график плотности распределения
pData = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
pData['age'].plot(kind='kde', linewidth=3);  plt.title('Age');
show()
pData['fnlwgt'].plot(kind='kde', linewidth=3);  plt.title('Something');
show()
pData['education-num'].plot(kind='kde', linewidth=2);  plt.title('Education');
show()
pData['capital-gain'].plot(kind='kde', linewidth=1);  plt.title('$gain');
show()
pData['capital-loss'].plot(kind='kde', linewidth=3);  plt.title('$loss');
show()
pData['hours-per-week'].plot(kind='kde', linewidth=3);  plt.title('Work-hours');
show()


# In[18]:

# гистограммы
plt.figure();
pData['age'].diff().hist(); plt.title('Age');
show()
pData['fnlwgt'].diff().hist(); plt.title('fnlwgt');
show()
pData['education-num'].diff().hist(); plt.title('education-num');
show()
pData['capital-gain'].diff().hist(); plt.title('capital-gain');
show()
pData['capital-loss'].diff().hist(); plt.title('capital-loss');
show()
pData['hours-per-week'].diff().hist(); plt.title('hours-per-week');
show()


# In[22]:

pData.plot(x='age', y='capital-gain', style='o', markersize=3);
show()


# In[23]:

pData.plot(x='age', y='capital-loss', style='o', markersize=3);
show()


# In[ ]:




# In[ ]:



