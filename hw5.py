import sys
import time
def findAugPath(p):
    visiting = p[-1]
    if(visiting=="happystudents"):
        return p
    for edge in nodes[visiting].keys():
        if nodes[visiting][edge][0]>0 and edge not in p:
            p.append(edge)
            val=findAugPath(p)
            if val:
                return p
            else:
                p.pop()
    return False
def solve():
    p=findAugPath(["flockofstudents"])
    while(p):
        for i in range(0,len(p)-1):
            if i==0:
                nodes["flockofstudents"][p[i+1]][0]-=1
            elif i==len(p)-2:
                nodes[p[i]]["happystudents"][0]-=1
            else:
                nodes[p[i]][p[i+1]][0]-=1
                nodes[p[i+1]][p[i]][0]+=1
        #print(p)
        #for node in nodes.keys():
        #    print(node,nodes[node])
        #print("\n")
        p=findAugPath(["flockofstudents"])
def verify():
    valid = True
    for edge in nodes["flockofstudents"].keys():
        if nodes["flockofstudents"][edge][0]>0:
            valid=False
    return valid

#Read in File, split into cases
start_time=time.time()
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
              nodes["flockofstudents"][temp[0]]=[n,True]
          nodes[temp[0]][temp[1]]=[1,True]
          if not nodes.get(temp[1]):
              nodes[temp[1]]={}
          nodes[temp[1]][temp[0]]=[0,False]
    for i in range(r+1,r+1+c):
        temp = case[i].split()
        #sinkEdge = [int(temp[1]),True]
        nodes[temp[0]]["happystudents"]= [int(temp[1]),True]
    solve()
    if verify():
        print("Yes")
    else:
        print("No")
    print(time.time()-start_time)
