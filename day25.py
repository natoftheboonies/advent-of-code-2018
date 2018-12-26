from collections import deque
input = """
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
""".split('\n')

with open('input25.txt') as fp:
    input = fp.read().strip().split('\n')


points = []
for line in input:
    coords = line.split(',')
    if len(coords) == 4:
        points.append(tuple(map(int, coords)))
#print(points)
sky = []
for coord in points:
    matched = None
    #print ("coord",coord)
    if not sky:
        sky.append([coord])
        continue
    c = 0
    for const in sky:
        s = 0
        for star in const:
            if star == coord: 
                print("why?!?")
                continue
            dist = abs(coord[0]-star[0])+abs(coord[1]-star[1])+abs(coord[2]-star[2])+abs(coord[3]-star[3])
            #print (c,s,"dist {} to {} is".format(coord, star),dist)
            if dist <= 3:
                if matched != None:
                    #print("also matched", c)
                    #print(sky, matched)
                    if c != matched: 
                        sky[matched].extend(sky.pop(c))
                        #print("popped", sky)
                else:
                    const.append(coord)       
                    #print("appended to", c)
                    matched = c
                break
            s+=1
        c+=1
    if matched == None:
        #print("not matched") 
        sky.append([coord])

print("#1:", len(sky))
#print(sky)

# not 575


