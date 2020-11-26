# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:55:54 2020

@author: shrey
"""
#Shreya Srivastava
#19BCP123
import numpy as np
#numpy library will help us create arrays

row=int(input("enter no. of rows"))#since it is a square matrix
#so, only no. of rows is needed

A=np.zeros((row,row))#creating a zero matrix of the size (no. of rows) x (no. of rows)
B=np.zeros((row,row))
C=np.zeros((row,row))
for i in range(row):
    for j in range(row):
        print("enter 1 if there is a direct edge present between",i,"row and",j,"column else enter 0")
     
        b=int(input())#taking the input from the user
        A[i][j]=b #and assigning the value of the element present at 
        #i'th row and j'th column in A matrix
B=A
C=A
print("length 1\n",B)
for i in range(row-1):
    B=B.dot(A)#multiplying two matrices and storing the result in variable B
    #since B was A earlier, so it becomes A*A=A^2 and this A^2 is stored in B
    #so for the next multiplication, B is A^2, so A^2 * A= A^3 and this is stored in B, and so on..
    print("LENGTH",i+2,B,"\n")
    C=C+B #adding two matrices and storing it in C
    #therefore, C will be composed of A+A^2+A^3+...

path_matrix=np.zeros((row,row))#so, initially all the elements in path matrix are zeros
for i in range(row):
    for j in range(row):
        if C[i][j]!=0:
            path_matrix[i][j]=1 #changing the element to 1, if the corresponding element 
            #in C is non-zero

print(path_matrix)