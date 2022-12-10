ranges_1 = []
with open("input.txt",'r') as content:
        for line in content:
            ranges_1.append(line.split(' '))
            
def find_height(liste): #Find where the boxes are
    for i in range(len(ranges_1)):
        for j in ranges_1[i]:
            if j == "1":
                return i
            
def create_lists_of_lists(numb): #Create lists for boxes and moveset
    list_of_lists = []
    for i in range(numb):
        list_of_lists.append([])
    return list_of_lists
            
def find_cols_box(liste, megaliste): #place boxes into a nested list
    for lines in liste:
        space_cnt = 0
        letter_cnt = 0
        last_pos = 0
        for i in range(len(lines)):
            if lines[i] != "" and lines[i] != "\n":
                if space_cnt == 0 and letter_cnt == i:
                    megaliste[i].append(lines[i][1])
                    letter_cnt += 1
                    space_cnt = 0
                elif space_cnt % 4 == 0:
                    megaliste[int(space_cnt/4) + last_pos].append(lines[i][1])
                    letter_cnt += 1
                    last_pos += int(space_cnt/4)+1
                    space_cnt = 0
            else:
                space_cnt += 1
        
    return(megaliste)

def create_moves(move_list):    #Read out the moveset and add to nested list.
    move_set = create_lists_of_lists(3)
    for lines in move_list:
        move_set[0].append(int(lines[1]))
        move_set[1].append(int(lines[3]))
        move_set[2].append(int(lines[5]))
    return move_set

def make_moves_9000(megalist, move_set): #Follow moveset one crate at the time
    for i in range(len(move_set[0])):
        for j in range(move_set[0][i]):
            megalist[move_set[2][i]-1].insert(0, megalist[move_set[1][i]-1].pop(0))
            
    return megalist

def make_moves_9001(megalist, move_set): #Follow moveset all crates at the time
    for i in range(len(move_set[0])):
        move_items =[]
        for j in range(move_set[0][i]):
            move_items.append(megalist[move_set[1][i]-1].pop(0))

        megalist[move_set[2][i]-1] = move_items + megalist[move_set[2][i]-1]
        move_items = []
        
    return megalist

def sol_print(liste): #Print solution
    a = ''
    for lists in liste:
        a += lists[0]
    print(a)

def part_1(input_list):

    boxes = ranges_1[0:find_height(ranges_1)]
    num_row =ranges_1[find_height(ranges_1)]
    max_box = int(num_row[-2])
    mega_list = create_lists_of_lists(max_box)
    bokser = find_cols_box(boxes,mega_list)
    
    moves = ranges_1[find_height(ranges_1)+2:]
    move_set = create_moves(moves)

    new_boxes = make_moves_9000(bokser, move_set)
    sol_print(new_boxes)

def part_2(input_list):

    boxes = ranges_1[0:find_height(ranges_1)]
    num_row =ranges_1[find_height(ranges_1)]
    max_box = int(num_row[-2])
    mega_list = create_lists_of_lists(max_box)
    bokser = find_cols_box(boxes,mega_list)
    
    moves = ranges_1[find_height(ranges_1)+2:]
    move_set = create_moves(moves)

    new_boxes2 = make_moves_9001(bokser, move_set)
    sol_print(new_boxes2)

part_1(ranges_1)
part_2(ranges_1)
    
