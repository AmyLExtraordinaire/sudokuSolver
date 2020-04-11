import sys

def solve(board):
    domains = [] #TODO, fill domains

    """
    backtracking algroithm
    if an index had no available domain,
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = getNeighbors({i,j}, board, domains)

    return board

"""
looks at each of the neighbors for a given index
returns a list of the neighbor indexes for the given index
"""
def getNeighbors(index, board):
    neighbors = []
    for i in range(9):
        if i != index[0]:
            neighbors.append({i,index[1]})

        if i != index[1]:
            neighors.append({index[0],i})

    if inRange({index[0]-1,index[1]+1}):
        neighors.append({index[0]-1,index[1]+1})

    if inRange({index[0]+1,index[1]+1}):
        neighors.append({index[0]+1,index[1]+1})

    if inRange({index[0]+1,index[1]-1}):
        neighors.append({index[0]+1,index[1]-1})

    if inRange({index[0]-1,index[1]-1}):
        neighors.append({index[0]-1,index[1]-1})

    return neighbors

#takes index and returns if the index is in the board
def inRange(index):
    if index[0] > 8 or index[0] < 0:
        return false
    if index[1] > 8 or index[1] < 0:
        return false
    return true

"""
gets domain of the current index
achieves this by removing the already assigned neighbors
"""
def getDomain(neighbors, board, domains):
    dom = [1,2,3,4,5,6,7,8,9]
    for i in neighbors:

    return dom

def main():
    #TODO: input option to set your own sudoku board
    #define the sudoku board
    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    #call the sudoku function
    board = solve(board)
    print(board)

if __name__ == "__main__":
    main()