#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS, stem_text
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk import download
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
import string
download('wordnet')
download('omw-1.4')
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    text = text.lower()
    tokens = simple_preprocess(text, deacc=True)  
    tokens = [token for token in tokens if token not in STOPWORDS]
    stemmed_tokens = [stem_text(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]
    
    return lemmatized_tokens
file_path = "sample_text.txt"  
with open(file_path, 'r') as file:
    text = file.read()
processed_text = preprocess_text(text)
print("Original Text:")
print(text)
print("\nProcessed Tokens:")
print(processed_text)


# In[ ]:




