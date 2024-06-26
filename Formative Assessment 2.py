#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shift_letter(letter,shift):
    letter = str(letter)
    shift = int(shift)
    
    if letter == " ":
        return " "
    else: 
        shifted_letter = (ord(letter) - ord("A") + shift) % 26 + ord("A")
        return chr(shifted_letter) 


# In[3]:


def caesar_cipher(message, shift):
    message = str(message) 
    shift = int(shift) 
    final_message = "" 
    
    for character in message:
        if character == " ": 
            final_message += " "
        if character.isupper():
            shifted_character = chr((ord(character) - ord("A") + shift) % 26 + ord("A"))

            final_message += shifted_character

    return final_message


# In[5]:


def shift_by_letter(letter, letter_shift):
    letter = str(letter) 
    letter_shift = str(letter_shift)
    
    if letter == " ":
        return " "
    else:
        shift = ord(letter_shift) - ord("A")
        shifted_letter = (ord(letter) - ord("A") + shift) % 26 + ord("A")
        return chr(shifted_letter)


# In[7]:


def vigenere_cipher(message, key):
    message = str(message)
    key = str(key)
    index = 0
    final_message = ""  
    
    for char in message: 
        if char == " ":
            final_message += " "
            index += 1
        elif char.isupper(): 
            shift = ord(key[index % len(key)]) - ord("A")
            shifted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            final_message += shifted_char
            index += 1
    return final_message


# In[9]:


def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += '_'
        
    encoded_message = ''
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[index]
    return encoded_message


# In[11]:


def scytale_decipher(message, shift):
    deciphered_message = ''
    new_shift = len(message)//shift
    
    for i in range(len(message)):
        index = (i // new_shift) + (len(message) // new_shift) * (i % new_shift)
        deciphered_message += message[index]
    
    return deciphered_message

