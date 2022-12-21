def readfile():
    numbers= []
    operations = []
    monkey_dict = {}
    with open("input.txt",'r') as content:
        for lines in content:
            if lines.strip().split(": ")[1].isnumeric():
                numbers.append(lines.strip().split(": "))
            else:
                a = ''
                b = ''
                counter = 0
                for char in lines.strip().split(": ")[1]:
                    if char == " ":
                        counter +=1
                    if counter == 0:
                        a += char
                    elif counter == 1:
                        operator = char
                    elif counter == 2 and char != " ":
                        b+=char
                operations.append([lines.strip().split(": ")[0],a,operator,b])
                
        
    for elements in numbers:
        monkey_dict[elements[0]] = int(elements[1])
    for elements in operations:
        monkey_dict[elements[0]] = [elements[1],elements[2],elements[3]] 
    return monkey_dict
            
def find_next_value(monkey,monkey_dict):
    if isinstance(monkey, list):
        monkey = monkey[0]
    if  isinstance(monkey_dict[monkey], list):
        return [monkey_dict[monkey][0],monkey_dict[monkey][2]]
    else:
        return monkey_dict[monkey]

def do_operation(liste, monkey_dict):
    if liste[1] == "+":
        return monkey_dict[liste[0]] + monkey_dict[liste[2]]
    elif liste[1] == "-":
        return monkey_dict[liste[0]] - monkey_dict[liste[2]]
    elif liste[1] == "*":
        return monkey_dict[liste[0]] * monkey_dict[liste[2]]
    elif liste[1] == "/":
        return int(monkey_dict[liste[0]] / monkey_dict[liste[2]])

def find_human_path(monkey_dict):
    path = ['humn']
    operator = []
    i = 0
    while path[-1] != 'root':
        for key in monkey_dict:
            if isinstance(monkey_dict[key],list):
                # print(monkey_dict[key][0],monkey_dict[key][2])
                if monkey_dict[key][0] == path[i] or monkey_dict[key][2] == path[i]:
                    path.append(key)
                    operator.append(monkey_dict[key])
                    i += 1
                    break
    return path, operator

def inverse_operator(oper):
    if oper == "+":
        return "-"
    elif oper == "-":
        return "+"
    elif oper == "*":
        return "/"
    elif oper == "/":
        return "*"

def ez_math(a,b,c):
    if c == "*":
        return a*b
    elif c == "/":
        return int(a/b)
    elif c == "+":
        return a + b
    elif c == "-":
        return a-b

#part one
monkeys = readfile()
while isinstance(monkeys['root'], list):
    for monk in monkeys:
        # print(monkeys[monk])
        if isinstance(monkeys[monk], list):
            a = monkeys[monk][0]
            b = monkeys[monk][2]
            # print(a,b)
            if isinstance(monkeys[a], int) and isinstance(monkeys[b], int):
                monkeys[monk] = do_operation(monkeys[monk], monkeys)
print(f"Part one: {monkeys['root']}")

#part two
monkeys_2 = readfile()
human_path, operator_list = find_human_path(monkeys_2)
root_monkeys = [monkeys_2['root'][0], monkeys_2['root'][2]]

for roots in root_monkeys:   #Find which part of root that doesnt lead to humn
    if roots != human_path[-2]:
        sum_monkey = roots

operator_list.pop(-1)   #Remove step to root
operator_list.reverse()   #Reverse the list, to move from known value to humn
reach = monkeys[sum_monkey]

#Solving reach = a + b, reach = a - b, reach = a*b and reach = a/b for a and b
for elements in operator_list:
    if elements[0] in human_path:
        if elements[1] == "+":   #a =reach -b
            reach = ez_math(reach,monkeys[elements[2]],inverse_operator(elements[1]))
        elif elements[1] == "-":   #a = reach +b
            reach = ez_math(reach,monkeys[elements[2]],inverse_operator(elements[1]))
        elif elements[1] == "*":   #a = reach/b
            reach = ez_math(reach,monkeys[elements[2]],inverse_operator(elements[1]))
        elif elements[1] == "/":   #a = reach*b
            reach = ez_math(reach,monkeys[elements[2]],inverse_operator(elements[1]))
    elif elements[2] in human_path:
        if elements[1] == "+":   #b = reach -a
            reach = ez_math(reach,monkeys[elements[0]],inverse_operator(elements[1]))
        elif elements[1] == "-":   #b= a - reach
            reach = ez_math(monkeys[elements[0]], reach, elements[1])
        elif elements[1] == "*":   #b = reach/a
            reach = ez_math(reach,monkeys[elements[0]],inverse_operator(elements[1]))
        elif elements[1] == "/":   #b = a/reach
            reach = ez_math(monkeys[elements[0]], reach, elements[1])

print(f"Part two: {reach}")

#Check solution
monkeys_3 = readfile()
monkeys_3['humn'] = reach #Set human to result of part two
while isinstance(monkeys_3['root'], list):
    for monk in monkeys_3:
        # print(monkeys[monk])
        if isinstance(monkeys_3[monk], list):
            a = monkeys_3[monk][0]
            b = monkeys_3[monk][2]
            # print(a,b)
            if isinstance(monkeys_3[a], int) and isinstance(monkeys_3[b], int):
                monkeys_3[monk] = do_operation(monkeys_3[monk], monkeys_3)

print(f"Part two diff: {abs(monkeys_3['root']- 2*monkeys[sum_monkey])}")
