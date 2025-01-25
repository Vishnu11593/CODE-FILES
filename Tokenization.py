#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

def tokenize_paragraph(paragraph):
    sentences = sent_tokenize(paragraph)
    words = word_tokenize(paragraph)
    return sentences, words
paragraph = """
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence.
It focuses on the interaction between computers and humans through natural language.
Tokenization is one of the fundamental steps in NLP.
"""
sentences, words = tokenize_paragraph(paragraph)
print("Original Paragraph:")
print(paragraph)
print("\nTokenized Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")
print("\nTokenized Words:")
print(words)


# In[ ]:




