import time
def readfile():
    data = []
    new_data = []
    with open("input.txt",'r') as content:
        for line in content:
            data.append(line.split())
    for i in range(len(data)):
        coord = []
        for j in range(len(data[i])):
            if j % 2 == 0:
                coord.append([int(data[i][j].split(",")[0]),int(data[i][j].split(",")[1])])
        new_data.append(coord)
    return new_data

def create_cord_all_rocks(rock_map):
    diff = 0
    for i in range(len(rock_map)):
        new_rocks = []
        for j in range(len(rock_map[i])-1):
            if rock_map[i][j][0] == rock_map[i][j+1][0]:
                diff = rock_map[i][j+1][1] - rock_map[i][j][1]
                for k in range(abs(diff)-1):
                    new_rocks.append([rock_map[i][j][0],rock_map[i][j][1]+(k+1)*int(diff/abs(diff))])
            if rock_map[i][j][1] == rock_map[i][j+1][1]:
                diff = rock_map[i][j+1][0] - rock_map[i][j][0]
                for k in range(abs(diff)-1):
                    new_rocks.append([rock_map[i][j][0]+(k+1)*int(diff/abs(diff)),rock_map[i][j][1]])
    
        for rocks in new_rocks:
            rock_map[i].append(rocks)
            
    all_rocks = []
    for line in rock_map:
        for rock in line:
            all_rocks.append(rock)
    y_coord = []
    for elements in all_rocks:
        y_coord.append(elements[1])
    y_max = max(y_coord)
    rocky = []
    for i in range(y_max+2):
        rocky.append([])
    for rockz in all_rocks:
        rocky[rockz[1]].append(rockz)
    
    return all_rocks, rocky

def sand_move(sand_pos,all_rocks, floor, part):
    new_pos = [[sand_pos[0],sand_pos[1]+1],[sand_pos[0]-1,sand_pos[1]+1],[sand_pos[0]+1,sand_pos[1]+1]]
    
    counter = 0
    if part == 2:
        if sand_pos[1] == floor - 1:
            return sand_pos, False
        
    for i in range(len(new_pos)):
        if new_pos[i] not in all_rocks[new_pos[i][1]]:
            pos = new_pos[i]
            return pos, True
        else:
            counter += 1
            if counter == 3:
                return sand_pos, False

seconds = time.time()
part = 2
rock_coord = readfile()
rock_map, other_rock_map = create_cord_all_rocks(rock_coord)
y_coord = []
for elements in rock_map:
    y_coord.append(elements[1])
y_lim = max(y_coord)
sand = [500,0]
a = True
sand_list = []
while a:
    sand = [500,0]
    counter = 0
    run = True
    while run:
        sand, run = sand_move(sand,other_rock_map, y_lim  + 2, part)
        if part == 2:
            if sand == [500,0]:
                a = False
                break
        elif part == 1:
            if sand[1] > y_lim:
                a = False
                break
    sand_list.append(sand)
    other_rock_map[sand[1]].append(sand)
    
if part == 1:
    print(len(sand_list)-1)
elif part == 2:
    print(len(sand_list)) 
print(time.time()-seconds)
