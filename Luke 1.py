elf = 0
elfkcal = []
 
with open("inputtest.txt",'r') as namelist:
        for line in namelist:
            if line.strip():
                elf += int(line.split(None, 1)[0])
            else:
                elfkcal.append(elf)
                elf = 0
elfkcal.append(elf)     #Adding the last elf
 
elfkcal.sort(reverse=True)
 
kcalsum = 0
for i in range(3):
    kcalsum += elfkcal[i]
print(elfkcal[0])
print(kcalsum)
