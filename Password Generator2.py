#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries

import pandas as pd
from numpy.random import randint
import string
from random import *


# In[2]:


#Asking the user to specify length of password 
length = int(input("How many characters would you like to have in your password? (Your password should be a minimum of 6 characters long)"))

while length < 6:
  length = int(input("Please enter a number higher than 6"))


# Asking the user to select the number of letters in the password
no_letters = int(input("How many letters would you like to have in your password?"))

while no_letters > length:
  no_letters = int(input("The number of letters should be less than the total. How many letters would you like to have in your password?"))


# Asking the user to select the number of digits in the password
no_digits = int(input("How many digits would you like to have in your password?"))

while no_digits + no_letters > length:
  no_digits = int(input("The total number of numbers and letters combined should be less than the total. How many numbers would you like to have in your password?"))



# writing the function

def password(length, no_letters, no_digits):
  """Get a random password with user input"""

  # Random digits
  characters = ''.join(choice(string.digits) for i in range(no_digits))

  # Random letters
  characters += ''.join(choice(string.ascii_letters) for i in range(no_letters))

  # Random symbols
  symbols = length - (no_letters + no_digits) # Calculating number of symbols

  characters += ''.join(choice(string.punctuation) for i in range(symbols))


 
  all_characters = list(characters) 

  shuffle(all_characters)       # mixing characters for more randomness

  password = ''.join(all_characters) 

  print("Your password is:", password)

# Calling the function

password(length, no_letters, no_digits)


# In[ ]:




