import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = 'output.txt'

# Initialize lists to store data
indices = []
real_nums_preHT = []
imag_nums_preHT = []
real_nums_postHT = []
imag_nums_postHT = []
analytic_signal = []

# Read data from the file
with open(filename, 'r') as file:
    lines = file.readlines()
    # number of samples
    n = int(lines[0])
    
    # Split the data into two sections
    preHT_lines = lines[1:n+1]
    postHT_lines = lines[n+1:2*n+1]
    analytic_lines = lines[2*n+1:3*n+1]
    
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

    # Process Analytic Signal
    for line in analytic_lines:
        parts = line.split()
        index = int(parts[0])
        real_num = float(parts[1])
        analytic_signal.append(real_num)

# Plotting in 3D
fig = plt.figure(figsize=(14, 7))

# 3D Plot for Pre-HT
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(range(n), real_nums_preHT, imag_nums_preHT, c='blue', label='Pre-HT')
ax1.set_xlabel('Index')
ax1.set_ylabel('Real Number')
ax1.set_zlabel('Imaginary Number')
ax1.set_title('Pre-HT')
ax1.legend()

# 3D Plot for Post-HT
# ax2 = fig.add_subplot(122, projection='3d')
# x2.scatter(range(n), real_nums_postHT, imag_nums_postHT, c='red', label='Post-HT')
# x2.set_xlabel('Index')
# x2.set_ylabel('Real Number')
# x2.set_zlabel('Imaginary Number')
# x2.set_title('Post-HT')
# x2.legend()

# 2D Plot for Analytic
ax2 = fig.add_subplot(122)
ax2.scatter(range(n), analytic_signal, c='red', label='Analytic Signal')
ax2.set_xlabel('Index')
ax2.set_ylabel('Real Number')
ax2.set_title('Analytic Signal')
ax2.legend()


plt.tight_layout()
plt.show()
