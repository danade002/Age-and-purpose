#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    print ("Welcome to my world- Daniel Ademeso")
    print('')

    Age = int (input("Enter your age: "))
    if Age<0:
        print ("It is impossible, you cannot have a negative age")
    elif Age==0:
        print ("Are a toddler? or you mistakenly entered the wrong age?")
    elif Age>0 and Age<18:
        print ("You are a tennager, you are still pretty young, keep growing!")
    elif Age>18 and Age<45:
        print ("You are in the period that determines what you will be in future, Use this period!")
    else:
        print("You are in the future already but you can still make things happen")
except ValueError:
    print("Invalid characters, enter number>=0")


# In[ ]:



        
        
    
        


# In[ ]:





# In[ ]:




