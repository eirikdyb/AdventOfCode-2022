ranges_1 = []
ranges_2 = []
with open("input.txt",'r') as content:
        for line in content:
            ranges_1.extend(line.split(",")[0].split("-"))
            ranges_2.extend(line.split(",")[1].strip().split("-"))

ranges_1 = [int(x) for x in ranges_1]
ranges_2 = [int(x) for x in ranges_2]

def check_for_subset(intervalls_1, intervalls_2):
    overlap = 0
    for i in range(0, len(ranges_1) - 1, 2):
        if intervalls_1[i+1] >= intervalls_2[i+1] and intervalls_1[i] <= intervalls_2[i]:
            overlap += 1
        elif intervalls_2[i+1] >= intervalls_1[i+1] and intervalls_2[i] <= intervalls_1[i]:
            overlap += 1
        
    return overlap

def check_for_cmn_elmnt(intervalls_1, intervalls_2):
    overlap = 0
    for i in range(0, len(ranges_1) - 1, 2):
        if intervalls_2[i] <= intervalls_1[i] <= intervalls_2[i+1] or intervalls_2[i] <= intervalls_1[i+1] <= intervalls_2[i+1]:
            overlap += 1
        elif intervalls_1[i] <= intervalls_2[i] <= intervalls_1[i+1] or intervalls_1[i] <= intervalls_2[i+1] <= intervalls_1[i+1]:
            overlap += 1
        
    return overlap
    
print(check_for_subset(ranges_1, ranges_2))
print(check_for_cmn_elmnt(ranges_1, ranges_2))

    
