# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:10:42 2019

@author: HEMEL
"""

def update_functions(given_functions, calculated_member, test_sample_actual_member, c, k, test_sample_ws):
    
    corrected_list = []
    
    function_num_to_be_reduced = 0
    function_num_to_be_increased = 0
    
    i = 0
    
    for function in given_functions:
        
        if calculated_member == function[0]:
            function_num_to_be_reduced = i
            
        elif test_sample_actual_member == function[0]:
            function_num_to_be_increased = i
        i += 1
        
    function_to_be_reduced = given_functions[function_num_to_be_reduced]
    function_to_be_increased = given_functions[function_num_to_be_increased]
    
    #print(" Reduce {}".format(function_to_be_increased))
    
    
    function_to_be_reduced[1] = function_to_be_reduced[1] - c*k
    for i in range(2, len(function_to_be_reduced)):
        function_to_be_reduced[i] = function_to_be_reduced[i] - c*test_sample_ws[i-2]
        
        
    function_to_be_increased[1] = function_to_be_increased[1] + c*k
    for i in range(2, len(function_to_be_increased)):
        function_to_be_increased[i] = function_to_be_increased[i] + c*test_sample_ws[i-2]
        
    #print(" Reduce {}".format(function_to_be_increased))

    
    for i in range(len(given_functions)):
        
        if i == function_num_to_be_reduced:
            corrected_list.append(function_to_be_reduced)
            
        elif i == function_num_to_be_increased:
            corrected_list.append(function_to_be_increased)
            
        else:
            corrected_list.append(given_functions[i])
    
    return corrected_list



def calculate_membership(given_functions, test_sample_feature_values):
    
    class_distance_list = []
    
    for function in given_functions:
        
        local_total = 0
        
        for i in range(2, len(function)):
            local_total += function[i] * test_sample_feature_values[i-2]
        
        local_total += function[1]
        
        class_distance_list.append([function[0], local_total])
        
    sorted_class_distance_list = sorted(class_distance_list, key = lambda x: x[1], reverse = True)
        
    
    #print(sorted_class_distance_list)
    
    return sorted_class_distance_list[0][0]
    pass

#individua functions like [func_number, wo, w1, w2, w3]
given_functions = [
            ['c1', 3, 4, 5, 6],
            ['c2', 7, 2, -3, 4],
            ['c3', -2, -4, 6, 8],
            ['c4', 5, 6, -7, 8]
            ]

#test sample x, y, z values
test_sample_ws = [1, 2, 3]

test_sample_actual_member = 'c3'

C = 1
K = 3

calculated_member = calculate_membership(given_functions, test_sample_ws)

print(calculated_member)

dummy_list = given_functions

if not calculated_member == test_sample_actual_member:
    print("HOyyyyy Nai ")
    
    updated_function = update_functions(dummy_list, calculated_member, test_sample_actual_member, C, K, test_sample_ws)


for list in given_functions:
    print(list)
