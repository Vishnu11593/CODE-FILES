#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def clean_text(text):
    """
    Cleans the given text by:
    - Converting it to lowercase.
    - Removing special characters.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text
input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)
print("Original Text:")
print(input_text)
print("\nCleaned Text:")
print(cleaned_text)


# In[ ]:




