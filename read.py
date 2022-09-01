# function to read a text file 
# '#' represents can be visited Node
# 'O' represents obstacle
def readMaze(path):
    grid = []
    file = open(path)
    maze = file.readlines()
    grid = [line.strip() for line in maze]
    return grid
