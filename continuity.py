import matplotlib.pyplot as plt

# Define the binary chop sequence
sequence = [
    '0.1',
    '0.01', '0.11',
    '0.001',  '0.011', '0.101', '0.111',
    '0.0001', '0.0011', '0.0101', '0.0111', '0.1001',  '0.1011','0.1101', '0.1111',
    '0.00001', '0.00011', '0.00101', '0.00111', '0.01001', '0.01011', '0.01101', '0.01111', '0.10001', '0.10011', '0.10101', '0.10111', '0.11001', '0.11011', '0.11101', '0.11111'
]

# Define the x positions for each level
x_positions = [int(binary.split('.')[1], 2) / (2**len(binary.split('.')[1])) for binary in sequence]

# Define the y positions for each level
y_positions = []
current_level = 1
for binary in sequence:
    level = len(binary.split('.')[1])
    if level > current_level:
        current_level = level
    y_positions.append(9 - current_level)

# Plotting
plt.figure(figsize=(12, 8))
plt.scatter(x_positions, y_positions, color='blue')
for i, (x, y, binary) in enumerate(zip(x_positions, y_positions, sequence), start=1):
    plt.text(x, y + 0.15, str(i), ha='center', va='bottom', fontsize=8)
    plt.text(x, y - 0.15, binary, ha='center', va='top', fontsize=8)

# Adding labels for the x-axis
plt.xticks([i/8 for i in range(9)], ['0', '1/8', '1/4', '3/8', '1/2', '5/8', '3/4', '7/8', '1'])
plt.yticks([])

# Add extra rows with ... and <1|0>
plt.text(0, 8.5, 'Discreteness', ha='left', fontsize=12)
plt.text(0.5, 3, '...', ha='center', fontsize=20)
plt.text(0.5, 2, '<1|0>', ha='center', fontsize=12)
plt.text(0, 2, 'Uncertainty', ha='left', fontsize=12)
plt.text(0, 0.5, 'Continuity', ha='left', fontsize=12)


# Draw solid blue line from 0 to 1
plt.plot([0, 1], [1, 1], 'b-', linewidth=4)
plt.title('Counting [0,1]', ha='center', fontsize=16)
plt.xlabel('Number')
plt.ylabel('Bicimal Precision')
plt.ylim(0, 9)
plt.savefig('continuity.png')
plt.show()



