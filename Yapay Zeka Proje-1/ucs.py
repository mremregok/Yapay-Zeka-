import time
PacMap = [["0,0","%"],["0,1","-"],["0,2","-"],["0,3","-"],["0,4","-"],["0,5","-"],["0,6","-"],["0,7","-"],["0,8","-"],["0,9","%"],
          ["1,0","|"],["1,1"," "],["1,2"," "],["1,3"," "],["1,4"," "],["1,5","X"],["1,6","X"],["1,7","X"],["1,8","X"],["1,9","|"],
          ["2,0","|"],["2,1"," "],["2,2","X"],["2,3","X"],["2,4"," "],["2,5","X"],["2,6"," "],["2,7"," "],["2,8","X"],["2,9","|"],
          ["3,0","|"],["3,1","X"],["3,2"," "],["3,3","X"],["3,4"," "],["3,5","X"],["3,6","X"],["3,7"," "],["3,8","X"],["3,9","|"],
          ["4,0","|"],["4,1","X"],["4,2"," "],["4,3","X"],["4,4"," "],["4,5"," "],["4,6"," "],["4,7"," "],["4,8","X"],["4,9","|"],
          ["5,0","|"],["5,1","X"],["5,2"," "],["5,3"," "],["5,4"," "],["5,5","X"],["5,6"," "],["5,7","X"],["5,8","X"],["5,9","|"],
          ["6,0","|"],["6,1"," "],["6,2"," "],["6,3","X"],["6,4","X"],["6,5","X"],["6,6"," "],["6,7"," "],["6,8","X"],["6,9","|"],
          ["7,0","|"],["7,1"," "],["7,2","X"],["7,3","X"],["7,4"," "],["7,5","X"],["7,6"," "],["7,7","X"],["7,8","X"],["7,9","|"],
          ["8,0","|"],["8,1"," "],["8,2","X"],["8,3"," "],["8,4"," "],["8,5"," "],["8,6"," "],["8,7"," "],["8,8","X"],["8,9","|"],
          ["9,0","%"],["9,1","-"],["9,2","-"],["9,3","-"],["9,4","-"],["9,5","-"],["9,6","-"],["9,7","-"],["9,8","-"],["9,9","%"],]

PacDict = {'1.1': ['1.2','2.1'], '1.2': ['1.1','1.3'], '1.3': ['1.2','1.4'], '1.4': ['1.3','1.5'], '1.5': ['1.4','1.6','2.5'], '1.6': ['1.5','1.7'], '1.7': ['1.6','1.8'], '1.8': ['1.7','2.8'],
           '2.1': ['1.1','3.1'], '2.5': ['1.5','3.5'], '2.8': ['1.8','3.8'],
           '3.1': ['2.1','3.2','4.1'], '3.2': ['3.1','3.3'], '3.3': ['3.2','3.4','4.3'], '3.4': ['3.3','3.5'], '3.5': ['2.5','3.4','3.6','4.5'], '3.6': ['3.5'], '3.8': ['2.8','4.8'],
           '4.1': ['3.1','5.1'], '4.3': ['3.3','5.3'], '4.5': ['3.5','5.5'], '4.7': ['4.8'], '4.8': ['3.8','4.7','5.8'],
           '5.1': ['4.1','6.1'], '5.3': ['4.3','6.3'], '5.5': ['4.5','6.5'], '5.8': ['4.8','6.8'],
           '6.1': ['5.1','6.2','7.1'], '6.2': ['6.1','6.3'], '6.3': ['5.3','6.2','6.4'], '6.4': ['6.3','6.5'], '6.5': ['5.5','6.4','6.6'], '6.6': ['6.5', '6.7'], '6.7': ['6.6','6.8'], '6.8': ['5.8','6.7','7.8'],
           '7.1': ['6.1','8.1'], '7.8': ['6.8','8.8'],
           '8.1': ['7.1','8.2'], '8.2': ['8.1','8.3'],'8.3': ['8.2','8.4'], '8.4': ['8.3','8.5'], '8.5': ['8.4','8.6'], '8.6': ['8.5','8.7'], '8.7': ['8.6','8.8'], '8.8': ['7.8','8.7']}

def MapDrawer():
    i = 0
    while i < len(PacMap):
        print(PacMap[i][1], end = " ")
        if (i % 10) == 9:
            print("\n")        
        i = i + 1
    time.sleep(0.5)

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def PacFinder(x,y):
    a = 0

    while a < len(PacMap):
        if PacMap[a][0] == x:
            PacMap[a][1] = "C"
        if PacMap[a][0] == y:
            PacMap[a][1] = "Y"
        a = a + 1
        
    list = find_all_paths(PacDict,x,y)

    shortest = []

    for i in list:
        if shortest == []:
           shortest = i
           continue
        if len(i) < len(shortest): 
            shortest = i

    x = 0
    y = 0
    z = 0
    while z < len(shortest):
        while x < len(PacMap):
            if shortest[z] == PacMap[x][0]:
                while y < len(PacMap):
                    if PacMap[y][1] == "C":
                        PacMap[y][1] = " "
                        PacMap[x][1] = "C"
                        MapDrawer()
                    y = y + 1
            x = x + 1
            y = 0
        x = 0
        z = z + 1
    print("Düğüm ziyaret listesi: ",shortest)

