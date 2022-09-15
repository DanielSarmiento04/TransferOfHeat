
# Open TablasTemp.txt
values = dict()
values["placa"] = [], []
values["cilindro"] = [], []
values["esfera"] = [], []
bis =[]
f = open("TablasTemp.txt", "r")
for line in f:
    if len(line) > 1 and line[0] != "B":
        bi, l1, c1, l2, c2, l3, c3 = line.split('\t')
        bis.append(float(bi))
        values["placa"][0].append(float(l1))
        values["placa"][1].append(float(c1))
        values["cilindro"][0].append(float(l2))
        values["cilindro"][1].append(float(c2))
        values["esfera"][0].append(float(l3))
        values["esfera"][1].append(float(c3))


def getCAndlanda(bi: float,tipo:str)->tuple:

    # Find the index of the bi value in the bis list
    # This is the index of the corresponding c value
    # if the value is not in the list return the amount of upper and downer values
    try:
        index = bis.index(bi)
        return values[tipo][0][index], values[tipo][1][index]
    except ValueError:
        for i in range(len(bis)):
            if bis[i] > bi:
                num = bis[i] - bis[i-1]
                den1 = values[tipo][1][i] - values[tipo][1][i-1]
                den2 = values[tipo][0][i] - values[tipo][0][i-1]
                delta = ((bi - bis[i-1])*den1) / num
                delta2 = ((bi - bis[i-1])*den2) / num
                c = delta+values[tipo][1][i-1]
                l = delta2+values[tipo][0][i-1]
                return l, c



print(getCAndlanda(70,'placa'))
