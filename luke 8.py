def readfile():
    ranges_1 = []
    with open("input.txt",'r') as content:
        for line in content:
            ranges_1.append(line.split())
        
    data =[]
    for element in ranges_1:
        for numbers in element:
            data.append([int(x) for x in str(numbers)])
    return data

def check_up_down_left_right(data,x,y):
    width = len(data[0])
    height = len(data)    
    if x == 0 or x == (width-1) or y == 0 or y == (height -1):
        return 1
    else:
        #lup
        up_vis = True
        for i in range(0,x):
            if data[x][y] <= data[i][y]:
                up_vis = False
                break
        #down
        down_vis = True
        for i in range(x+1,height):
            if data[x][y] <= data[i][y]:
                down_vis = False
                break
        #left
        left_vis = True
        for i in range(0,y):
            if data[x][y] <= data[x][i]:
                left_vis = False
                break
        #right
        right_vis = True
        for i in range(y+1,width):
            if data[x][y] <= data[x][i]:
                right_vis = False
                break
                
    if not up_vis and not down_vis and not left_vis and not right_vis:
        return 0
    else:
        return 1
    
def view_dist(data,x,y):
    width = len(data[0])
    height = len(data)    
    #up
    up_view = 0
    for i in range(x-1,-1,-1):
        if data[x][y] > data[i][y]:
            up_view += 1
        elif data[x][y] <= data[i][y]:
            up_view += 1
            break
    #down
    down_view = 0
    for i in range(x+1,height):
        if data[x][y] > data[i][y]:
            down_view += 1
        elif data[x][y] <= data[i][y]:
            down_view += 1
            break
    #left
    left_view = 0
    for i in range(y+1,width):
        if data[x][y] > data[x][i]:
            left_view += 1
        elif data[x][y] <= data[x][i]:
            left_view += 1
            break
    #right
    right_view = 0
    for i in range(y-1,-1,-1):
        if data[x][y] > data[x][i]:
            right_view += 1
        elif data[x][y] <= data[x][i]:
            right_view += 1
            break
        
    return (left_view*right_view*up_view*down_view)

    
data = readfile()
width = len(data[0])
height = len(data) 

visible_trees = 0
for i in range(0,width):
    for j in range(0,height):
        visible_trees += check_up_down_left_right(data,i,j)
        
print(visible_trees)

view_score =[]
for i in range(1,width-1):
    for j in range(1,height-1):
        view_score.append(view_dist(data,i,j))
        
print(max(view_score))
