def readfile():
    data = []
    with open("input.txt",'r') as content:
        for line in content:
            data.append(line.split())
    return data

def increase_signal_strength(sig_strength, cycle,value):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        sig_strength = cycle*value
    else:
        sig_strength = 0
    return sig_strength

#part 2 func
def create_monitor(width, height):
    monitor_list = []
    for i in range(height):
        for j in range(width):
            monitor_list.append(".")
    return monitor_list

def print_monitor_to_txt(screen, width):
    new_screen = []
    for i in range(int(len(screen)/width)):
        new_screen.append(screen[i*width:width+i*width])
    f = open("screen.txt", "w")
    for lines in new_screen:
        for symbol in lines:
            f.write(symbol)
        f.write("\n")
    f.close()

def sprite_pos(value):
    return [value-1,value,value+1]

def draw_pixel(cycle, value, width):
    if cycle % width in sprite_pos(value):
        return '#'
    else:
        return '.'
cycle = 0
value = 1
sig_strength = 0
width = 40
height = 6
monitor = create_monitor(width, height)

for lines in readfile():
    if lines[0] == 'noop':
        monitor[cycle] = draw_pixel(cycle, value, width)
        cycle += 1
        sig_strength += increase_signal_strength(sig_strength, cycle,value)
    elif lines[0] == 'addx':
        monitor[cycle] = draw_pixel(cycle, value, width)
        cycle += 1
        sig_strength += increase_signal_strength(sig_strength, cycle,value)
        monitor[cycle] = draw_pixel(cycle, value, width)
        cycle +=1 
        sig_strength += increase_signal_strength(sig_strength, cycle,value)
        value += int(lines[1])

print(sig_strength)
print_monitor_to_txt(monitor, width)
