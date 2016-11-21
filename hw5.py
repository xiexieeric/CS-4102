import sys
def findAugPath(p,visited):
    visiting = p[-1]
    if(visiting=="happystudents"):
        return p
    for edge in nodes[visiting].keys():
        if nodes[visiting][edge]>0 and not visited.get(edge):
            p.append(edge)
            visited[edge]=True
            val=findAugPath(p,visited)
            if val:
                return p
            else:
                p.pop()
    return False
def solve():
    visited={}
    visited["flockofstudents"]=True
    p=findAugPath(["flockofstudents"],visited)
    while(p):
        for i in range(0,len(p)-1):
            if i==0:
                nodes["flockofstudents"][p[i+1]]-=1
            elif i==len(p)-2:
                nodes[p[i]]["happystudents"]-=1
            else:
                nodes[p[i]][p[i+1]]-=1
                nodes[p[i+1]][p[i]]+=1
        #print(p)
        #for node in nodes.keys():
        #    print(node,nodes[node])
        #print("\n")
        visited={}
        visited["flockofstudents"]=True
        p=findAugPath(["flockofstudents"],visited)
def verify():
    valid = True
    for edge in nodes["flockofstudents"].keys():
        if nodes["flockofstudents"][edge]>0:
            valid=False
    return valid

#Read in File, split into cases
f = open(sys.argv[1],"r")
content = f.readlines()
cases=[]
case=[]
for s in content:
    s=s.strip()
    if s=="0 0 0":
        break
    elif len(s.split())==3:
        case = []
        case.append(s)
    if not s:
        cases.append(case)
    if len(s.split())==2:
        case.append(s)
#Process Each Case into adjacency lists
for case in cases:
    firstLine = case[0].split(" ")
    r = int(firstLine[0])
    c = int(firstLine[1])
    n = int(firstLine[2])
    nodes = {}
    nodes["flockofstudents"]={}
    for i in range(1,r+1):
          temp = case[i].split()
          if not nodes.get(temp[0]):
              nodes[temp[0]]={}
              nodes["flockofstudents"][temp[0]]=n
          nodes[temp[0]][temp[1]]=1
          if not nodes.get(temp[1]):
              nodes[temp[1]]={}
          nodes[temp[1]][temp[0]]=0
    for i in range(r+1,r+1+c):
        temp = case[i].split()
        #sinkEdge = [int(temp[1]),True]
        nodes[temp[0]]["happystudents"]= int(temp[1])
    solve()
    if verify():
        print("Yes")
    else:
        print("No")
