def readfile():
    numbers = []
    operations = []
    monkey_dict = {}
    with open("input.txt", 'r') as content:
        for lines in content:
            if lines.strip().split(": ")[1].isnumeric():
                numbers.append(lines.strip().split(": "))
            else:
                a = ''
                b = ''
                counter = 0
                for char in lines.strip().split(": ")[1]:
                    if char == " ":
                        counter += 1
                    if counter == 0:
                        a += char
                    elif counter == 1:
                        operator = char
                    elif counter == 2 and char != " ":
                        b += char
                operations.append([lines.strip().split(": ")[0], a, operator, b])

    for elements in numbers:
        monkey_dict[elements[0]] = int(elements[1])
    for elements in operations:
        monkey_dict[elements[0]] = [elements[1], elements[2], elements[3]]
    return monkey_dict

def find_human_path(monkey_dict):
    path = ['humn']
    operator = []
    i = 0
    while path[-1] != 'root':
        for key in monkey_dict:
            if isinstance(monkey_dict[key], list):
                if monkey_dict[key][0] == path[i] or monkey_dict[key][2] == path[i]:
                    path.append(key)
                    operator.append(monkey_dict[key])
                    i += 1
                    break
    operator.pop(-1)   #Remove root line
    operator.reverse() #move from root to humn
    return path, operator

# part one
monkeys = readfile()
while isinstance(monkeys['root'], list):
    for monk in monkeys:
        if isinstance(monkeys[monk], list):
            a = monkeys[monk][0]
            b = monkeys[monk][2]
            if isinstance(monkeys[a], int) and isinstance(monkeys[b], int):
                if monkeys[monk][1] == "+":
                    monkeys[monk] = monkeys[a] + monkeys[b]
                elif monkeys[monk][1] == "-":
                    monkeys[monk] = monkeys[a] - monkeys[b]
                elif monkeys[monk][1] == "*":
                    monkeys[monk] = monkeys[a] * monkeys[b]
                elif monkeys[monk][1] == "/":
                    monkeys[monk] = int(monkeys[a]/monkeys[b])

print(f"Part one: {monkeys['root']}")

# part two
monkeys_2 = readfile()
human_path, operator_list = find_human_path(monkeys_2)
root_monkeys = [monkeys_2['root'][0], monkeys_2['root'][2]]

for roots in root_monkeys:  # Find which part of root that doesnt lead to humn
    if roots != human_path[-2]:
        sum_monkey = roots

root_human = monkeys[sum_monkey] #Choose human such that other part of root is equal
# Solving root_human = a + b, root_human = a - b, root_human = a*b and root_human = a/b for a and b
for elements in operator_list:
    a = monkeys[elements[0]]
    b = monkeys[elements[2]]
    if elements[0] in human_path:   #solve for a
        if elements[1] == "+":
            root_human =root_human - b
        elif elements[1] == "-":
            root_human = root_human + b
        elif elements[1] == "*":
            root_human = int(root_human/b)
        elif elements[1] == "/":
            root_human = root_human * b
    elif elements[2] in human_path:   #solve for b
        if elements[1] == "+":
            root_human = root_human - a
        elif elements[1] == "-":
            root_human = a - root_human
        elif elements[1] == "*":
            root_human = int(root_human/a)
        elif elements[1] == "/":
            root_human = int(a/root_human)

print(f"Part two: {root_human}")

# Check solution
monkeys_3 = readfile()
monkeys_3['humn'] = root_human  # Set human to result of part two
while isinstance(monkeys_3['root'], list):
    for monk in monkeys_3:
        if isinstance(monkeys_3[monk], list):
            a = monkeys_3[monk][0]
            b = monkeys_3[monk][2]
            if isinstance(monkeys_3[a], int) and isinstance(monkeys_3[b], int):
                if monkeys_3[monk][1] == "+":
                    monkeys_3[monk] = monkeys_3[a] + monkeys_3[b]
                elif monkeys_3[monk][1] == "-":
                    monkeys_3[monk] = monkeys_3[a] - monkeys_3[b]
                elif monkeys_3[monk][1] == "*":
                    monkeys_3[monk] = monkeys_3[a] * monkeys_3[b]
                elif monkeys_3[monk][1] == "/":
                    monkeys_3[monk] = int(monkeys_3[a]/monkeys_3[b])

print(f"Part two diff: {abs(monkeys_3['root'] - 2 * monkeys[sum_monkey])}")
