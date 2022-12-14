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
            all_rocks.append(rock) #rocks in no order
    y_coord = []
    for elements in all_rocks:
        y_coord.append(elements[1])
    y_max = max(y_coord)
    rocky = []
    for i in range(y_max+2):
        rocky.append([])
    for rockz in all_rocks:
        rocky[rockz[1]].append(rockz) #list rocks by y-coord
    return all_rocks, rocky

def sand_move(sand_pos,all_rocks, floor, part):
    new_pos = [[sand_pos[0],sand_pos[1]+1],[sand_pos[0]-1,sand_pos[1]+1],[sand_pos[0]+1,sand_pos[1]+1]]
    if sand_pos[1] == floor-1:
        return sand_pos
    counter = 0 
    for i in range(len(new_pos)):
        if new_pos[i] not in all_rocks[new_pos[i][1]]:
            return sand_move(new_pos[i],all_rocks, floor, part)
        else:
            counter += 1
            if counter == 3:
                return sand_pos

seconds = time.time()
part = 1
rock_coord = readfile()
rock_map, other_rock_map = create_cord_all_rocks(rock_coord)
y_lim = len(other_rock_map) - 2
a = True
sand_list = []
sand = [500,0]

if part == 1:
    condition = 'sand[1] < y_lim'
elif part == 2:
    condition = 'sand_move(sand,other_rock_map, y_lim  + 2, part) != [500,0]'
    
while eval(condition):
    sand = [500,0]
    sand = sand_move(sand,other_rock_map, y_lim  + 2, part)
    sand_list.append(sand)
    other_rock_map[sand[1]].append(sand)
    
if part == 1:
    print(len(sand_list)-1)
elif part == 2:
    print(len(sand_list)) 
print(time.time()-seconds)
