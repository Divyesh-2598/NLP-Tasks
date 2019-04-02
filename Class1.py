#!/usr/bin/env python
# coding: utf-8

# In[20]:


import nltk


# In[21]:


nltk.download()


# In[22]:


from nltk.book import*


# In[23]:


from nltk.corpus import brown


# In[24]:


brown.categories()


# In[25]:


brown.words(categories = "humor")


# In[26]:


from nltk.corpus import inaugural


# In[27]:


inaugural.words()


# In[28]:


import nltk
from nltk.corpus import stopwords
stopwords.words('english')


# In[29]:


import nltk
from nltk.corpus import stopwords
stopwords.words('swedish')


# In[30]:


entries = nltk.corpus.cmudict.entries()
len(entries)


# In[31]:


for entry in entries[10000:10025]:
    print(entry)


# In[32]:


from nltk.corpus import wordnet as wn
wn.synsets('motorcar')  #synsets= synonyms sets


# In[33]:


wn.synset('car.n.01').lemma_names()


# In[34]:


texts = ["""VIT offers academic programs in Engineering, Technology, Applied Sciences, and Management. It offers 20 undergraduate programs, 34 postgraduate, four integrated MS courses, and four doctoral programs. VIT consolidated its disciplines into 10 Schools of Study with the addition of the VIT Law School at its Chennai campus.Research centers are part of the schools to encourage collaboration between the research and coursework areas and provide an opportunity for coursework students to participate in research projects. VIT organizes industrial workshops like Automotive Engineering, organized by ParaMek Technologies in GraVitas Fest."""]
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        print(tagged_words)


# In[35]:


from nltk.stem import PorterStemmer
stemmerporter = PorterStemmer()
stemmerporter.stem('working')


# In[36]:


stemmerporter.stem('shipping')


# In[37]:


stemmerporter.stem('troubling')


# In[38]:


stemmerporter.stem('swimming')


# In[58]:


stemmerlancaster.stem('mining')


# In[40]:


stemmerporter.stem('managing')


# In[41]:


stemmerporter.stem('computing')


# In[42]:


stemmerporter.stem('happiness')


# In[43]:


stemmerporter.stem('Dying')


# In[44]:


from nltk.stem import LancasterStemmer
stemmerlancaster = LancasterStemmer()
stemmerlancaster.stem('working')


# In[69]:


stemmerlancaster.stem('dying')


# In[68]:


stemmerporter.stem('dying')


# In[48]:


stemmerlancaster.stem('Troubling')


# In[49]:


stemmerlancaster.stem('disadvantage')


# In[50]:


stemmerlancaster.stem('unorganized')


# In[51]:


stemmerporter.stem('unorganized')


# In[52]:


stemmerporter.stem('disadvantage')


# In[53]:


stemmerlancaster.stem('unorganized')


# In[54]:


stemmerlancaster.stem('mixing')


# In[55]:


print(stemmerlancaster.stem('unorganized'))


# In[57]:


print(stemmerlancaster.stem('disadvantage'))
print(stemmerporter.stem('disadvantage'))


# In[ ]:




