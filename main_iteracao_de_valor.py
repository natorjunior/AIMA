# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 03:24:56 2019

@author: Trisa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 01:35:18 2019

@author: Trisa
"""
import numpy as np

def U(s,estados,num_linhas,num_cols):
    u = -0.04 
    S = [[s[0],s[1]+1],#direita
       [s[0],s[1]-1],#esquerda
       [s[0]-1,s[1]],#cima
       [s[0]+1,s[1]],#baixo
       ]
    #print(s,S)
    aux=[]
    cont = 0
    for i in S:
        estads_possiveis = []
        if cont == 0:#direita
            x = 0
            estads_possiveis.append([i[0],i[1]])
            estads_possiveis.append([S[2][0],S[2][1]])
            estads_possiveis.append([S[3][0],S[3][1]])
            print('direita',estads_possiveis)
            for j in range(len(estads_possiveis)):
                if estads_possiveis[j][0] < 0 or estads_possiveis[j][0] >= num_linhas or estads_possiveis[j][1] < 0 or estads_possiveis[j][1] >= num_cols or (estads_possiveis[j][0] == 1 and estads_possiveis[j][1] == 1) :
                    if j == 0:
                        x = 0.8*estados[s[0]][s[1]]
                    else:
                        x += 0.1*estados[s[0]][s[1]]
                else:
                    if j == 0:
                        x = 0.8*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
                    else:
                        x += 0.1*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
            x = u+x
            #verifica se é um estado terminal ou bloqueado
            if (s[0]==1  and s[1] == 1):  
                pass
                #print('bloqueado',s)
            elif (s[0] == 3 and s[1] == 1):
                pass
                #print('terminais negativo',s)
            elif (s[0] == 3 and s[1] == 2):
                pass
                #print('terminais positivo',s)
            else:
                 aux.append(x)
            #print(x,i,s,estados)
        elif cont == 1:#esquerda
            estads_possiveis.append([i[0],i[1]])
            estads_possiveis.append([S[2][0],S[2][1]])
            estads_possiveis.append([S[3][0],S[3][1]])
            print('esquerda',estads_possiveis)
            x = 0
            for j in range(len(estads_possiveis)):
                #verifica se ultrapassa os limites, estados bloqueados.
                if estads_possiveis[j][0] < 0 or estads_possiveis[j][0] >= num_linhas or estads_possiveis[j][1] < 0 or estads_possiveis[j][1] >= num_cols or (estads_possiveis[j][0] == 1 and estads_possiveis[j][1] == 1) :
                    if j == 0:
                        x = 0.8*estados[s[0]][s[1]]
                    else:
                        x += 0.1*estados[s[0]][s[1]]
                else:
                    if j == 0:
                        x = 0.8*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
                    else:
                        x += 0.1*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
            x = u+x
            #verifica se é um estado terminal ou bloqueado
            if (s[0]==1  and s[1] == 1):  
                pass
                #print('bloqueado',s)
            elif (s[0] == 3 and s[1] == 1):
                pass
                #print('terminais negativo',s)
            elif (s[0] == 3 and s[1] == 2):
                pass
                #print('terminais positivo',s)
            else:
                 aux.append(x)
            #print(x,i,s,estados)

        elif cont == 2:#cima
            estads_possiveis.append([i[0],i[1]])
            estads_possiveis.append([S[0][0],S[0][1]])
            estads_possiveis.append([S[1][0],S[1][1]])
            print('cima',estads_possiveis)
            x = 0
            for j in range(len(estads_possiveis)):
                #verifica se ultrapassa os limites, estados bloqueados.
                if estads_possiveis[j][0] < 0 or estads_possiveis[j][0] >= num_linhas or estads_possiveis[j][1] < 0 or estads_possiveis[j][1] >= num_cols or (estads_possiveis[j][0] == 1 and estads_possiveis[j][1] == 1) :
                    if j == 0:
                        x = 0.8*estados[s[0]][s[1]]
                    else:
                        x += 0.1*estados[s[0]][s[1]]
                else:
                    if j == 0:
                        x = 0.8*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
                    else:
                        x += 0.1*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
            x = u+x
            #verifica se é um estado terminal ou bloqueado
            if (s[0]==1  and s[1] == 1):  
                pass
                #print('bloqueado',s)
            elif (s[0] == 3 and s[1] == 1):
                pass
                #print('terminais negativo',s)
            elif (s[0] == 3 and s[1] == 2):
                pass
                #print('terminais positivo',s)
            else:
                 aux.append(x)
        elif cont == 3:#baixo
            estads_possiveis.append([i[0],i[1]])
            estads_possiveis.append([S[0][0],S[0][1]])
            estads_possiveis.append([S[1][0],S[1][1]])
            print('baixo',estads_possiveis)
            x = 0
            for j in range(len(estads_possiveis)):
                #verifica se ultrapassa os limites, estados bloqueados.
                if estads_possiveis[j][0] < 0 or estads_possiveis[j][0] >= num_linhas or estads_possiveis[j][1] < 0 or estads_possiveis[j][1] >= num_cols or (estads_possiveis[j][0] == 1 and estads_possiveis[j][1] == 1) :
                    if j == 0:
                        x = 0.8*estados[s[0]][s[1]]
                    else:
                        x += 0.1*estados[s[0]][s[1]]
                else:
                    if j == 0:
                        x = 0.8*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
                    else:
                        x += 0.1*estados[estads_possiveis[j][0]][estads_possiveis[j][1]]
            x = u+x
            #verifica se é um estado terminal ou bloqueado
            if (s[0]==1  and s[1] == 1):
                pass
                #print('bloqueado',s)
            elif (s[0] == 3 and s[1] == 1):
                pass
                #print('terminais negativo',s)
            elif (s[0] == 3 and s[1] == 2):
                pass
                #print('terminais positivo',s)
            else:
                 aux.append(x)
        cont+=1
    if (s[0]==1  and s[1] == 1):  
        #print('bloqueado',s)
        pass
    elif (s[0] == 3 and s[1] == 1):
        #print('terminais negativo',s)
        pass
    elif (s[0] == 3 and s[1] == 2):
        #print('terminais positivo',s)
        pass
    else:
        estados[s[0]][s[1]] = max(aux)
    #print(aux)
    #print(estados)
    #estados[s[0]][s[1]] = aux
#linha negativa
#coluna negativa
#linha maior que 4
#coluna maior que 3

estados = np.zeros((4,3),float)
#estados = [estados]*4
estados[3][1] = -1
estados[3][2] = 1
#estados[1][1] = -2
for x in range(200):
    for i in range(4):
        for j in range(3):
            U([i,j],estados,4,3)
    print(estados)
    input('>')
    print('iterção',x,' \n\n')