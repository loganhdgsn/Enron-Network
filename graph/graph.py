#!/usr/bin/env python3

file = open("test.txt","r")

pairSet = dict(line.split() for line in file)
singleSet = {}

print(pairSet)
print("**************************************************")

for i in pairSet.items():
    pair,num = i
    num=int(num)
    name1, name2 = pair.split("-")
    print(name1+" "+name2)
    if(name1 in singleSet):
        singleSet[name1] += num
    else:
        singleSet[name1] = num
    if(name2 in singleSet):
        singleSet[name2]+= num
    else:
        singleSet[name2] = num

print("************************************************")
print(singleSet)
    
