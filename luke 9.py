def readfile():
    data = []
    with open("input.txt",'r') as content:
        for line in content:
            data.append(line.split())
    return data

def update_head(h_pos,line):
    h_x = h_pos[0]
    h_y = h_pos[1]
    if line[0] == 'R': #right
        h_x += 1
    elif line[0] == 'L': #left
        h_x -= 1
    elif line[0] == 'U': #up
        h_y += 1
    elif line[0] == 'D': #down
        h_y -= 1
    h_pos[0] = h_x
    h_pos[1] = h_y 
    return h_pos

def update_tail(h_pos,t_pos):
    h_x = h_pos[0]
    h_y = h_pos[1]
    t_x = t_pos[0]
    t_y = t_pos[1]
    if t_x == h_x and h_y == t_y + 2: #up
        t_y += 1
    elif t_x == h_x and h_y == t_y -2: #down
        t_y -=1
    elif t_y == h_y and h_x == t_x + 2: #right
        t_x +=1
    elif t_y == h_y and h_x == t_x -2: #left
        t_x -=1
    elif h_x -1 <= t_x <= h_x +1 and h_y - 1 <= t_y <= h_y +1: #stay still
        return t_pos
    elif h_x == t_x +1 and h_y == t_y + 2 or (h_x == t_x +2 and h_y == t_y +1): #up right
        t_x += 1
        t_y +=1
    elif h_x == t_x -1 and h_y == t_y + 2 or (h_x == t_x -2 and h_y==t_y +1): #up left
        t_x -= 1
        t_y +=1
    elif h_x == t_x + 1 and h_y == t_y - 2 or (h_x == t_x + 2 and h_y == t_y - 1): #down right
        t_x += 1
        t_y -= 1
    elif h_x == t_x -1 and h_y == t_y - 2 or (h_x == t_x -2 and h_y == t_y - 1): #down left
        t_x -= 1
        t_y -= 1    
    #part 2 moves
    if h_x == t_x + 2 and h_y == t_y + 2: #up right
        t_x += 1
        t_y += 1
    elif h_x == t_x + 2 and h_y == t_y - 2:#down right
        t_x += 1
        t_y -= 1
    elif h_x == t_x - 2 and h_y == t_y + 2: #up left
        t_x -= 1
        t_y += 1
    elif h_x == t_x - 2 and h_y == t_y - 2: #down left
        t_x -= 1
        t_y -= 1   
    t_pos[0] = t_x
    t_pos[1] = t_y
    return t_pos

def find_unique_pos(list_of_coord): #Find number of unique elements in list
    uni_pos =[list_of_coord[0]]
    for coord in list_of_coord:
        add = True
        for pos in uni_pos:
            if coord == pos:
                add = False
                break
        if add:
            uni_pos.append(coord)     
    return len(uni_pos)

def create_rope(rope_length):
    rope_pos = []
    for i in range(rope_length):
        rope_pos.append([0,0])   
    return rope_pos

def tail_history(data,rope):
    t_pos_hist = [[0,0]] #intialize pos of tail knot
    for lines in data:
        for i in range(int(lines[1])):
            rope[0] = update_head(rope[0], lines)
            for j in range(1,len(rope)):
                rope[j] = update_tail(rope[j-1], rope[j])
            t_pos_hist.append([rope[-1][0],rope[-1][1]])      
    return t_pos_hist

#print(find_unique_pos(tail_history(readfile(), create_rope(10))))
data = readfile()
rope_length = 10 #part 1: 2 part2: 10
rope = create_rope(rope_length)
tail_pos = tail_history(data,rope)
num_of_pos = find_unique_pos(tail_pos)
print(num_of_pos)
