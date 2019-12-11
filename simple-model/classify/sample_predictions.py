#!/usr/bin/env python
# coding: utf-8

# In[1]:


from match_my_voice_model import Model


# In[2]:


us = Model()


# In[3]:


input_str = 'Thank you to Great Republican @SenJohnKennedy for the job he did in representing both the Republican Party and myself against Sleepy Eyes Chuck Todd on Meet the Depressed!'


# In[4]:


us.predict(input_str)

