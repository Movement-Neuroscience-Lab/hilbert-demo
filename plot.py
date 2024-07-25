import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = 'output.txt'

# Initialize lists to store data
indices = []
real_nums_preHT = []
imag_nums_preHT = []
real_nums_postHT = []
imag_nums_postHT = []

# Read data from the file
with open(filename, 'r') as file:
    lines = file.readlines()
    
    # Split the data into two sections
    preHT_lines = lines[:256]
    postHT_lines = lines[256:512]
    
    # Process Pre-HT
    for line in preHT_lines:
        parts = line.split()
        index = int(parts[0])
        real_num = float(parts[1])
        imag_num = float(parts[2])
        indices.append(index)
        real_nums_preHT.append(real_num)
        imag_nums_preHT.append(imag_num)
    
    # Process Post-HT
    for line in postHT_lines:
        parts = line.split()
        index = int(parts[0])
        real_num = float(parts[1])
        imag_num = float(parts[2])
        real_nums_postHT.append(real_num)
        imag_nums_postHT.append(imag_num)

# Plotting in 3D
fig = plt.figure(figsize=(14, 7))

# 3D Plot for Pre-HT
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(range(256), real_nums_preHT, imag_nums_preHT, c='blue', label='Pre-HT')
ax1.set_xlabel('Index')
ax1.set_ylabel('Real Number')
ax1.set_zlabel('Imaginary Number')
ax1.set_title('Pre-HT')
ax1.legend()

# 3D Plot for Post-HT
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(range(256), real_nums_postHT, imag_nums_postHT, c='red', label='Post-HT')
ax2.set_xlabel('Index')
ax2.set_ylabel('Real Number')
ax2.set_zlabel('Imaginary Number')
ax2.set_title('Post-HT')
ax2.legend()

plt.tight_layout()
plt.show()
