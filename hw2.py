import sys

infile = open(sys.argv[1],"r")
numRooms = int(infile.readline())
arr=[];
for x in range(0,numRooms):
    temp=infile.readline().split()
    temp=list(map(int,temp))
    arr.append(temp)
# Sort by increasing initial capacity
for x in range(numRooms-1,0,-1):
    for i in range(x):
        if(arr[i][0]>arr[i+1][0]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
trailer=0
delta=0
for x in range(0,numRooms):
    if(arr[x][1]>=arr[x][0]):
        if(arr[x][0]>(delta)):
            trailer+=arr[x][0]-(delta)
            delta+=arr[x][0]-(delta)
            delta+=arr[x][1]-arr[x][0]
        else:
            delta+=arr[x][1]-arr[x][0]
#Sort by increasing final capacity
for x in range(numRooms-1,0,-1):
    for i in range(x):
        if(arr[i][1]>arr[i+1][1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
for x in range(numRooms-1,-1,-1):
    if(arr[x][1]<arr[x][0]):
        if(arr[x][0]>(delta)):
            trailer+=arr[x][0]-(delta)
            delta-=arr[x][0]-arr[x][1]
        else:
            delta+=arr[x][1]-arr[x][0]
print(trailer)
