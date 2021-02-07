#!/usr/bin/env python
# coding: utf-8

# # IMDB Top Rated TV Shows

# In[204]:


# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[205]:


url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
response = requests.get(url)
imdb = response.text
soup = BeautifulSoup(imdb, 'html.parser')
table = soup.find(class_='chart full-width')
table_body = table.tbody


# In[206]:


movie_list = []
table_row = table_body.find_all('tr')
for i in range (0, len(table_row)):
    movie_name = table_row[i].find(class_='titleColumn').a.text.strip()
    movie_rating = table_row[i].find(class_='ratingColumn imdbRating').text.strip()
    rating_user = table_row[i].find(class_='ratingColumn imdbRating').strong['title']
    movie_year = table_row[i].find(class_='titleColumn').span.text
    data_dict = {}
    data_dict['Movie Name'] = movie_name + ' ' + movie_year
    data_dict['Movie Rating'] = movie_rating
    data_dict['Rating based on users'] = rating_user
    movie_list.append(data_dict)


# In[207]:


df = pd.DataFrame(movie_list)
df.columns = ['MOVIE NAME & YEAR', 'MOVIE RATINGS', 'RATING BASED ON USERS']
df.index.name = 'foo'
df.index = np.arange(1, len(df)+1)    


# In[208]:


df.index.name='S/No.'


# In[209]:


df.to_csv('imdb top tv show.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




