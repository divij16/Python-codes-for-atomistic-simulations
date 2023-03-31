import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

rd1 = open(r"h2pg.cell", 'r')
x_init = rd1.readlines()           # read lines corresponding to position of H2 atoms
rd1.close()

rd2 = open(r"h2pg.cell", 'r')
x = rd2.readlines()           # read lines corresponding to position of H2 atoms
rd2.close() 

y0 = ['0','0','0','0']
x_cor = []
y_cor = []
e_f_list = []


            
i = 0
while i < 40 and float(y0[3]) > -0.4 and float(y0[3]) < 0.41 :                       # 8/0.2 = 40 points along z

    # test.py
    subprocess.call(["./RunCASTEP.sh -np 8 -nt 1 -q low H2G_1"],shell=True)

    # test2.py
    run = 0
    while True:
        check = subprocess.check_output(["qstat -u phm212508"],shell=True)          # capture output of command
        check = check.split()
        if len(check) != 0 and check[-2] == 'R' and run == 0:
                print('running now')
                run = 1
        if len(check) != 0 and (check[-2] == 'Q' or check[-2] == 'R'):
                time.sleep(5)
                continue
        else:
                print('Done!')
                break

    # test3.py
    rd_out = open(r"h2pg.castep", 'r')
    castep_out = rd_out.readlines()                    # open and read output file
    rd_out.close()
        
    castep_out_1 = []
    for line1 in castep_out:                          # take each line split them into words 
            line2 = line1.split()
            for line3 in line2:                       # add each word as a new string in list
                    castep_out_1.append(line3)
    #print(castep_out_1)

    count = 0 
    E_f = 0
    for word in castep_out_1:                                   # search for 'Final energy =' to get total energy value
            if word == 'Final':
                    if castep_out_1[count+1] == 'energy':
                            E_f = float(castep_out_1[count+3])
            count = count + 1

    if E_f == 0:
            print('did not converge, current total energy = ')
            count = 0
            E_f = 0
            for word in castep_out_1:                                   # search for 'Final energy =' to get total energy value
                if word == 'Current':
                    if castep_out_1[count+1] == 'total':
                        if castep_out_1[count+2] == 'energy':
                            E_f = float(castep_out_1[count+4])
                count = count + 1
    print(E_f)

    pos_energy_str = []
    pos_energy_str.append(str(float(y0[1])*12.3))
    pos_energy_str.append(str(float(y0[2])*12.3))
    pos_energy_str.append(str(float(y0[3])*10))
    pos_energy_str.append(str(E_f))
    pos_energy_str = '	'.join(pos_energy_str) + '\n'
    wrt_out = open("Pos_Energy.txt", 'a')
    wrt_out.write(pos_energy_str)                               # fills up text file with position and energy
    wrt_out.close()


    x_cor.append(float(y0[1])*17.375604)                       # create lists for plot 
    y_cor.append(float(y0[2])*10.36)
    e_f_list.append(E_f)

    subprocess.call(["rm -v !(*.cell|*.param|*.sh|*.py|*.txt)"],shell=True)

    y0 = x[-3].split()               # line to words
    y1 = x[-2].split()
    print(y0)
    print(y1)

    y0[3] = str(float(y0[3])-0.02)   # H2 molecule displaced by 0.2A along x dir
    y1[3] = str(float(y1[3])-0.02)   # 0.2A in frac = .2/10 = 0.02
    print(y0)
    print(y1)
    x[-3] = '  ' + '   '.join(y0) + '\n'           # words to line
    x[-2] = '  ' + '   '.join(y1) + '\n'         # x has been replaced with modified coordinates
    
    with open(r'h2pg.cell', 'w') as fp:
        for item in x:
            fp.write("%s" % item)       # document is modified
    fp.close()
    i = i+1;
        

plt.plot(x_cor, e_f_list)
plt.show()
fp = open(r'h2pg.cell', 'w')
for item in x_init:
    fp.write("%s" % item)       # document is reset to initial values
fp.close()
            
