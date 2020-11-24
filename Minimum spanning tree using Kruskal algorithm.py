# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 09:53:11 2020

@author: shrey
"""

import networkx as nx


G=nx.Graph()#creating a graph G
l=int(input("Enter no. of nodes"))
nodes=input("enter nodes").split(',')
for i in range(l):
    G.add_node(nodes[i])
no_of_edges=int(input("enter no. of edges"))

print("enter the pair of nodes, where the edge is present and the edge-weight separated by comma ")
print("\n")
print("Enter the edges in ascending order of their weights")

#Therefore, the user will enter the edges in ascending order of their weights, edges having the
#least weights will be entered first and then the edges with greater weights will be entered by
#the user

edge_with_weight=[] #creating an empty list
for i in range(no_of_edges):
    
    b=input().split(',')#consists a list of edges and weights separated by comma
    #if there is an edge present between 1 and 2 of weight 10, b=[1,2,10]
    #where b[0]=1, b[1]=2, b[2]=10
    
    G.add_edge(b[0],b[1], weight=int(b[2]))
    edge_with_weight.append((b[0],b[1],int(b[2])))#if we consider the example above, one of
    #the elements of edge_with_weight list can be (1,2,10), which is a tuple

print("The list of edges with their weights:-")   
print(edge_with_weight)

H=nx.Graph()
H.add_nodes_from(G) #creating a new graph that already has the nodes 
#from the graph entered by the user

for i in range(len(edge_with_weight)):
    (node1, node2, weightt)=edge_with_weight[i]#we are extracting data from the 
    #edge_with_weight list elements one by one and storing it in LHS
    #so, if there was an element (1,2,10) in the list then, node1=1, node2=2, weightt=10
    
    H.add_edge(node1, node2, weight= weightt)
    #Now we check if any cycle was created after adding this edge
    
    if nx.cycle_basis(H)!=[]:
        #checking if the list of cycles is empty or not
        # and removing the edge that was recently added if the list is not empty
        H.remove_edge(node1,node2)

#After creating graph H(which is the minimum spanning tree), all we have to do
# is add the weights of edges
b=list(H.edges(data='weight'))#we get a list of the edges in H with weights
min_weight=0#declaring a variable with initial value 0
for i in range(len(b)):
    (src,dest,weightt)=b[i]#since b is a list of tuples, we extract data from tuple first
    #and then add the weight below
    min_weight=min_weight+weightt
print("Minimum weight of spanning tree is",min_weight)
