import numpy as np
import pandas as pd

def euc(obj_a, obj_b): 
    return np.linalg.norm(obj_a - obj_b)

dataset = np.genfromtxt('spambase.csv', delimiter=',')

# separando as classes da matriz e colocando num vetor chamado "classes"
data,classes = dataset[:,:-1] , dataset[:, -1] 

# pegando o maior e menor valor de cada coluna e colocando numa matriz [2,n] onde n é o numero de atributos
min_max = np.matrix([np.min(data,axis = 0), np.max(data,axis = 0)]).astype(int) 

# aplicando tratamento de dados min-max (normalizacao)
data = np.array((data[:,:] - min_max[0, :])/ (min_max[1,:] - min_max[0,:])) 

dist = {}
min_value = {'value': -1, 'i': -1, 'j': -1}

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
