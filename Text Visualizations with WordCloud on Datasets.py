#!/usr/bin/env python
# coding: utf-8

# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Text to generate the WordCloud
text = "data science machine learning artificial intelligence"

# Generate the WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(text)

# Save the WordCloud as an image file
wordcloud.to_file("wordcloud.png")

# Display the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

print("WordCloud image saved as 'wordcloud.png'.")


# In[ ]:




