import random
outfile = open("testfile.txt","w")
outfile.write("1\n")
outfile.write("Test 20 20\n")
lst = []
for i in range(0,500):
    row=[]
    for j in range(0,500):
        r = random.randint(0,100)
        row.append(r)
        outfile.write(str(r)+" ")
    lst.append(row)
    outfile.write("\n")
outfile.write(str(lst))
