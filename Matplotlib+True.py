
# coding: utf-8

# In[16]:

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


# In[17]:

x = linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()


# In[18]:

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.set_xlabel(r'$\alpha$', fontsize=38)
ax.set_ylabel(r'$y$', fontsize=38)
ax.set_title('title')
ax.legend(loc=2); # upper left corner
show()


# In[19]:

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig.tight_layout()
show()


# In[20]:

#Метод .plot() для Series и DataFrame объектов DataFrame, это всего лишь обёртка для plt.plot:
ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot();
show()


# In[21]:

plt.figure(); ts.plot(style='k--', label='Series'); plt.legend();
show()


# In[22]:

#Если применить эту же функцию к DataFrame, она выведет все имеющиеся колонки:
df = DataFrame(randn(1000, 4), index=ts.index, columns=list('ABCD'));
df = df.cumsum();

plt.figure(); 
df.plot(); 
plt.legend(loc='best');
show()


# In[23]:

#Легенда активно по умолчанию. Отключается она при помощи параметра legend=False
df = DataFrame(randn(1000, 4), index=ts.index, columns=list('ABCD'));
df = df.cumsum();

plt.figure(); 
df.plot(); 
df.plot(legend=False);
show()


# In[24]:

#Для того, чтобы перейти на логарифмическую шкалу надо задать параметр logy.
plt.figure();
ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
ts = np.exp(ts.cumsum())
ts.plot(logy=True);
show()


# In[25]:

#Также очень легко строится обычный график плотности распределения
ser = Series(randn(1000))
ser.plot(kind='kde');
show()


# In[ ]:



