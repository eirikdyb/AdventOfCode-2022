import matplotlib.pyplot as plt
def readfile():
    data = []
    sides = {}
    max_x = 0
    max_y = 0
    max_z = 0
    min_x = 10000
    min_y = 10000
    min_z = 10000
    with open("input_vetle.txt",'r') as content:
        for lines in content:
            data.append([int(x) for x in lines.strip().split(",")])
            if  int(lines.strip().split(",")[0]) > max_x:
                max_x =  int(lines.strip().split(",")[0])
            if  int(lines.strip().split(",")[1]) > max_y:
                max_y =  int(lines.strip().split(",")[1])
            if  int(lines.strip().split(",")[2]) > max_z:
                max_z =  int(lines.strip().split(",")[2])
            if  int(lines.strip().split(",")[0]) < min_x:
                min_x =  int(lines.strip().split(",")[0])
            if  int(lines.strip().split(",")[1]) < min_y:
                min_y =  int(lines.strip().split(",")[1])
            if  int(lines.strip().split(",")[2]) < min_z:
                min_z =  int(lines.strip().split(",")[2])
    for i in range(len(data)):
        sides[i] = 6
    return data, sides, [max_x,max_y,max_z], [min_x,min_y,min_z]

def side_check(cube_1,cube_2,side_dict,i,j):
    if (cube_1[0] == cube_2[0] - 1 or cube_1[0] == cube_2[0] + 1) and cube_1[1] == cube_2[1] and cube_1[2] == cube_2[2]:
        side_dict[i] -= 1
        side_dict[j] -= 1
    elif (cube_1[1] == cube_2[1] - 1 or cube_1[1] == cube_2[1] + 1) and cube_1[0] == cube_2[0] and cube_1[2] == cube_2[2]:
        side_dict[i] -= 1
        side_dict[j] -= 1
    elif (cube_1[2] == cube_2[2] - 1 or cube_1[2] == cube_2[2] + 1) and cube_1[0] == cube_2[0] and cube_1[1] == cube_2[1]:
        side_dict[i] -= 1
        side_dict[j] -= 1
    return side_dict
    

def find_neighbours(air_cube):
    neighbour = []
    neighbour.append([air_cube[0]+1,air_cube[1],air_cube[2]])
    neighbour.append([air_cube[0]-1,air_cube[1],air_cube[2]])
    neighbour.append([air_cube[0],air_cube[1]+1,air_cube[2]])
    neighbour.append([air_cube[0],air_cube[1]-1,air_cube[2]])
    neighbour.append([air_cube[0],air_cube[1],air_cube[2]+1])
    neighbour.append([air_cube[0],air_cube[1],air_cube[2]-1])
    return neighbour

def find_2d_neighbours(air_cube):
    neighbour = []
    neighbour.append([air_cube[0]+1,air_cube[1],air_cube[2]])
    neighbour.append([air_cube[0]-1,air_cube[1],air_cube[2]])
    neighbour.append([air_cube[0],air_cube[1]+1,air_cube[2]])
    neighbour.append([air_cube[0],air_cube[1]-1,air_cube[2]])

    return neighbour

def level_cubes(cubes):
    level_dict = {}
    for cube in cubes:
        if cube[2] not in level_dict:
            level_dict[cube[2]] = [[cube[0],cube[1]]]
        else:
            level_dict[cube[2]].append([cube[0],cube[1]])

    return level_dict


cubes, sides, max_values, min_values = readfile()

#Part one
for i in range(len(cubes)): #Check which cubes share sides with other cubes
    for j in range(i+1,len(cubes)):
        sides = side_check(cubes[i],cubes[j],sides,i,j)
sum_of_sides = 0
for keys in sides:
    sum_of_sides += sides[keys]
print(f"Part 1: {sum_of_sides}")

#Part two

z_cubes = level_cubes(cubes)
air_coords= []
for i in range(min_values[2],max_values[2]+1):
    cubes_to_check = z_cubes[i]
    non_cubes = []
    for y in range(-2,max_values[1]+2):
        for x in range(-2,max_values[0]+2):
            if [x,y] in cubes_to_check:
                break
            if [x,y] not in non_cubes:
                non_cubes.append([x,y])
    for y in range(-2,max_values[1]+2):
        for x in range(max_values[0]+2,-2,-1):
            if [x,y] in cubes_to_check:
                break
            if [x,y] not in non_cubes:
                non_cubes.append([x,y]) 
    for x in range(-2,max_values[0]+2):
        for y in range(max_values[1]+2,-2,-1):
            if [x,y] in cubes_to_check:
                break
            if [x,y] not in non_cubes:
                non_cubes.append([x,y])
    for x in range(-2,max_values[0]+2):
        for y in range(-2,max_values[1]+2):
            if [x,y] in cubes_to_check:
                break
            if [x,y] not in non_cubes:
                non_cubes.append([x,y])

    for x in range(-2,max_values[0]+2):
        for y in range(-2,max_values[1]+2):
            if [x,y] not in non_cubes and [x,y] not in cubes_to_check and [x,y] not in air_coords:
                air_coords.append([x,y,i])
    #Draw each level
    x = []
    y = []
    x_2 = []
    y_2 = []
    for cube in cubes_to_check:
        x.append(cube[0])
        y.append(cube[1])
    for cube in air_coords:
        if cube[2] == i:
            x_2.append(cube[0])
            y_2.append(cube[1])
    plt.scatter(x, y)
    plt.title(i)
    plt.scatter(x_2,y_2)
    plt.show()
    
print("----------------")
print("removing cubes:")

remove_list = []
surface_removal = []
#Removes air if not all neighbours are air or stone
for coord in air_coords:
    neighbourz = find_2d_neighbours(coord)
    for coords in neighbourz:
        if coords not in air_coords and [coords[0],coords[1]] not in z_cubes[coord[2]]:
            print(coord)
            remove_list.append(coord)
            break

#check for air under
#Removes air if it can reach surface down
for cube in air_coords:
    next_cube = cube
    while next_cube not in cubes:
        next_cube = [next_cube[0],next_cube[1],next_cube[2]-1]
        if next_cube not in air_coords and next_cube not in cubes:
            print(cube)
            remove_list.append(cube)
            surface_removal.append(cube)
            break
            
#check for air over
#Removes air if it can reach surface up
for cube in air_coords:
    next_cube = cube
    while next_cube not in cubes:
        next_cube = [next_cube[0],next_cube[1],next_cube[2]+1]
        if next_cube not in air_coords and next_cube not in cubes:
            print(cube)
            remove_list.append(cube)
            surface_removal.append(cube)
            break

for cube in air_coords: #Should check all clusters in surface_removal
    if cube not in remove_list:
        neigh = find_neighbours(cube)
        for coord in neigh:
            if coord in surface_removal:
                print(cube)
                remove_list.append(cube)

for elements in remove_list:
    if elements in air_coords:
        air_coords.remove(elements)

counter = 0
for cube in air_coords:
    neigh = find_neighbours(cube)
    for pos in neigh:
        if pos in cubes:
            counter +=1
print("----------------")
print(f"Part 2: {sum_of_sides - counter}")
