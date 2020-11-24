# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:57:37 2020

@author: shrey
"""

import networkx as nx 

G=nx.Graph()#creating a graph G
l=int(input("Enter no. of nodes"))
nodes=input("enter nodes").split(',')#like 1,2,3.. or a,b,c..
for i in range(l):
    G.add_node(nodes[i])#adding the node in graph G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present")
for i in range(no_of_edges):
    b=input()#consists of a list of nodes where an edge is present
    #if,say, there exists an edge between 1 and 2, then b=[1,2], where b[0]=1, b[1]=2
    G.add_edge(b[0],b[1])
even=0
odd=0
for i in range(l):
    if G.degree(nodes[i])%2==0:#checking whether the degree of i'th node is even or odd
        even=even+1#if it is even then increment the variable by 1
    else:
        odd=odd+1#same with odd
if even==len(nodes):#if the value of variable even is equal to the total no. of nodes
    print('eulerian cycle exits')
elif odd==2:
    print('eulerian path exits')
else:
    print("neither eulerian cycle nor eulerian path exists")