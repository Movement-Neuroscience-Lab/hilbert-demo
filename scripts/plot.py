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
    real_phase_data = []

    # Read data from HT output file
    with open(filename, 'r') as file:
        lines = file.readlines()
        # number of samples
        n = int(lines[0])
        
        # Split the data into two sections
        preHT_lines = lines[1:n+1]
        postHT_lines = lines[n+1:2*n+1]
        phase_lines = lines[2*n+1:3*n+1]
        real_phase_lines = lines[3*n+1:4*n+1]
        
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

        # Process calculated phase data 
        for line in phase_lines:
            parts = line.split()
            index = int(parts[0])
            phase = float(parts[1])
            phase_data.append(phase)

        # Process real phase data 
        for line in real_phase_lines:
            parts = line.split()
            index = int(parts[0])
            phase = float(parts[1])
            real_phase_data.append(phase)

    # Plotting
    fig = plt.figure(figsize=(15,10))

    # 3D Plot for Pre-HT
    ax0 = fig.add_subplot(221)
    ax0.plot(range(n), real_nums_preHT, c='blue', label=(r'$x(t)$'))
    ax0.set_xlabel(r'Index ($t$)')
    ax0.set_ylabel(r'Real Number ($x(t)$)')
    ax0.set_title('Original signal')
    ax0.legend()

    # 3D Plot for Post-HT
    ax1 = fig.add_subplot(222, projection='3d')
    ax1.plot(range(n), real_nums_postHT, imag_nums_postHT, c='red', label=(r'$H[x(t)]$'))
    ax1.set_xlabel(r'Index ($t$)')
    ax1.set_ylabel(r'Re')
    ax1.set_zlabel(r'Im')
    ax1.set_title('Hilbert transform')
    ax1.legend()

    # 2D Plot for calculated phase 
    ax2 = fig.add_subplot(223)
    ax2.plot(range(n), phase_data, c='purple', label=(r'$\phi (t)$'))
    ax2.set_xlabel(r'Index ($t$)')
    ax2.set_ylabel(r'Phase in radians ($\phi (t)$)')
    ax2.set_title('Calculated phase of signal')
    ax2.legend()

    # 2D Plot for real phase
    ax3 = fig.add_subplot(224)
    ax3.plot(range(n), real_phase_data, c='green', label=(r'$\phi (t)$'))
    ax3.set_xlabel(r'Index ($t$)')
    ax3.set_ylabel(r'Phase in radians ($\phi (t)$)')
    ax3.set_title('Real phase of signal')
    ax3.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
