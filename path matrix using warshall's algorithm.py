# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:20:15 2020

@author: shrey
"""
#Shreya Srivastava
#19BCP123
import numpy as np
#numpy library will help us create arrays/matrices
import networkx as nx



nodes=input("enter the nodes/vertices of the graph separated by comma").split(',')
G=nx.DiGraph()
for i in range(len(nodes)):
    G.add_node(nodes[i])#adding the node in G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present")
for i in range(no_of_edges):
    b=input().split(',')#consists of list of nodes where an edge is present, so, if
    #there is an edge between A and B, then b=[A,B], and b[0]=A, b[1]=B
    G.add_edge(b[0],b[1])

A=np.zeros((len(nodes),len(nodes)))
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if (G.has_successor(nodes[i],nodes[j])):
            A[i][j]=1
        else:
            A[i][j]=0

print("P0 is \n", A)


B=A

l=list(nx.simple_cycles(G))#list of nodes forming a cycle

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if nodes[i]!=nodes[j]:#since nx.all_simple_paths() function doesn't work when
            #source node and destination node is same, we check in the else statement if the
            #node is a part of cycle
            
            if list(nx.all_simple_paths(G,nodes[i],nodes[j]))!=[]:#checks whether there
                #exists a path between 2 nodes
            
                B[i][j]=1
            
                
                
        else:
            for r in range(len(l)):
                if nodes[i] in l[r]:#checks whether the nodes are a part of cycle
                    B[i][j]=1

print("THIS IS P",len(nodes),"\n",B)

print("the graph looks like this \n")
nx.draw(G,  node_size=1000,with_labels=True)    
        
            



