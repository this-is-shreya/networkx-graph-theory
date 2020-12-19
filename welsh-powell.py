# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:56:40 2020

@author: shrey
"""


import networkx as nx  

nodes=input("enter the nodes/vertices of the graph separated by comma").split(',')
G=nx.Graph()

for i in range(len(nodes)):
    G.add_node(nodes[i])#adding the node in G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present, with the weight,all separated by comma")

for i in range(no_of_edges):
    b=input().split(',')#consists of list of nodes where an edge is present, so, if
    #there is an edge between A and B, then b=[A,B], and b[0]=A, b[1]=B
    G.add_edge(b[0],b[1])

d=nx.greedy_color(G,strategy="random_sequential")#assigns colours to nodes
#such that no two adjacent nodes have the same colour
# say there are 3 nodes, A,B,C , in a cycle, then d={A:0,B:1,C:2}[this form is known as dictionary]
#where 0,1,2 are the colours assigned

l=list(d.values())#we will extract those values from the dictionary and convert it into a list
print("chromatic number is", max(l)+1)#since the colour starts from zero, we have to add 1

nx.draw(G, node_size=1000, with_labels=True)
