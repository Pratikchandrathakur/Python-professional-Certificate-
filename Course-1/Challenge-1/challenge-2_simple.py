# Python code below

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = hexNum.upper()  # Convert input to uppercase for uniformity
    result = 0
    length = len(hexNum)  # Get total length to calculate exponents
    index = 0  # Initialize index manually

    for digit in hexNum:  # Loop through digits
        if digit in hexNumbers:
            exponent = length - 1 - index  # Correct exponent calculation
            result += hexNumbers[digit] * (16 ** exponent)
            index += 1  # Manually increment index
        else:
            return None  # Return None if an invalid character is found

    return result  # Return the correct decimal result

# Example usage
print(hexToDec('2A'))  # Expected output: 42
print(hexToDec('FF'))  # Expected output: 255
print(hexToDec('10'))  # Expected output: 16
print(hexToDec('G1'))  # Expected output: None (invalid hex)
