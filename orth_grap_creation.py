import numpy as np
import math
rd = open("mother grap.txt",'r')  # read mother grain
x = rd.readlines()

n,m = len(x),3
pts_1 = [[0 for i in range(m)] for j in range(n)]   # generate nx3 matrx

# a = 73.8 A b = 73.8 A c = 10 A
i = 0
for line1 in x:
    line2 = line1.split()
    for j in range(3):
        if j == 0:
            pts_1[i][j] = 73.8*float(line2[j+1])    # each point place in nx3 matrix
        if j == 1:
            pts_1[i][j] = 73.8*float(line2[j+1])
        if j == 2:
            pts_1[i][j] = 10*float(line2[j+1])
    i = i + 1


#first we make axes orthogonal by transforming all lattice pts to orthogonal basis


transf_1 = [[-math.cos(math.pi/3), math.cos(math.pi/6), 0],[1, 0, 0],[ 0, 0, 1]]
print(transf_1)

pts_2 = []

for line1 in pts_1:
    pts_2.append(np.dot(line1,transf_1))


pts_mask = []
for pts in pts_2:
    if pts[0] < 13.54 and pts[0] > -0.5:               
        if pts[1] < 16.5:           
            pts_mask.append(pts)

# creating content to fill in .cell file
wrt = []
wrt.append('%BLOCK LATTICE_CART\n')
wrt.append('    14.76     0       0.000000000000000\n')
wrt.append('    0     17.04       0.000000000000000\n')    #
wrt.append('    0     0       10.000000000000000\n')
wrt.append('%ENDBLOCK LATTICE_CART\n')
wrt.append('%BLOCK POSITIONS_FRAC\n')
for pts in pts_mask:
    pts_1 = []
    for i in range(3):
        if i == 0:
            pts_1.append(str(pts[i]/14.76))
        if i == 1:
            pts_1.append(str(pts[i]/17.04))
        if i == 2:
            pts_1.append(str(pts[i]/10))
    wrt.append('  ' + 'C' + '   ' + '   '.join(pts_1) + '\n')
print(wrt)
wrt.append('%ENDBLOCK POSITIONS_FRAC\n')

# .cell file
with open(r'orth_pg.cell', 'w') as fp:
    for item in wrt:
        fp.write("%s" % item)       
    fp.close()
