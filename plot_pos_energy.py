import matplotlib.pyplot as plt

rd = open("Pos_Energy_1.txt",'r')
x = rd.readlines()

x_cor = []
E = []
for line1 in x:
    line2 = line1.split()
    x_cor.append(float(line2[0]))
    E.append(float(line2[3]))

rd.close()

print(x_cor)
print(E)
plt.plot(x_cor, E)
plt.show()

    
