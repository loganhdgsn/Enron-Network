#!/usr/bin/env python3

import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx

try:
    import matplotlib.pyplot as plt
except:
    raise


file = open("part-r-00000","r")
pairDict = dict(line.split("\t") for line in file)

#singleDict = {}
relateDict = {}
print(pairDict)
print("**************************************************")

for i in pairDict.items():
    pair,num = i
    num=int(num)
    name1, name2 = pair.split("-")
    print(name1+" "+name2)
    #relateDict[name1] = [name2]
    #relateDict[name2] = [name1]
#    if(name1 in singleDict):
#        singleDict[name1] += num
#    else:
#        singleDict[name1] = num
#    if(name2 in singleDict):
#        singleDict[name2]+= num
#    else:
#        singleDict[name2] = num

    if(name1 in relateDict):
    	if(name2 not in relateDict[name1]):
    		relateDict[name1].append(name2)
    else:
    	relateDict[name1] = [name2]
    if(name2 in relateDict):
    	if(name1 not in relateDict[name2]):
    		relateDict[name2].append(name1)
    else:
    	relateDict[name2] = [name1]


print("**************************************************")
print(relateDict)
print("**************************************************")
print(singleDict)

#G = nx.Graph()
G = nx.Graph(relateDict)
#for name in relateDict.keys():
#	G.add_edge(name,relateDict[name],weight=pairDict[name+"-"+relateDict[name]])
#weight=len(relateDict[name])??

#print(nx.get_node_attributes(G,'pos'))



#elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
#esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=2000)

#
nx.draw_networkx_labels(G,pos,labels=singleDict)
# edges
#nx.draw_networkx_edges(G,pos,edgelist=elarge,
#                    width=6)
#nx.draw_networkx_edges(G,pos,edgelist=esmall,
#                   width=6,alpha=0.5,edge_color='b',style='dashed')

nx.draw_networkx_edges(G,pos,width=3,alpha=0.5,edge_color='b')



# labels
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display
