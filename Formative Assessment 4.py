#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bin_to_dec(binary_string):
    new_binary_string = binary_string[::-1]
    index = 0 
    total = 0 
    
    while index != len(new_binary_string):
        calculation = int(new_binary_string[index]) * (2**index)
        total += calculation
        index += 1
    
    return total  


# In[3]:


def dec_to_bin(number):
    binary = ""
    
    if number == 0:
        return "0"
    
    while number != 0:
        binary += str(number%2)
        number = number // 2
        
    return binary[::-1]


# In[5]:


encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

def telephone_cipher(message):
    new_message = ""
    
    for i, char in enumerate(message): 
        if char in encoder_dict:
            number = str(encoder_dict[char])
            if i > 0 and encoder_dict[message[i-1]][0] == number[0]:
                new_message += "_"
            new_message += number 
        
    return new_message


# In[7]:


def telephone_decipher(telephone_string):

    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    
    new_message = ""

    i = 0
    while i < len(telephone_string):
        for j in range(4, 0, -1): 
            if i+j <= len(telephone_string):
                chunk = telephone_string[i:i+j]
                if chunk in decipher_dict:
                    new_message += decipher_dict[chunk]
                    i += j
                    break
        else:
            i += 1
    
    return new_message

