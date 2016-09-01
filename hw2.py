import sys

infile = open(sys.argv[1],"r")
numRooms = int(infile.readline())
arr=[];
for x in range(0,numRooms):
    arr.append(infile.readline().split())
arr=sorted(arr)
trailer=0
delta=0
print(arr)
for x in range(0,numRooms):
    if(arr[x][1]>=arr[x][0]):
        delta-=int(arr[x][0])
        if(delta<0):
            trailer-=delta
        delta+=int(arr[x][1])
arr=sorted(arr, key = lambda x: int(x[1]))
for x in range(numRooms,0):
    if(arr[x][1]<arr[x][0]):
        delta-=int(arr[x][0])
        if(delta<0):
            trailer-=delta
        delta+=int(arr[x][1])
if(delta<0):
    trailer+=delta
print(trailer)
