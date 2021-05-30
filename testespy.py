# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:59:52 2021

@author: César Cardoso
"""
import numpy as np
import pandas as pd

def euc(obj_a, obj_b): 
    return np.linalg.norm(obj_a - obj_b)


data = np.array([
        [0.40, 0.53],
        [0.22, 0.38],
        [0.35, 0.32],
        [0.26, 0.19],
        [0.08, 0.41],
        [0.45, 0.30]]);

dist = {}
min_value = {'value': euc(data[0], data[1]) , 'i': -1, 'j': -1}

for i, p1 in enumerate(data):
    dist[i] = {}
    for j, p2 in enumerate(data):
        if(i < j):
            distance = euc(p1, p2)
            dist[i][j] = distance

            if(distance < min_value['value']):
                min_value = {'value': distance, 'i': i, 'j': j}
        else:
            dist[i][j] = 0
        
distance_matrix = pd.DataFrame.from_dict(dist)

print(distance_matrix)
print(min_value)