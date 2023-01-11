#!/usr/bin/env python
# coding: utf-8

# In[10]:


pip install bitcoin


# In[2]:


from bitcoin import *


# In[3]:


my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)


# In[4]:


my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)


# In[5]:


my_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" % my_address)


# In[19]:


private_key1 = random_key()
private_key2 = random_key()
private_key3 = random_key()
private_key4 = random_key()
print("CEO Private Key: %s\n" % private_key1)
print("Alice Private Key: %s\n" % private_key2)
print("Bob Private Key: %s\n" % private_key3)
print("Coo Private Key: %s\n" % private_key3)


# In[21]:


public_key1 = privtopub(private_key1)
public_key2 = privtopub(private_key2)
public_key3 = privtopub(private_key3)
public_key4 = privtopub(private_key4)
print("CEO Public Key: %s\n" % public_key1)
print("Alice Public Key: %s\n" % public_key2)
print("Bob Public Key: %s\n" % public_key3)
print("Coo Public Key: %s\n" % public_key4)


# In[23]:


my_mulit_sig = mk_multisig_script(private_key1, private_key2, private_key3, private_key4, 3, 4)
my_mulit_address = scriptaddr(my_mulit_sig)
print("Multisignature Address: %s\n" % my_mulit_address)


# In[9]:


valid_address = '1KokfmiMAkpnqDTt3aKVkrEf6Hsagpbz8B'
print(history(valid_address))


# In[ ]:




