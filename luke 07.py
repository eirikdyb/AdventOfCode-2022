def readfile():
    data = []
    with open("input.txt",'r') as content:
        for lines in content:
            data.append(lines.strip())
    new_data = []
    for elements in data:
        new_data.append(elements.split())
    return new_data

def update_dir(current_dir,cmd_line):
    if cmd_line[1] == 'cd':
        if cmd_line[2] == '..':
            current_dir.pop()
        else:
            current_dir.append(cmd_line[2])
    return current_dir

def add_files(current_dir,cmd_line):
    folder_size = 0
    if cmd_line[0].isnumeric():
        folder_size = int(cmd_line[0])
    return folder_size

cmd = readfile()
current_dir = []
files_and_dir = dict()
for lines in cmd:
    current_dir = update_dir(current_dir,lines)  
    files_and_dir[str(current_dir)] = 0

current_dir= []
for lines in cmd:
    current_dir = update_dir(current_dir,lines) 
    if add_files(current_dir,lines) != 0:
        files_and_dir[str(current_dir)] += add_files(current_dir,lines)

key_list = []
for keys in files_and_dir:
    key_list.append(eval(keys))


tot_folder_size = []
for j in range(len(key_list)):
    size = 0
    for k in range(len(key_list)):
        counter = 0
        for i in range(len(key_list[j])):
            if i < len(key_list[k]):
                if key_list[j][i] in key_list[k][i]:
                    counter +=1
                    if counter == len(key_list[j]):
                        size += files_and_dir[str(key_list[k])]
                else:
                    break
    
    tot_folder_size.append(size)



solution_sum = 0
for sizes in tot_folder_size:
    if sizes <=100000:
        solution_sum += sizes
        
print(f"Solution part 1: {solution_sum}")

disk_space = 70000000
needed_space = 30000000
space_now = disk_space - tot_folder_size[0]
a = needed_space-space_now
pot_folder = []
for sizes in tot_folder_size:
    if sizes >= a:
        pot_folder.append(sizes)
pot_folder.sort()
print(f"Solution part 2: {pot_folder[0]}")
