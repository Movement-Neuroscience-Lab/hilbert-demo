import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Enable Tex rendering in matplotlib
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Main function
def main():
    # Create argument parser to parse filename
    parser = argparse.ArgumentParser(description='Script to plot HT data')
    parser.add_argument('filename', help='Name of file with HT data.')
    args = parser.parse_args()
    filename = args.filename

    # Initialize lists to store data
    real_nums_preHT = []
    real_nums_postHT = []
    imag_nums_postHT = []
    phase_data = []

    # Read data from HT output file
    with open(filename, 'r') as file:
        lines = file.readlines()
        # number of samples
        n = int(lines[0])
        
        # Split the data into two sections
        preHT_lines = lines[1:n+1]
        postHT_lines = lines[n+1:2*n+1]
        phase_lines = lines[2*n+1:3*n+1]
        
        # Process Pre-HT
        for line in preHT_lines:
            parts = line.split()
            index = int(parts[0])
            real_num = float(parts[1])
            real_nums_preHT.append(real_num)
        
        # Process Post-HT
        for line in postHT_lines:
            parts = line.split()
            index = int(parts[0])
            real_num = float(parts[1])
            imag_num = float(parts[2])
            real_nums_postHT.append(real_num)
            imag_nums_postHT.append(imag_num)

        # Process phase data 
        for line in phase_lines:
            parts = line.split()
            index = int(parts[0])
            phase = float(parts[1])
            phase_data.append(phase)

    # Plotting in 3D
    fig = plt.figure(figsize=(14, 7))

    # 3D Plot for Pre-HT
    ax1 = fig.add_subplot(121)
    ax1.scatter(range(n), real_nums_preHT, c='blue', label=(r'$x(t)$'))
    ax1.set_xlabel(r'Index ($t$)')
    ax1.set_ylabel(r'Real Number ($x(t)$)')
    ax1.set_title('Original signal')
    ax1.legend()

    # 3D Plot for Post-HT
    # ax2 = fig.add_subplot(122, projection='3d')
    # ax2.scatter(range(n), real_nums_postHT, imag_nums_postHT, c='red', label=(r'$H[x(t)]$'))
    # ax2.set_xlabel(r'Index ($t$)')
    # ax2.set_ylabel(r'Real Number ($H[x(t)]$)')
    # ax2.set_zlabel(r'Imaginary Number ($iH[x(t)]$)')
    # ax2.set_title('Hilbert transform')
    # ax2.legend()

    # 2D Plot for Analytic
    ax2 = fig.add_subplot(122)
    ax2.scatter(range(n), phase_data, c='red', label=(r'$\phi (t)$'))
    ax2.set_xlabel(r'Index ($t$)')
    ax2.set_ylabel(r'Phase ($\phi (t)$)')
    ax2.set_title('Phase of signal')
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
