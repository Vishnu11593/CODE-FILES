#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
url = "https://example.com"
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    print(f"Title of the webpage: {title}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")


# In[ ]:




