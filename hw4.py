import sys

def solve(matrix):
    def memoize(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            up=down=left=right=0
            if(i-1>=0):
                if(val<matrix[i-1][j]):
                    up=memoize(i-1,j)
            if(i+1<len(matrix)):
                if(val<matrix[i+1][j]):
                    down=memoize(i+1,j)
            if(j-1>=0):
                if(val<matrix[i][j-1]):
                    left=memoize(i,j-1)
            if(j+1<len(matrix[i])):
                if(val<matrix[i][j+1]):
                    right=memoize(i,j+1)
            dp[i][j]=max(up,down,left,right)+1
        return dp[i][j]
    dp=[]
    for i in range(0,len(matrix)):
        dp.append([0 for x in range(0,len(matrix[0]))])
    for i in range(0,len(dp)):
        for j in range(0,len(dp[i])):
            memoize(i,j)
    return max(dp[x][y] for x in range(len(matrix)) for y in range(len(matrix[0])))


infile = open(sys.argv[1],"r")
numCities = int(infile.readline())
solnList = []
for x in range(0,numCities):
    line = infile.readline().split()
    r = int(line[1])
    c = int(line[2])
    matrix = []
    for i in range(0,r):
        row = [int(num) for num in infile.readline().split()]
        matrix.append(row)
    lds = solve(matrix)
    solnList.append([line[0],lds])
for i in range(0,len(solnList)):
    print(solnList[i][0]+": "+str(solnList[i][1]))
