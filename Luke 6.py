def readfile():
    with open("input.txt",'r') as content:
        code = content.read()
        code_list = [*code]
    return code_list

def find_packet(liste):
    for i in range(len(liste)-3):
        next_four = liste[i:i+4]
        if len(set(next_four)) == 4:
            print(i+4)
            break


def find_msg(liste):
    for i in range(len(liste)-13):
        next_four = liste[i:i+14]
        if len(set(next_four)) == 14:
            print(i+14)
            break
        
code_list = readfile()
find_packet(code_list)
find_msg(code_list)
