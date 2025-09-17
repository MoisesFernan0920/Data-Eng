def getOneBits(n):
    # Convert to binary string without "0b" prefix
    bin_str = bin(n)[2:]
    # Positions are counted from left (MSB) to right (LSB), starting at 1
    positions = []
    for idx, bit in enumerate(bin_str):
        if bit == '1':
            # Position is (idx+1)
            positions.append(idx + 1)
    # Return: [number of 1s, pos1, pos2, ...]
    result = [len(positions)] + positions
    return result

# For testing:
if __name__ == '__main__':
    n = int(input())
    result = getOneBits(n)
    for x in result:
        print(x)