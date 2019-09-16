# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:11:22 2019

@author: HEMEL
"""

from tabulate import tabulate

def get_D(w_value_set, x_first):
    
    total_value = 0
    
    for i in range(len(x_first)):
        total_value += w_value_set[i+1] * x_first[i]
    
    
    return total_value + w_value_set[0]


def update_D_w_value_set(w_value_set, C, d, K, x_first):
    
    w_value_set[0] = w_value_set[0] + C*d*K
    
    print("len w_value_set {}".format(len(w_value_set)))
    
    for i in range(1, len(w_value_set)):
        
        w_value_set[i] = w_value_set[i] + C*d*x_first[i-1]
        
        #print("w_value_set {} C {} d {} x_first {}".format(w_value_set[i], C, d, x_first[i-0]))
    
    return w_value_set

result_array = []

C = 1
K = 1

#            [i   x   d]
test_data = [[1, -4, -1],
             [2, -1, 1]]

x_first = test_data[0][1:-1]
x_second = test_data[1][1:-1]

w_value_set = [0, 0]

instance_1_actual_class_d1 = test_data[0][-1]
instance_2_actual_class_d2 = test_data[1][-1]

t_value = 1

while(True):
    
    
    D_for_1 = get_D(w_value_set, x_first)
    
    if(D_for_1 >= 0):
        predicted_class_1 = 1
        
    else:
        predicted_class_1 = -1
        
        
    if(predicted_class_1 == instance_1_actual_class_d1):
        
        error_1 = 'No'
        
    else:
        error_1 = 'Yes'
        
        
    if(error_1 == 'Yes'):
        w_value_set = update_D_w_value_set(w_value_set, C, instance_1_actual_class_d1, K, x_first)
    
    result_array.append([t_value, 1, x_first[0], instance_1_actual_class_d1, w_value_set[0], w_value_set[1], D_for_1, error_1, w_value_set[0], w_value_set[1]])
    
    t_value += 1
    
    D_for_2 = get_D(w_value_set, x_second)
    
    if(D_for_2 >= 0):
        predicted_class_2 = 1
        
    else:
        predicted_class_2 = -1
        
        
    if(predicted_class_2 == instance_2_actual_class_d2):
        
        error_2 = 'No'
        
    else:
        error_2 = 'Yes'
        
    if(error_2 == 'Yes'):
        w_value_set = update_D_w_value_set(w_value_set, C, instance_2_actual_class_d2, K, x_second)
    
        
        
    result_array.append([t_value, 2, x_second[0], instance_2_actual_class_d2, w_value_set[0], w_value_set[1], D_for_2, error_2, w_value_set[0], w_value_set[1]])
    t_value += 1
    
    if error_1 == error_2 == 'No':
        
        break
    



    
print(tabulate(result_array, headers = ['t', 'i', 'x', 'd', 'Old w0', 'Old w1', 'D', 'Error?', 'New w0', 'New w1'], tablefmt='orgtbl'))
