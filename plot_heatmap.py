import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rd = open("Pos_Energy_heatmap.txt",'r')
x = rd.readlines()

E_1 = []
for line1 in x:
    line2 = line1.split()
    E_1.append(float(line2[3]))
print(E_1)

w, h = 22, 14
E_2 = [[0 for x in range(w)] for y in range(h)]
k = 0
for i in range(14):
        for j in range(22):
            E_2[i][j] = E_1[k]
            k = k + 1

print(E_2)

col = [str((0.14878 + i*0.01626)*12.3) for i in range(22)]
index = [str((0.54878 + i*0.01626)*12.3) for i in range(14)]

df = pd.DataFrame(E_2, columns = col, index = index)

#fig, ax = plt.subplots(figsize=(22,14))  
sns.heatmap(df, cmap ='viridis', linewidths = 0.0, annot = False)
plt.show()





#[str((0.5 + i*0.01626)*12.3) for i in range(22)]
#['6.15', '6.349998', '6.549996', '6.749994', '6.949992', '7.14999', '7.349988', '7.549986', '7.749984', '7.949982', '8.14998', '8.349978', '8.549976', '8.749974', '8.949972', '9.14997', '9.349968', '9.549966', '9.749964', '9.949962', '10.14996', '10.349958']
#>>> [str(0.5 + i*0.01626) for i in range(22)]
#['0.5', '0.51626', '0.53252', '0.54878', '0.56504', '0.5813', '0.59756', '0.61382', '0.63008', '0.64634', '0.6626', '0.67886', '0.69512', '0.71138', '0.72764', '0.7439', '0.76016', '0.77642', '0.79268', '0.80894', '0.8252', '0.84146']
#>>> [str(0.54878 + i*0.01626) for i in range(14)]
#['0.54878', '0.56504', '0.5813', '0.59756', '0.61382', '0.63008', '0.64634', '0.6626', '0.67886', '0.69512', '0.71138', '0.72764', '0.7439', '0.76016']
