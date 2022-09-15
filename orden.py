
f = open("j.txt", "r")

for line in f:
    line = line.split(" ")
    NS = line[0:29]
    print(NS)