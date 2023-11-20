#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import math

def fitness(totall_amount, list1):
    sum_cal = 0
    for index in range(len(totall_amount)):
        if(list1[index] != 0):
            sum_cal += totall_amount[index]
    return abs(sum_cal)

def crossover(list_another, new):
    idx = random.randint(1, new-1)
    crossovere1 = random.randint(0, len(list_another)-1) 
    crossovere2 = random.randint(0, len(list_another)-1) 
    new_list_1 = list_another[crossovere1][:idx] + list_another[crossovere2][idx:]
    new_list_2 = list_another[crossovere2][:idx] + list_another[crossovere1][idx:]
    return new_list_1, new_list_2

def mutation(list3):
    idx2 = random.randint(0, len(list3)-1)
    list3[idx2] = 1 - list3[idx2]
    return list3

result = -1
count = 0
totall_amount = []
input_num = int(input())
for idx_11 in range(input_num):
    input2 = input().split(" ")

    if(input2[0] == "l"):
        totall_amount.append(int(input2[1]) * -1)
    else:
        totall_amount.append(int(input2[1]))


while True:
    if count>10000:
        break
    list_another = []
    for idx_i in range(input_num+1):
        temp_var = [random.randint(0, 1) for idx_i2 in range(input_num) ]
        while temp_var.count(0) == input_num:
            temp_var = [random.randint(0, 1) for idx_i3 in range(input_num) ]
        list_another.append(temp_var)

    maximum_cal = -math.inf
    for indxx in list_another:
        output = fitness(totall_amount, indxx)
        maximum_cal = max(maximum_cal, output)
        if(output == 0) and indxx.count(0) != input_num:
            result = "".join([str(idx_j) for idx_j in indxx])
            break
    
    for idx_22 in range(input_num+1):
        if(fitness(totall_amount, list_another[idx_22]) == maximum_cal):
            list_another.pop(idx_22)
            break

    for idx_33 in list_another:
        output = fitness(totall_amount, idx_33)
        maximum_cal = max(maximum_cal, output)
   
    for idx_44 in range(input_num):
        if(fitness(totall_amount, list_another[idx_44]) == maximum_cal):
            list_another.pop(idx_44)
            break
    final_output1, final_output2 = crossover(list_another, input_num)
    final_output1 = mutation(final_output1)
    final_output2 = mutation(final_output2)
    while final_output1.count(0) == input_num and input_num > 1:
        final_output1 = mutation(final_output1)
    while final_output2.count(0) == input_num and input_num > 1:
        final_output2 = mutation(final_output2)
    count += 1
    
print(result)


# In[ ]:




