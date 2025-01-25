#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def extract_emails(text):
    """
    Extracts all email addresses from the given string using regular expressions.

    Args:
        text (str): The input string containing email addresses.

    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails
input_text = 'Contact us at support@example.com and sales@example.org.'
extracted_emails = extract_emails(input_text)
print("Original Text:")
print(input_text)
print("\nExtracted Email Addresses:")
print(extracted_emails)


# In[ ]:




