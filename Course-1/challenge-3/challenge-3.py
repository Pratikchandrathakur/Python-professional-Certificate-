# Python code​​​​​​‌‌​​‌​‌​​‌‌‌​‌​​​​​​‌​‌‌‌ below

def run_length_encode(s):
    if not s:
        return []  # Return an empty list for an empty string

    encoded = []  # List to store the result
    count = 1     # Initialize count of current character

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increment count if the current character matches the previous one
        else:
            encoded.append((s[i - 1], count))  # Append the character and its count
            count = 1  # Reset count for the new character

    # Append the last character and its count
    encoded.append((s[-1], count))

    return encoded

# Example usage
input_string = 'AAAAABBBBAAA'
encoded_string = run_length_encode(input_string)
print(encoded_string)  # Output: [('A', 5), ('B', 4), ('A', 3)]
def run_length_decode(encoded):
    decoded = []  # List to store the decoded characters

    # Iterate through each tuple in the encoded list
    for char, count in encoded:
        decoded.append(char * count)  # Append the character repeated 'count' times

    # Join the list into a single string
    return ''.join(decoded)

# Example usage
encoded_string = [('A', 5), ('B', 4), ('A', 3)]
decoded_string = run_length_decode(encoded_string)
print(decoded_string)  # Output: 'AAAAABBBBAAA'
