
# print the output grid to the file and command line
def printMaze(adjList, stack, H, W):
    file = open("out.txt", "w")
    for i in range(H):
        st = ""
        for j in range(W):
            # if the start node print 'S'
            if(i==0 and j==0):
                st += 'S'
            # if the last node print 'E'
            elif(i==H-1 and j==W-1):
                st += 'E'
            # stack is the path if node in stack print ' '(blank)
            elif ([i, j] in stack):
                st += " "
            # if obstacle or not in path print as it is
            else:
                st += adjList[i][j]
        print(st)
        # write to the file names "out.txt"
        file.write(st + "\n")