#!/usr/bin/env python
# coding: utf-8

# In[6]:


from translate import Translator


translator = Translator(from_lang='en', to_lang='hi')  # from English to hindi


text = 'Hello, how are you?'


translation = translator.translate(text)


print(f'Text: {text}')
print(f'Translation: {translation}')


# In[ ]:





# In[ ]:





# In[ ]:




