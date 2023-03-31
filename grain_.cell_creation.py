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


print(pts_1[3])
print(pts_2[3])                                 # 4th pt in file is [0.5,0.5,0.5]
print(np.dot([0.5,0.5,0.5],transf_1))            # we take centre of grain [0.5,0.5,0.5]in old basis as new origin

origin = pts_2[3]
# shift origin

pts_3 = []
for pts in pts_2:
    pts_3.append(np.subtract(pts, origin))
 

# rotate the mother grain by specified angle

theta = 20
theta_rad = (theta*math.pi)/180
pts_4 = []
rot_mat = [[math.cos(theta_rad),math.sin(theta_rad),0],[-math.sin(theta_rad),math.cos(theta_rad),0],[0, 0, 1]]

for pts in pts_3:
    pts_4.append(np.dot(pts, rot_mat))
    
# window to select atoms within window boundaries
# how to decide window dimensions - selecting ) .25 to -0.25 in xy dir 
# decide whether edges are zig zag or arm chair - change window boundaries by sqrt((2.46)^2 + (1.23)^2)

# for arm chair

pts_mask = []
for pts in pts_4:
    if pts[0] < 4.42 and pts[0] > -4.92:               # 4.92 = 73.8/15
        if pts[1] < 4.92 and pts[1] > -7.76:           # 0.5 got removed drom 4.92 to 4.42 as one atom extra atom was included
            pts_mask.append(np.add(pts,[9.84, 0, 5]))

pts_0deg = []
for pts in pts_3:
    if pts[0] < 4.42 and pts[0] > -4.92:
        if pts[1] < 4.92 and pts[1] > -7.76:
            pts_0deg.append(np.add(pts,[0, 0, 5]))


    

# placing rotated, 0 deg grains next to each other
pts_final_1 = []
for pts in pts_0deg:                                  
    pts_final_1.append(pts)

for pts in pts_mask:
    pts_final_1.append(pts)


# origin shift back to corner for clean look
pts_final = []
for pts in pts_final_1:
    pts_final.append(np.add(pts,[4.92,7.76,0]))

    
# creating content to fill in arm chair .cell file
wrt = []
wrt.append('%BLOCK LATTICE_CART\n')
wrt.append('    20.18     0       0.000000000000000\n')
wrt.append('    0     12.78       0.000000000000000\n')    #
wrt.append('    0     0       10.000000000000000\n')
wrt.append('%ENDBLOCK LATTICE_CART\n')
wrt.append('%BLOCK POSITIONS_FRAC\n')
for pts in pts_final:
    pts_1 = []
    for i in range(3):
        if i == 0:
            pts_1.append(str(pts[i]/20.18))
        if i == 1:
            pts_1.append(str(pts[i]/12.78))
        if i == 2:
            pts_1.append(str(pts[i]/10))
    wrt.append('  ' + 'C' + '   ' + '   '.join(pts_1) + '\n')
print(wrt)
wrt.append('%ENDBLOCK POSITIONS_FRAC\n')

# arm chair .cell file
with open(r'20deg_ac.cell', 'w') as fp:
    for item in wrt:
        fp.write("%s" % item)       
    fp.close()






# for zig zag

ninety_rot = [[0, 1, 0],[-1, 0, 0],[0, 0, 1]]
pts_mask_zz = []
pts_mask_zz_1 = []
pts_0deg_zz = []
for pts in pts_mask:
    pts_mask_zz.append(np.add(pts,[-9.84, -13.2, 0]))
for pts in pts_mask_zz:
    pts_mask_zz_1.append(np.dot(pts,ninety_rot))
for pts in pts_0deg:
    pts_0deg_zz.append(np.dot(pts,ninety_rot))




# placing rotated, 0 deg grains next to each other
pts_final_zz_1 = []
for pts in pts_0deg_zz:                                  
    pts_final_zz_1.append(pts)

for pts in pts_mask_zz_1:
    pts_final_zz_1.append(pts)


# origin shift back to corner for clean look
pts_final_zz = []
for pts in pts_final_zz_1:
    pts_final_zz.append(np.add(pts,[4.26,4.92,0]))

# creating content to fill in zig zag .cell file
wrt = []
wrt.append('%BLOCK LATTICE_CART\n')
wrt.append('    26.36     0       0.000000000000000\n')
wrt.append('    0     9.84       0.000000000000000\n')    # recalculate for zig zag as we place 2 grains togethher
wrt.append('    0     0       10.000000000000000\n')
wrt.append('%ENDBLOCK LATTICE_CART\n')
wrt.append('%BLOCK POSITIONS_FRAC\n')
for pts in pts_final_zz:
    pts_1 = []
    for i in range(3):
        if i == 0:
            pts_1.append(str(pts[i]/26.36))
        if i == 1:
            pts_1.append(str(pts[i]/9.84))
        if i == 2:
            pts_1.append(str(pts[i]/10))
    wrt.append('  ' + 'C' + '   ' + '   '.join(pts_1) + '\n')
print(wrt)
wrt.append('%ENDBLOCK POSITIONS_FRAC\n')

# zig zag .cell file
with open(r'20deg_zz.cell', 'w') as fp:
    for item in wrt:
        fp.write("%s" % item)       
    fp.close()
    
# 
