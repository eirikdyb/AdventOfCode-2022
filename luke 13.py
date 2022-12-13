import ast
def readfile():
    data = []
    new_data = []
    with open("input.txt", 'r') as content:
        for line in content:
            if line == "\n":
                continue
            else:
                data.append(line.split())
    for lines in data:
        new_data.append(ast.literal_eval(lines[0]))
    return new_data

def compare_list_and_list(A, B):
    max_length = max(len(A), len(B))
    for k in range(max_length):
        if k > len(B) - 1:
            return 0
        elif k > len(A) - 1:
            return 1
        if isinstance(A[k], int) and isinstance(B[k], int):
            if A[k]> B[k]:
                return 0
            elif A[k] < B[k]:
                return 1
        else:
            if isinstance(A[k], list) and isinstance(B[k], int):
                if compare_list_and_list(A[k], [B[k]]) == 0:
                    return 0
                elif compare_list_and_list(A[k], [B[k]]) == 1:
                    return 1
            elif isinstance(A[k], int) and isinstance(B[k], list):
                if compare_list_and_list([A[k]], B[k]) == 0:
                    return 0
                elif compare_list_and_list([A[k]], B[k]) == 1:
                    return 1
            elif isinstance(A[k], list) and isinstance(B[k], list):
                if compare_list_and_list(A[k], B[k]) == 0:
                    return 0
                elif compare_list_and_list(A[k], B[k]) == 1:
                    return 1

input = readfile()
sum_of_pairs = 0
for i in range(0, len(input), 2):
    if compare_list_and_list(input[i], input[i+1]) == 1:
        sum_of_pairs += int(i/2+1)
print(sum_of_pairs)

sorted_packets = [[[2]],[[6]]]
for packet in input:
    for j in range(len(sorted_packets)):
        counter = 0
        if compare_list_and_list(packet, sorted_packets[j]) == 1:
            sorted_packets.insert(j,packet)
            break
        elif compare_list_and_list(packet, sorted_packets[j]) == 0:
            counter += 1
    if counter > 0:
        sorted_packets.append(packet)

decoder_key = 1
for i in range(len(sorted_packets)):
    if sorted_packets[i] == [[6]] or sorted_packets[i] == [[2]]:
        decoder_key *= (i+1)
print(decoder_key)
