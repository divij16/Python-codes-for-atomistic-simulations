import subprocess
import time
import math
import numpy as np
import matplotlib.pyplot as plt

rd1 = open(r"21.8g_ac_2.cell", 'r')
x_init = rd1.readlines()           # read lines corresponding to position of H2 atoms
rd1.close()

print(x_init)
# lattice vectors
a = x_init[1].split()
b = x_init[2].split()
c = x_init[3].split()

for i in range(3):
    a[i] = float(a[i])
    b[i] = float(b[i])
    c[i] = float(c[i])
print(a)
print(b)
print(c)
a_0 = math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)
b_0 = math.sqrt(b[0]**2 + b[1]**2 + b[2]**2)
c_0 = math.sqrt(c[0]**2 + c[1]**2 + c[2]**2)
print(a_0)
print(b_0)
print(c_0)
# point around which atoms are removed
defect_size = 1 + 1.1                       # defect dia 8A + hydrogen ended pore edge 1.1A
x_ref = [0,0,0]
step =  (b_0 - defect_size)/(9*b_0)             
print(step)

for j in range(10) :
    rd1 = open(r"21.8g_ac_2.cell", 'r')
    x_final = rd1.readlines()           # read lines corresponding to position of atoms
    rd1.close()
    print(len(x_final))
    x_ref[0] = 0.45*a[0] + ((9.1/(2*b_0)) + 5*step)*b[0] +0.5*c[0]
    x_ref[1] = 0.45*a[1] + ((9.1/(2*b_0)) + 5*step)*b[1] +0.5*c[1]                 
    x_ref[2] = 0.45*a[2] + ((9.1/(2*b_0)) + 5*step)*b[2] +0.5*c[2]
    x_ref = [14.812287967416829, 6.70734669434362, 7.499999972309642]
    print(x_ref)
    x = []
    x_real = [0,0,0]
    count = 0
    for i in range(len(x_init)) :
        
        x = x_init[i + 7].split()
        if x[0] != 'C' :
            break
        x[1] = float(x[1])
        x[2] = float(x[2])
        x[3] = float(x[3])
        x_real[0] = x[1]*a[0] + x[2]*b[0] +x[3]*c[0]
        x_real[1] = x[1]*a[1] + x[2]*b[1] +x[3]*c[1]
        x_real[2] = x[1]*a[2] + x[2]*b[2] +x[3]*c[2]
        d = math.sqrt((x_real[0] - x_ref[0])**2 + (x_real[1] - x_ref[1])**2 )
#        print(d)
        if d <= (defect_size/2) :                                    
            x_final[i+7] = 'asdfghjkl'
            count = count + 1
    print(count)
    defect_size = defect_size + 1
    for i in range(count):
        x_final.remove('asdfghjkl')
        
    if j == 0 :
        with open(r'21.8_6_1A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 1 :
        with open(r'21.8_6_2A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 2 :
        with open(r'21.8_6_3A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 3 :
        with open(r'21.8_6_4A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 4 :
        with open(r'21.8_6_5A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 5 :
        with open(r'21.8_6_6A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j ==6 :
        with open(r'21.8_6_7A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 7 :
        with open(r'21.8_6_8A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 8 :
        with open(r'21.8_6_9A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()

    if j == 9 :
        with open(r'21.8_6_10A.cell', 'w') as fp:
            for item in x_final:
                fp.write("%s" % item)       # document is modified
        fp.close()


