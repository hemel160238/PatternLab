# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:22:23 2019

@author: HEMEL
"""

import numpy as np
from scipy.spatial import distance
from tabulate import tabulate

def get_indexes_to_be_merged(entireList):
    
    List_with_only_values = []
    
    for row in entireList[1:]:
        
        value_list_row = []
        
        for eachValue in row[1:]:
            value_list_row.append(eachValue)
            
        List_with_only_values.append(value_list_row)
        
    #print(List_with_only_values)
    
    np_array = np.array(List_with_only_values)
    
    #print(np_array)
    
    min_value = np.min(np_array[np.nonzero(np_array)])
    
    #print("Min Value is {}".format(min_value))
    
    result = np.where(np_array == min_value)
    
    #print(result[0][0])
    #print(result[1][0])
    
    #print("The Position is {}".format(np.where(np_array == min_value)))

    return [result[0][0], result[1][0]]

def eucledian_distance(point1, point2):
    
    dst  = distance.euclidean(point1, point2)
    
    return dst


def get_min_distance(list1, list2, indexList):
    
    if set(list1) == set(list2):
        
        #return math.nan
        return int(0)
    
        
    else:
        #print("Lists are not same ")
        
        
        min_distance = 9999
        
        for class1 in list1:
            
            for class2 in list2:
                
                distance_calculated = eucledian_distance(indexList[class1 - 1], indexList[class2 - 1])
                
                if min_distance > distance_calculated:
                    
                    min_distance = distance_calculated
        
        #print("Minimum Distance is {}".format(min_distance))
        
        return min_distance
    
    

def get_init_matrix(indexList, classList):
    
    headerList = [' ']
    for eachClass in classList:
        headerList.append(eachClass)
    
    
    
    BroaderList = [headerList]
    
    
    for i in range(len(classList)):
        row = [classList[i]]
        
        for j in classList:
            
            distance_calculated = get_min_distance(classList[i], j, indexList)
            
            row.append(distance_calculated)
    
        BroaderList.append(row)

    
    print(tabulate(BroaderList[1:], headers=BroaderList[0], tablefmt='fancy_grid'))
    
    r, c = get_indexes_to_be_merged(BroaderList)
    
    #print("r is {} and c is {} ".format(r+1,c+1))
    
    return [r, c]
    
    
    
    pass

data = [[4, 4],
        [8, 4],
        [15, 8],
        [1, 11],
        [24, 12]]

#header = [[1], [2], [3], [4], [5]]
header = [[1], [2], [3], [4], [5]]



#r,c = get_init_matrix(data, header)

#header = [[1], [2], [3], [4], [5]]


while(len(header) > 1):
    
    r,c = get_init_matrix(data, header)
    
    new_header = []
    merged_list = header[r] + header[c]
    new_list = [merged_list]
    
    for i in range(len(header)):
        if(not (i == r or i == c)):
            new_list.append(header[i])
            
            
    header = new_list

    
    pass

print("Output : {}".format(header[0]))


