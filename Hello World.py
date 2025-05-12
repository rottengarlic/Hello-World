import utility
import queue
import sys

e={0:[1,2,3],1:[2,5], 2:[3,4,5,6], 3:[4,6], 4:[6,7]}
n = 8
a = [[0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1
utility.printMatrix(a)
visited = n*[0]

def BFS(a,v):
    q = queue.Queue()
    visited[v] = 1
    for i in range(len(a[v])):
        if(a[v][i]!=0 and visited[i] != 1):
            print(i)
            visited[i] = 1
            q.put(i)
            a[v][i] = 0
            a[i][v] = 0
    while(q.empty() != 1):
        BFS(a,q.get())
    return 0

BFS(a,0)



def promising(x, col):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
            return False
    
    return True

def queens(n,x,col):
    x+=1
    if x == n:
        print(col)
        return

    else:
        for i in range(n):
            col[x] = i
            if promising(x,col):
                queens(n,x,col)


n=5
col=n*[0]
queens(n,-1,col)
