#!/usr/bin/env python
# coding: utf-8

# In[1]:


def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            return "friends"
        else:
            return "follower"
            
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship" 


# In[3]:


def tic_tac_toe(board):

    board_size = len(board)
    
    for row_no in range(board_size):
        #check the rows
        if len(set(board[row_no])) == 1 and board[row_no][0] != '':  
            return board[row_no][0]
        #check the columns
        column = [board[col_no][row_no] for col_no in range(board_size)]
        if len(set(column)) == 1 and column[0] != '':
            return column[0]
        
    #check the diagonal 
    diagonal1 = [board[row_no][row_no] for row_no in range(board_size)] 
    if len(set(diagonal1)) == 1 and diagonal1[0] != '':
        return diagonal1[0]

    #check the other diagonal 
    diagonal2 = [board[row_no][board_size - 1 - row_no] for row_no in range(board_size)]
    if len(set(diagonal2)) == 1 and diagonal2[0] != '':
        return diagonal2[0]
    
    #if there is no winner
    return "NO WINNER"


# In[5]:


def eta(first_stop, second_stop, route_map):
    time = 0

    while first_stop != second_stop:
        for key in route_map:
            if key[0] == first_stop:
                time += route_map[key]['travel_time_mins']
                first_stop = key[1]
                break

    return time

