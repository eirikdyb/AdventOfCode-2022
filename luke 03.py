rucksacks = []
with open("input3.txt",'r') as content:
        for line in content:
            rucksacks.append(line.split(None, 1)[0]) 
 
 
 
def common_elements(rucksacks):
    common = []
    for line in rucksacks:
        count = 0
        comp_1 = []
        comp_2 = []
        for letters in line:
            if count < len(line)/2:
                comp_1.append(letters)
            else:
                comp_2.append(letters)
            count += 1
        common.append(list(set(comp_1).intersection(comp_2))[0])
    return common
    
 
def pts(list):
    pts = 0
    for letters in list:
        if letters.isupper():
            pts += ord(letters) - 38
        else:
            pts += ord(letters) - 96
    return pts
 
 
def common_3_rucksacks(rucksacks):
    badge_1 = []
    badge_2 = []
    for i in range(0,len(rucksacks),3):
        badge_1 = list(set(rucksacks[i]).intersection(rucksacks[i+1]))
        badge_2.append(list(set(rucksacks[(i+2)]).intersection(badge_1))[0])
        badge_1 = []
    return badge_2
 
common = common_elements(rucksacks)
common_3 = common_3_rucksacks(rucksacks)
print(pts(common))
print(pts(common_3))
