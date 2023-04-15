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

theta = 13.2
theta_rad = (theta*math.pi)/180
pts_4 = []
pts_5 = []
rot_mat_1 = [[math.cos(theta_rad/2),math.sin(theta_rad/2),0],[-math.sin(theta_rad/2),math.cos(theta_rad/2),0],[0, 0, 1]]
rot_mat_2 = [[math.cos(-theta_rad/2),math.sin(-theta_rad/2),0],[-math.sin(-theta_rad/2),math.cos(-theta_rad/2),0],[0, 0, 1]]

for pts in pts_3:
    pts_4.append(np.subtract(np.dot(pts, rot_mat_1),[0, 0, 0])) # for alignment of 0deg and 60deg grain to get prisgrap whwn placed together
                                                                        
for pts in pts_3:
    pts_5.append(np.subtract(np.dot(pts, rot_mat_2),[0, 0, 0]))
    
# window to select atoms within window boundaries
# how to decide window dimensions - selecting ) .25 to -0.25 in xy dir 
# decide whether edges are zig zag or arm chair - change window boundaries by sqrt((2.46)^2 + (1.23)^2)

# for arm chair

pts_mask_ac = []
for pts in pts_5:
    if pts[0] < (15.4) and pts[0] > -0.01:               # 2.46*5 = 12.3, take 15.4 for all
        if pts[1] < 10.72 and pts[1] > -0.01:       # 12d = 10.72, 14d = 10.72, 21.8d = 6.51, 30d = 8.87, 32.2d = 8.87, 38.2d = 11.27, 42.1d = 13.7
            pts_mask_ac.append(np.add(pts,[17.4, 0, 7.5]))  # xshift = 15.4 + 2  # .73 along x for proper bonding of 60 deg with 0 deg grains 

pts_0deg_ac = []
for pts in pts_4:
    if pts[0] < 15.4 and pts[0] > -0.01:
        if pts[1] < 10.72 and pts[1] > -0.01:
            pts_0deg_ac.append(np.add(pts,[0, 0, 7.5]))


    

# placing rotated, 0 deg grains next to each other
pts_final_1 = []
for pts in pts_0deg_ac:                                  
    pts_final_1.append(pts)

for pts in pts_mask_ac:
    pts_final_1.append(pts)


# origin shift back to corner for clean look
pts_final = []
for pts in pts_final_1:
    pts_final.append(np.add(pts,[0, 0, 0]))

    
# creating content to fill in arm chair .cell file
wrt = []
wrt.append('%BLOCK LATTICE_CART\n')
wrt.append('    34.8     0       0.000000000000000\n')    # ((15.4+2)*2 = 34.8) - 1
wrt.append('    0     10.72       0.000000000000000\n')    # 24.85 + 0.71 = 25.56
wrt.append('    0     0       15.000000000000000\n')
wrt.append('%ENDBLOCK LATTICE_CART\n')
wrt.append('%BLOCK POSITIONS_FRAC\n')
for pts in pts_final:
    pts_1 = []
    for i in range(3):
        if i == 0:
            pts_1.append(str(pts[i]/34.8))
        if i == 1:
            pts_1.append(str(pts[i]/10.72))
        if i == 2:
            pts_1.append(str(pts[i]/15))
    wrt.append('  ' + 'C' + '   ' + '   '.join(pts_1) + '\n')
print(wrt)
wrt.append('%ENDBLOCK POSITIONS_FRAC\n')

# arm chair .cell file
with open(r'13.2deg_ac.cell', 'w') as fp:
    for item in wrt:
        fp.write("%s" % item)       
    fp.close()






# for zig zag

ninety_rot = [[0, 1, 0],[-1, 0, 0],[0, 0, 1]]
pts_6 = []
pts_7 = []
pts_8 = []

for pts in pts_3:
    pts_6.append(np.dot(pts, ninety_rot))
    
for pts in pts_6:
    pts_7.append(np.subtract(np.dot(pts, rot_mat_2),[0, 0, 0]))

for pts in pts_6:
    pts_8.append(np.subtract(np.dot(pts, rot_mat_1),[0, 0, 0]))
    
pts_mask_ac = []
for pts in pts_7:
    if pts[0] < (14.4) and pts[0] > -0.01:               # 4.26*2 + 2.84 = 11.36
        if pts[1] < 6.51 and pts[1] > -0.01:       # 12deg = 18.57, 14d = 16.13,21.8d = 11.27, 30d = 8.87, 32,2d = 15,36, 40d = 6.51
            pts_mask_ac.append(np.add(pts,[16.4, 0, 5]))  # xshift = 14.4 + 2 

pts_0deg_ac = []
for pts in pts_8:
    if pts[0] < 14.4 and pts[0] > -0.01:
        if pts[1] < 6.51 and pts[1] > -0.01:
            pts_0deg_ac.append(np.add(pts,[0, 0, 5]))


    

# placing rotated, 0 deg grains next to each other
pts_final_1 = []
for pts in pts_0deg_ac:                                  
    pts_final_1.append(pts)

for pts in pts_mask_ac:
    pts_final_1.append(pts)


# origin shift back to corner for clean look
pts_final = []
for pts in pts_final_1:
    pts_final.append(np.add(pts,[0, 0, 0]))

    
# creating content to fill in zig zag .cell file
wrt = []
wrt.append('%BLOCK LATTICE_CART\n')
wrt.append('    32.8     0       0.000000000000000\n')    # (14.4 + 2)*2 = 32.8 
wrt.append('    0     6.51       0.000000000000000\n')    # 2.46*10 = 24.6 +0.71
wrt.append('    0     0       10.000000000000000\n')
wrt.append('%ENDBLOCK LATTICE_CART\n')
wrt.append('%BLOCK POSITIONS_FRAC\n')
for pts in pts_final:
    pts_1 = []
    for i in range(3):
        if i == 0:
            pts_1.append(str(pts[i]/32.8))
        if i == 1:
            pts_1.append(str(pts[i]/6.51))
        if i == 2:
            pts_1.append(str(pts[i]/10))
    wrt.append('  ' + 'C' + '   ' + '   '.join(pts_1) + '\n')
print(wrt)
wrt.append('%ENDBLOCK POSITIONS_FRAC\n')

# zig zag .cell file
with open(r'13.2deg_zz.cell', 'w') as fp:
    for item in wrt:
        fp.write("%s" % item)       
    fp.close()
