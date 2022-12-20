def readfile():
    code = []
    code_move = []
    with open("input.txt",'r') as content:
        for lines in content:
            code.append(int(lines))
            code_move.append([int(lines),0])
    return code, code_move
            
code, code_move = readfile()

part = 1

if part == 2:
    for i in range(len(code_move)):
        code_move[i][0] *= 811589153
        code[i] *= 811589153
    rounds = 10
else:
    rounds = 1

num_of_codes = len(code_move)
for j in range(rounds):
    for i in range(num_of_codes):
        item = code[i]
        for p in range(len(code_move)):
            if j == 0:
                if code_move[p][0] == item and code_move[p][1] == 0:
                    index = p
                    break
            if j != 0:
                if code_move[p][0] == item and code_move[p][1] == i:
                    index = p
                    break
        move_item = code_move.pop(index)[0]
        steps = abs(move_item) % (num_of_codes-1)
        if steps != 0:
            steps *= int(abs(move_item)/move_item)
        if (steps + index) <0:
            steps -= 1
        elif (steps + index) > (num_of_codes-1):
            steps += 1
        new_pos = (index + steps) % num_of_codes
        if new_pos == 0 and move_item != 0:
            code_move.append([move_item,i])
            new_pos = num_of_codes -1
        else:
            code_move.insert(new_pos, [move_item,i])
        # print(f"Moved {move_item} from {index} to {new_pos}.")
        # print([x[0] for x in code_move])

code_list = [x[0] for x in code_move]
index = code_list.index(0)
#1000th after 0
a = code_list[(index + 1000) % (num_of_codes)]
#2000th after 0
b = code_list[(index + 2000) % (num_of_codes)]
#3000th after 0
c = code_list[(index + 3000) % (num_of_codes)]
print(f"Sol: {a+b+c}")
