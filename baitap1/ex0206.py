inputstr = input("nhap x,y :")
dimensions = [int(x) for x in inputstr.split(',')]
rownum= dimensions[0];
colnum= dimensions[1];
multilist= [[0 for col in range(colnum)] for row in range (rownum)]
for row in range(rownum):
    for col in range(colnum):
        multilist[row][col]= row*col
print(multilist)        