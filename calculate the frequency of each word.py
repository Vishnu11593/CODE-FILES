#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import Counter

def calculate_word_frequency(text):
    words = text.lower().split()
    word_count = Counter(words)
    return word_count
text = input("Enter the text: ")
word_frequency = calculate_word_frequency(text)
print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")


# In[ ]:




