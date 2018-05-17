#!/usr/bin/env python3

inFile = open("part-r-00000","r")
nFile = open("nodes.txt", "w")
eFile = open("edges.txt", "w")
for line in inFile:
	#line = line.lstrip()
	line = line.replace("\t0",";0")
	line = line.replace("\t1",";1")
	line = line.replace("\t2",";2")
	line = line.replace("\t3",";3")
	line = line.replace("\t4",";4")
	line = line.replace("\t5",";5")
	line = line.replace("\t6",";6")
	line = line.replace("\t7",";7")
	line = line.replace("\t8",";8")
	line = line.replace("\t9",";9")
	if(":" in line):
		line = line.replace(":",";")
		eFile.write(line)

	else:
		nFile.write(line)
