def countShortest(i, j, adjList, stack, map, visit):

    H = len(adjList)
    W = len(adjList[0])

    # if node in stack then we have already visited and it is creating a cycle
    if [i, j] in stack:
        return False

    # if reached the final destination return true
    if (i == H-1 and j == W-1):
        return True

    result = False

    # mark the current node visited
    visit[i][j] = True
    XY = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tempMemo = []

    # add all the possible neighbouring nodes to our path stack
    for xy in XY:
        tempX = i+xy[0]
        tempY = j+xy[1]
        if(canMove(tempX, tempY, H, W, adjList, visit)):
            stack.append([tempX, tempY])
            tempMemo.append([tempX, tempY])
    
    # for each neighbour node check if leads us to the shortest path
    # if yes let it be in the stack
    # if not remove it from the stack
    for item in tempMemo:
        if (not (result)):
            stack.remove([item[0], item[1]])
            result = countShortest(item[0], item[1], adjList, stack, map, visit)
            if (result):
                stack.append([item[0], item[1]])
        elif (result):
            stack.remove([item[0], item[1]])
    return result

# determine if we can move to the grid node
def canMove(i, j, H, W, adjList, visit):
    if (0 <= i < H and 0 <= j < W):
        if (adjList[i][j]=='#' and visit[i][j]==False):
            return True
    return False