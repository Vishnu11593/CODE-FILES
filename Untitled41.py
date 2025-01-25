#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.corpus import stopwords
import spacy
nltk.download('stopwords')
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    processed_text = [token.text for token in doc if token.text not in stop_words and not token.is_punct]
    return " ".join(processed_text)
text = input("Enter the text: ")
cleaned_text = preprocess_text(text)
print("\nProcessed Text:")
print(cleaned_text)

