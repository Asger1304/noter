'''
    COIN COLLECTOR

    Consider a rectangular maze of height x width cells. Each cell is
    either blocked by a wall '#', a free cell '.', a cell with a gold
    coin 'x', or a starting cell 'S'. A maze contains exactly one 'S'.
    Your task is to compute how many gold coins can be collected
    starting from 'S' when you are only allowed to move horizontally or
    vertically to adjacent cells not blocked by a wall. See example below.

    Input:

      The first line contains two positive integers height and width,
      separated by space, where 1 <= height <= 25 and 1 <= width <= 25.
      The following height lines each contain a row of the maze.  Each
      row has length width and contains only characters from '#Sx.'.

    Ouput: 

      A single line with the number of gold coins collectable from 'S'.

    Example:

      Input:  7 9
              #########
              #..x.x.x#
              ###.#####
              #.#S.x#x#
              #.#####.#
              #.#x.x.x#
              #########

      Output: 4
'''


y,x=tuple(map(int,input().split()))
maze=[]
for _ in range(y):
    maze.append(list(input()))

def s_finder(maze):
   for y in range(len(maze)):
      for x in range(len(maze[0])):
         if maze[y][x]=="S":
            return (y,x)
         
visited=[[False for _ in range(x)] for _ in range(y)]
Q = [s_finder(maze)] # cells to visit
coins=0
while Q:
  i, j = Q.pop()
  if (0 <= i < y and 0 <= j < x and
    maze[i][j] != '#' and not visited[i][j]):
    visited[i][j] = True
    if maze[i][j] == 'x':
      coins +=1
    Q.append((i - 1, j))
    Q.append((i + 1, j))
    Q.append((i, j - 1))
    Q.append((i, j + 1))
print(coins)



#for i in range(len(maze)):
#    print("".join(maze[i]))
