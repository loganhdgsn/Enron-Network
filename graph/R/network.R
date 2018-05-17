#!/usr/bin/Rscript

rm(list=ls())
library(network)
library(sna)
library(ggplot2)
library(GGally)
library(dplyr)
library(igraph)
nodes <- read.csv2("nodes.txt", header=FALSE,quote = "", row.names = NULL, stringsAsFactors = FALSE)
#nodes <- unique(nodes)
#nodes <- nodes[!(duplicated(nodes) | duplicated(nodes, fromLast = FALSE)), ]
nodes <- nodes[!duplicated(nodes[,"V1"]),]
nodes <- arrange(nodes, as.numeric(V2))
tail(nodes,n=10)


edges <- read.csv2("edges.txt",header=FALSE,quote = "", row.names = NULL, stringsAsFactors = FALSE)
#edges <- unique(edges)
#edges <- edges[!(duplicated(edges) | duplicated(edges, fromLast = FALSE)), ]

#nodes <- unique(c(edges[,1], edges[,2])) #Define v from both columns in data
#nodes <- na.omit(nodes)
#edges<- na.omit(edges)
edges <- edges[!is.na(as.numeric(as.character(edges$V3))),]
edges <- arrange(edges, as.numeric(V3))
edges = tail(edges, n=100)

g <- graph_from_data_frame(d=edges, directed=FALSE)
E(g)$weight <- edges$V3
#par(mar=c(0,0,0,0))
l <- layout_in_circle(g)
plot(g, layout=l, vertex.size = 10, edge.arrow.size=1, vertex.color = rgb(0,0,1),vertex.label.color=adjustcolor("black",0.3), vertex.label.cex=1 )

l <- layout_on_sphere(g)
plot(g, layout=l, vertex.size = 10, edge.arrow.size=1, vertex.color = rgb(0,0,1),vertex.label.color=adjustcolor("black",0.3), vertex.label.cex=1 )

