#!/usr/bin/env python
# coding: utf-8

# # Input-Output and Strings

# In[1]:


Data= "Data Science Fun"


# In[2]:


type (Data)#Checking the type


# In[3]:


Data=input() #Taking data via input function


# In[4]:


Data


# In[5]:


type(Data)


# In[6]:


x=input()
y=input()


# In[7]:


x+y #Values stored in x and y as string.


# In[8]:


type (x)


# In[9]:


type (y)


# In[10]:


x=int(x)#Conversion of x from string to int.


# In[11]:


x


# In[12]:


type(x)


# In[13]:


y=int(y)


# In[14]:


y


# In[15]:


x+y


# In[17]:


x= int(input("Enter a value for x=  ")) #Taking int value for x and y
y= int(input("Enter a value for y=  "))


# In[18]:


print (x+y)


# In[19]:


a= float(input("Enter a value for a=  ")) #Taking float value for a and b
b= float(input("Enter a value for b=  "))
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(b*b)


# STRING

# In[20]:


len("NAYEEM the Data Analyst") #Checking legth of a string


# In[23]:


Dream= "NAYEEM the Data Analyst"


# In[25]:


import sys
sys.getsizeof(Dream) #Checking the size of Dream variable


# In[26]:


Dream.count("Data") #Checking how many times "data" word is available in Dream variable 


# In[30]:


Dream.find("Data") #Tracking the location of a word using find function


# In[31]:


Dream.find("E") #Tracking the location of a letter (The first one avialable)


# In[32]:


Dream.find("E",4,8) #Tracking the location of a letter within a range


# In[33]:


Dream.index("Data") #Tracking the location of a word using index function


# In[34]:


Dream.index("E") #Tracking the location of a letter via index function


# In[35]:


Dream.find("Z") #find function shows (-1) when unavailable


# In[36]:


Dream.index("Z") #index function shows error when unavailable


# In[37]:


Dream.lower() #Convert to lower case


# In[39]:


Dream.upper() #Convert to upper case


# In[40]:


Dream.capitalize() #Capitalize the first letter


# In[41]:


Dream.title() #Capitalize the first letter of each word


# In[42]:


Dream.encode()#Convert to encoded version


# In[44]:


type(Dream.encode())


# In[45]:


Dream.split ()#Split and show as a list


# In[46]:


Dream.split ()[0]


# In[47]:


Dream.split ()[2]


# In[49]:


Dream.split ()[3]


# In[ ]:




