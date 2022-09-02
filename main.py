# author : melsonic
# version: 1.0.0
# shortest pathfinding algorithm
# startNode(0, 0) -> endNode(H-1, W-1)

import sys
import read
import countShortest as cs
import printGrid as pg


def main():
    # read the maze from the file
    adjList = read.readMaze(sys.argv[1])
    H = len(adjList)
    W = len(adjList[0])

    # print the original grid
    print("Initial Grid ===>\n")
    pg.printMaze(adjList, [], H, W)

    visit = [[False for i in range(W)] for j in range(H)]
    stack = []
    # main function to count the steps and print the output
    result = cs.countShortest(0, 0, adjList, stack, {}, visit)

    # print the final grid
    print("\nSolved Grid ===>\n")
    pg.printMaze(adjList, stack, H, W)

    #print the number of steps that took us to reach our final destination
    print("\nCell Count : ", len(stack) -
          1) if result else print("\nCell Count : ", -1)

# calling the main function
main()
