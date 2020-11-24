# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:08:24 2020

@author: shrey
"""

import networkx as nx 
l=int(input("Enter no. of nodes"))
G=nx.Graph()#creating a graph
H=nx.path_graph(l) #creating a graph having l no. of nodes

nodes=input("enter nodes separated by comma").split(',')
for i in range(l):
    G.add_node(nodes[i])#adding the nodes in G and H
    H.add_node(nodes[i])
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present")
for i in range(no_of_edges):
    b=input()#consists of the list of nodes where an edge is present between them
    #so, if, there exists an edge between 1 and 3, then b=[1,3], where b[0]=1,b[1]=3
    G.add_edge(b[0],b[1])
    H.add_edge(b[0],b[1])
    
print("the diameter of the graph is ", nx.diameter(G))

print("enter the pair of nodes you want to find the distance between")
a=input("enter first node  ")
b=input("enter second node  ")


print("the shortest distance between",a,"and",b, "is",nx.shortest_path_length(H, source=a, target=b ))

