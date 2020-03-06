
# coding: utf-8

# In[107]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_excel('mtcars.xlsx')
#membuka dan membaca file mtcars yang ada di folder 

df['mpg level'] = ['hard' if x >30  else'medium' if x >20  else 'low' if x<10 else 'low' for x in df['mpg']] 
#membuat kolom baru 

print(df)
#dicetak

#scatter plot
mpg = df['mpg']
mpg_level = df['mpg level']
colors = (0,0,0)
area = np.pi*3

plt.scatter(mpg, mpg_level, s = area, c = colors, alpha = 0.5)
plt.title('Scatter plot')
plt.xlabel('mpg')
plt.ylabel('mpg level')
plt.show()

#


# In[ ]:





# In[93]:





# In[94]:


#scatter plot
mpg = df['mpg']
mpg_level = df['mpg level']
colors = (0,0,0)
area = np.pi*3

plt.scatter(mpg, mpg_level, s = area, c = colors, alpha = 0.5)
plt.title('Scatter plot')
plt.xlabel('mpg')
plt.ylabel('mpg level')
plt.show()


# In[ ]:



    

