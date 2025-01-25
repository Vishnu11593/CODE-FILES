#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install spacy


# In[ ]:


python -m spacy download en_core_web_sm


# In[ ]:


python pos_tagging.py


# In[ ]:


for token in doc:
    print(f"{token.text}: {token.pos_} ({spacy.explain(token.pos_)}), Dependency: {token.dep_}")


# In[ ]:


from spacy import displacy
displacy.serve(doc, style="dep")

