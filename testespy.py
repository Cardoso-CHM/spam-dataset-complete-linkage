# -*- coding: utf-8 -*-
import numpy as np

def euc(obj_a, obj_b): 
    return np.linalg.norm(obj_a - obj_b)

# função que remove a linha e coluna de maior indice
def remove_column_line(matrix,index): 
    # TO DO
    # matrix = matrix.drop([index])
    # matrix = matrix.drop(columns=[index])
    return matrix

# função que pega o max de ((pi,pj), pk) e atualizar valor na tabela
def calc_max(i, j): 
    # percorre todos os indices do array, 0-length
    for k, obj_k in enumerate(data):
        # o calculo so é feito nos pk que nao estao em (pi, pj)
        if(k != i and k != j):
            # se i for maior que k, a ordem das coordenadas na tabela é dirente
            if(i > k) :
                max_ik = distance_matrix[k][i]
                # se j for maior que k, a ordem das coordenadas na tabela é dirente
                if(j > k):
                    max_jk = distance_matrix[k][j]
                else :
                    max_jk = distance_matrix[j][k]
                # pegando o max da coordenada (pi, pk) e (pj, pk)
                distance_matrix[k][i] = max(max_ik, max_jk) 
            else :
                max_ik = distance_matrix[i][k]
                if(j > k):
                    max_jk = distance_matrix[k][j]
                else :
                    max_jk = distance_matrix[j][k]
                distance_matrix[i][k] = max(max_ik, max_jk) 

data = np.array([
        [0.40, 0.53],
        [0.22, 0.38],
        [0.35, 0.32],
        [0.26, 0.19],
        [0.08, 0.41],
        [0.45, 0.30]]);

rows, cols = data.shape
distance_matrix = np.zeros([rows, rows])
min_value = {'value': euc(data[0], data[1]) , 'i': 0, 'j': 1}

for row, p1 in enumerate(data):
    for col, p2 in enumerate(data):
        if(row > col):
            distance = euc(p1, p2)
            distance_matrix[row][col] = distance

            if(distance < min_value['value'] and distance > 0.0):
                min_value = {'value': distance, 'i': row, 'j': col}
        else:
            distance_matrix[row][col] = 0
            
print(distance_matrix, "\n")
print(min_value, "\n")

i = min_value['i']
j = min_value['j']

calc_max(i, j)
        
if(i < j):
    distance_matrix = remove_column_line(distance_matrix, j)
else:
    distance_matrix = remove_column_line(distance_matrix, i)
    
print(distance_matrix)





