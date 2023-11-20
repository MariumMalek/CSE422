#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
import random 
def minimax(depth_of_tree,thrd_idx_number_of_bullets, maximizing,lst_of_tree, value_of_alpha, value_of_beta,node_depth=0, position_of_value=0): 
    global node_visited 
    if node_depth == depth_of_tree: 
        node_visited += 1
        return lst_of_tree[position_of_value] 
    if maximizing: 
        best_of_value = float("-inf") 
        for idxx in range(0, thrd_idx_number_of_bullets):
            value_of_child_node=position_of_value * 2 + idxx
            value_of_max = minimax(depth_of_tree,thrd_idx_number_of_bullets,False, lst_of_tree, value_of_alpha, value_of_beta,node_depth + 1, value_of_child_node) 
            best_of_value = max(best_of_value, value_of_max) 
            value_of_alpha = max(value_of_alpha, best_of_value) 
            if value_of_beta <= value_of_alpha: 
                break
        return best_of_value 
    else:
        best_of_value = float("inf")
        for idx2 in range(0, thrd_idx_number_of_bullets):
            value_of_child_node=position_of_value * 2 + idx2 
            value_of_min = minimax(depth_of_tree,thrd_idx_number_of_bullets,True, lst_of_tree, value_of_alpha, value_of_beta,node_depth + 1, value_of_child_node) 
            best_of_value = min(best_of_value, value_of_min) 
            value_of_beta = min(value_of_beta, best_of_value) 
            if value_of_beta <= value_of_alpha: 
                break
        return best_of_value


student_id= (input('Enter your student id: '))

number_of_turns_1st_dig= int(student_id[0])
depth_of_tree=number_of_turns_1st_dig*2
# print('depth_of_tree',depth_of_tree)
initial_lifeline_last_two_dig=int(student_id[-2:][::-1])
# print((initial_lifeline))
thrd_idx_number_of_bullets=int(student_id[2:3])
# print('number_of_bullets',thrd_idx_number_of_bullets)

range_of_value =input('Minimum and Maximum value for the range of negative HP: ')
minimum_value=int(range_of_value [0])
maximum_value =int(range_of_value [-2:])
# print(maximum_value)
# print(minimum_value)

loop_range=thrd_idx_number_of_bullets**depth_of_tree
# print(loop_range)
idx=0
lst_of_tree=[]
while idx< loop_range:
    lst_of_tree.append(random.randint(minimum_value,maximum_value))
    idx=idx+1


value_of_beta1,value_of_alpha1  = float("inf"), float("-inf")
node_visited = 0
optimal = minimax(depth_of_tree,thrd_idx_number_of_bullets, True, lst_of_tree, value_of_alpha1, value_of_beta1)

string=str(lst_of_tree[0])
for i in lst_of_tree[1::]:
    string=string+","+str(i)
print(f'Depth and Branches ratio is {depth_of_tree}:{thrd_idx_number_of_bullets}')
print(f'Terminal States(Leaf Nodes) are {string}.')
print('Left life(HP) of the defender after maximum damage caused by the attacker is',initial_lifeline_last_two_dig-optimal)
print('After Alpha-Beta Pruning Leaf Node Comparisons', node_visited)


# In[ ]:




