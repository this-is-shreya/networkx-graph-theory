# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:48:30 2020

@author: shrey
"""


import networkx as nx 

G=nx.Graph()#creating an undirected graph G

no_of_nodes=input("enter no. of nodes")

nodes=input("enter nodes").split(',')#like 1,2,3.. or a,b,c..
for i in range(len(no_of_nodes)):
    G.add_node(nodes[i])#adding the node in G
no_of_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present")
for i in range(no_of_edges):
    b=input()#consists of list of nodes where an edge is present, so, if
    #there is an edge between A and B, then b=[A,B], and b[0]=A, b[1]=B
    G.add_edge(b[0],b[1])

print("Second Graph")

H=nx.Graph()

no_of_second_nodes=input("enter no. of nodes")

nodes_second=input("enter nodes").split(',')
for i in range(len(no_of_second_nodes)):
    H.add_node(nodes_second[i])
    
no_of_second_edges=int(input("enter no. of edges"))
print("enter the pair of nodes, where the edge is present")
for i in range(no_of_second_edges):
    b=input()
    H.add_edge(b[0],b[1])

print("Now, to compare")
count=0
l=list(G.nodes)#consists of list of nodes of graph G
m=list(H.nodes)#same with H


if(len(l)==len(m)):#checking whether the length of the lists of nodes of G and H are same or not
    
    print("no. of nodes is same")
    count=count+1
else:
   
    print("different number of nodes")
if(G.number_of_edges()==H.number_of_edges()):
    print("no. of edges is same")
    count=count+1
else:
    print("no. of edges are different")
    
if(G.number_of_selfloops()==H.number_of_selfloops()):
    print("no. of self-loops is same")
    count=count+1
else:
    
    print("different no. of self-loops")

temp=0

for i in range(len(l)):
    
    if(G.degree[l[i]])!=(H.degree[m[i]]):#comparing the degree of the corresponding nodes in G and H
        print("degree of", l[i], " in first graph is not equal to that of ", m[i], " in second graph")
        print("degree of",l[i], " in first graph is", G.degree[l[i]])
        print("degree of",m[i], "in second graph is", H.degree[m[i]])
        temp=temp-1

if(temp==0 and count==3):
    print("the graphs are isomorphic")
else:
    print("the graphs are not isomorphic")

#drawing the graphs
nx.draw(H, node_color='green',node_size=1000,with_labels=True, font_weight='bold')
print()

nx.draw(G, node_size=1000,with_labels=True, font_weight='bold')

