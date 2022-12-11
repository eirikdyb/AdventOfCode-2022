def readfile():
    data = []
    item_list = []
    new_items = []
    operators = []
    value = []
    div_test = []
    true_list = []
    false_list = []
    with open("input.txt",'r') as content:
        for line in content:
            data.append(line.split())
            line = line.split()
            collect = False
            for j in range(len(line)):
                element = line[j]
                if line[j-2] == 'Starting' and line[j-1] == "items:":
                    collect = True
                if collect:
                    new_items.append(int(element.replace(',', '')))
                if element == 'Operation:':
                    collect = False
                    item_list.append(new_items)
                    new_items = []
                if line[j-2] == '=' and line[j-1] == "old":
                    operators.append(element)
                    if line[j+1].isnumeric():
                        value.append(int(line[j+1]))
                    else:
                        value.append(line[j+1])
                if line[j-2] == 'divisible' and line[j-1] == "by":
                    div_test.append(int(element))
                if j>4:
                    if line[j-4] == 'true:' and line[j-3] == "throw":
                        true_list.append(int(element))
                    if line[j-4] == 'false:' and line[j-3] == "throw":
                        false_list.append(int(element))
    return item_list, operators, div_test, true_list, false_list, value

def update_worry_level(worry_level, operator, value):
    if value == "old":
        value = worry_level
    if operator == "+":
        worry_level += value
    elif operator == "*":
        worry_level *= value
    return worry_level #//3 for part 1

def modulo(worry_level, value, divisor,operator):
        if operator == "+":
            return (worry_level % divisor + value % divisor) % divisor
        elif operator == "*":
            return (worry_level % divisor * value % divisor) % divisor
        
def product_of_divisors(divisors):
    prod = 1
    for div in divisors:
        prod *= div
    return prod

def monkey_round(items, operators, value, true_list, false_list, inspect_list,div_test):
    for i in range(len(items)):
        for j in range(len(items[i])):
            worry_level = update_worry_level(items[i][j], operators[i],value[i])
            inspect_list[i] += 1
            worry_level = worry_level % product_of_divisors(div_test)
            if worry_level % div_test[i] == 0:
                items[true_list[i]].append(worry_level)
            else:
                items[false_list[i]].append(worry_level)
        items[i] = []
    return items, inspect_list

items, operators, div_test, true_list, false_list,value = readfile()
rounds = 10000
inspect_list = []
for i in range(len(items)):
    inspect_list.append(0)

for i in range(rounds):
    items,inspect_list = monkey_round(items, operators,value, true_list,false_list,inspect_list,div_test)

inspect_list.sort()
print(inspect_list[-2]*inspect_list[-1])
