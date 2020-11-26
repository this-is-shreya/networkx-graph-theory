# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:18:32 2020

@author: shrey
"""
#Shreya Srivastava
#19BCP123
import networkx as nx
import numpy as np


nodes=input("enter the nodes/vertices of the graph separated by comma").split(',')
G=nx.DiGraph()
for i in range(len(nodes)):
    G.add_node(nodes[i])#adding the node in G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present, with the weight,all separated by comma")
for i in range(no_of_edges):
    b=input().split(',')#consists of list of nodes where an edge is present, so, if
    #there is an edge between A and B, then b=[A,B,4], and b[0]=A, b[1]=B, b[2]=4(the edge weight)
    G.add_edge(b[0],b[1], weight=int(b[2]))
    
a=nx.floyd_warshall_numpy(G)#returns a shortest path matrix using warshall's algorithm
#but this matrix doesn't provide shortest path where the source and the destination node is same

#if there is a cycle between 1,2,3; then, we can traverse from 1 to 1 or 2 to2 or 3 to 3 via this
#cycle, but in the matrix the value of 1st row-1st col =0; similarly for 2nd and 3rd row and cols

C=np.asarray(a)#converting it into an array

m=[]
l=list(nx.simple_cycles(G))#returns a list of nodes forming a cycle
f=0
for i in range(len(nodes)):
    
    for r in range(len(l)):
       
        if nodes[i] in l[r]:#if the node is in the list containing cycles
            k=l[r]
            
            for s in range(len(k)):#say, k=[1,2,3], so, len(k)=3, but 2 is the last index
                #that is, k[3] doesn't exist
                if (s+1)!=len(k):#thus, the if conditions check whether index is in range
                           
                    f=f+G.get_edge_data(k[s],k[s+1])['weight']#adding the weight as we proceed
                    #from one edge to another in a cycle
                    
                if (s+1)==len(k):
                   
                    f=f+G.get_edge_data(k[s],k[0])['weight']
            m.append(f)#appending the value of the shortest path obtained in the list
            f=0
    if m!=[]:
        C[i][i]=min(m)#assigning the minimum value in the list
        m=[]
    
print("shortest path matrix \n", C)
                    
                    
                    
                    