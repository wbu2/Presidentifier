#!/usr/bin/env python
# coding: utf-8

# In[1]:


from match_my_voice_model import Model


# In[2]:


us = Model()


# In[3]:


input_str = 'As I have stated strongly before, and just to reiterate, if Turkey does anything that I, in my great and unmatched wisdom, consider to be off limits, I will totally destroy and obliterate the Economy of Turkey (I’ve done before!). They must, with Europe and others, watch over...'


# In[4]:


us.predict(input_str)

