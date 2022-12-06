def readfile():
    with open("input.txt",'r') as content:
        code = content.read()
        code_list = [*code]
    return code_list

def find_unique_elements(string_list, numb):
    for i in range(len(string_list)-numb-1):
        next_chars = string_list[i:i+numb]
        if len(set(next_chars)) == numb:
            print(i+numb)
            break
        
find_unique_elements(readfile(), 4)
find_unique_elements(readfile(), 14)
