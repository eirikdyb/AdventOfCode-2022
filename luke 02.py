elf = []
strat = []
 
with open("input.txt",'r') as namelist:
        for line in namelist:
            elf.append(line.split(None, 1)[0])
            strat.append(line.split(None, 2)[1])
 
#A stein, B papir, C saks
#X stein, Y papir, Z saks
#X er tap, Y er draw og Z er vinn
#Poeng 1, 2, 3
#Tap = 0, uavjort = 3 og seier = 6
def result(A,B):
    res = 0
    if B == 'X' :
        res = 1
        if A == 'A':
            res += 3
        elif A == 'B':
            res += 0
        elif A == 'C':
            res += 6
        
    if B == 'Y' :
        res = 2
        if A == 'A':
            res += 6
        elif A == 'B':
            res += 3
        elif A == 'C':
            res += 0
            
    if B == 'Z' :
        res = 3
        if A == 'A':
            res += 0
        elif A == 'B':
            res += 6
        elif A == 'C':
            res += 3
            
    return res
 
def strat_list(liste1, liste2):
    new_strat = []
    for i in range(len(liste1)):
        if liste2[i] == 'X': #Loss
            if liste1[i] == 'A':
                new_strat.append("Z")
            elif liste1[i] == 'B':
                new_strat.append("X")
            elif liste1[i] == 'C':
                new_strat.append("Y")
 
        elif liste2[i] == 'Y': #draw
            if liste1[i] == 'A':
                new_strat.append("X")
            elif liste1[i] == 'B':
                new_strat.append("Y")
            elif liste1[i] == 'C':
                new_strat.append("Z")
                
        elif liste2[i] == 'Z': #Win
            if liste1[i] == 'A':
                new_strat.append("Y")
            elif liste1[i] == 'B':
                new_strat.append("Z")
            elif liste1[i] == 'C':
                new_strat.append("X")
    return new_strat
            
        
pts = 0
new_strat = strat_list(elf, strat)
 
for i in range(len(elf)):
    pts += result(elf[i],new_strat[i])
print(pts)
