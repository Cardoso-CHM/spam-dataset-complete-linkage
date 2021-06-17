# -*- coding: utf-8 -*-
import numpy as np

def distance_function(obj_a, obj_b): 
    # return sum(abs(val1 - val2) for val1, val2 in zip(obj_a, obj_b)) # manhattan
    return np.linalg.norm(obj_a - obj_b) # euclidean

# função que remove a linha e coluna de maior indice
def remove_column_line(matrix,index):     
    matrix = np.delete(matrix, (index), axis=0)
    matrix = np.delete(matrix, (index), axis=1)
    
    return matrix

def get_min_value_indexes(d_matrix):
    filter_arr = (d_matrix > 0)
    non_zero_values = d_matrix[filter_arr]
    
    min_value = np.amin(non_zero_values)
    aux2 = np.where(d_matrix == min_value)
    
    return aux2[1][0], aux2[0][0]

# função que pega o max de ((pi,pj), pk) e atualizar valor na tabela
def update_distance_matrix(d_matrix, i, j):
    # percorre todos os indices do array, 0-length
    for k, obj_k in enumerate(d_matrix):
        # o calculo so é feito nos pk que nao estao em (pi, pj)
        if(k != i and k != j):
            # se i for maior que k, a ordem das coordenadas na tabela é dirente
            if(i > k) :
                max_ik = d_matrix[i][k]
                # se j for maior que k, a ordem das coordenadas na tabela é dirente
                if(j > k):
                    max_jk = d_matrix[j][k]
                else :
                    max_jk = d_matrix[k][j]
                # pegando o max da coordenada (pi, pk) e (pj, pk)
                # print(max_ik, max_jk)
                d_matrix[i][k] = max(max_jk, max_ik) 
            else :
                max_ik = d_matrix[k][i]
                if(j > k):
                    max_jk = d_matrix[j][k]
                else :
                    max_jk = d_matrix[k][j]
                    
                # print(max_ik, max_jk)
                d_matrix[k][i] = max(max_jk, max_ik)

def initialize_distance_matrix(dataset):

    # separando as classes da matriz
    data, classes = dataset[:,:-1] , dataset[:, -1] 
    
    rows, cols = data.shape
    
    new_distance_matrix = np.zeros([rows, rows])
    
    for row, p1 in enumerate(data):
        for col, p2 in enumerate(data):
            if(row > col):
                distance = distance_function(p1, p2)
                new_distance_matrix[row][col] = distance
                
            else:
                new_distance_matrix[row][col] = 0
                
    return new_distance_matrix, classes

def main():
    data_set = np.genfromtxt('spambase.csv', delimiter=',')
    
    distance_matrix, classes = initialize_distance_matrix(data_set)
    
    groups = [[i] for i in range(len(distance_matrix))]
    
    while len(groups) > 2:
        min_i, min_j = get_min_value_indexes(distance_matrix)
        
        update_distance_matrix(distance_matrix, min_i, min_j)    
        
        if(min_i < min_j):
            groups[min_i].extend(groups[min_j])
            groups.pop(int(min_j))
            distance_matrix = remove_column_line(distance_matrix, min_j)
        else:
            groups[min_j].extend(groups[min_i])
            groups.pop(int(min_i))
            distance_matrix = remove_column_line(distance_matrix, min_i)
            
    print(groups)
    
if __name__ == "__main__":
    main()