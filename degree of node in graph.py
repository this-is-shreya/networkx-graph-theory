# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:58:25 2020

@author: shrey
"""

import networkx as nx 

G=nx.Graph()#creating a graph G
l=int(input("Enter no. of nodes"))
nodes=input("enter the nodes separated by comma").split(',')
for i in range(l):
    G.add_node(nodes[i])#adding the node in G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present,separated by comma")
for i in range(no_of_edges):
    b=input().split(',')#consists of list of nodes where an edge is present, so, if
    #there is an edge between A and B, then b=[A,B], and b[0]=A, b[1]=B
    #the next time the loop runs again, b becomes empty list
    G.add_edge(b[0],b[1])
    
for i in range(l):
    print("The degree of",nodes[i],"is",G.degree(nodes[i]))# tells the degree of the i'th node