#!/usr/bin/Rscript

rm(list=ls())

library(network)
library(sna)
library(ggplot2)
library(GGally)
library(dplyr)
file = read.csv("test.txt")
#arrange(file, "name1")
namelist = c(as.character(file[["name1"]]),as.character(file[["name2"]]))

#j = data.frame(strsplit(namelist,"-")[1,])
print(namelist)
namelist = unique(namelist)
print(namelist)
emailCounts = c()
#f = filter(file,name1=="alex" | name2=="alex")
#ffff = as.numeric(f[["emails"]])
for(i in namelist){
  j = sum(as.numeric(filter(file,name1==i | name2 == i)[["emails"]]))
  emailCounts = c(emailCounts, j)
}
print(emailCounts)
#Right now the program will make a list "namelist" of all the names in the file and a list "emailCounts"
#of all the total emails for each person in namelist (in the same order)
#Need to put these values in a table, possibly also make a column for adjacency list, or make a 
#matrix, but it would have to eventually be 150x150 (0=no emails, >0 = edge with weight #emails)
#can also make a separate list to hold relationships 


#print(j)
#for(i in file$relationship){
#  j = strsplit(i, "-")[[1]]
#  
#  if( !(j[1] %in% namelist)){
#    
#    namelist = c(namelist, j[1])
#  }
#  if( !(j[2] %in% namelist)){
#    namelist = c(namelist, j[2])
#  }
#}
#print(namelist)
#random graph
net = rgraph(150, mode = "graph", tprob = 0.1)
net = network(net, directed = FALSE)

# vertex names
network.vertex.names(net) = letters[1:10]
ggnet2(net, mode = "circle", size = 2, color = "black")
ggnet2(net, mode = "fruchtermanreingold", size = 2, color = "black", layout.par = list(cell.jitter = 0.90))

