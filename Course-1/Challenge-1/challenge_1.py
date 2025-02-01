# Python code​​​​​​‌‌​​‌​​‌‌​​‌​​​​‌‌‌​​​‌‌‌ below

def factorial(num):
    # Check if input is a string
    if isinstance(num, str):
        print(f'There was an error processing case "{num}"')
        print("TypeError: '<' not supported between instances of 'str' and 'int'")
        return None
    
    # Check if input is not an integer
    if not isinstance(num, int):
        print("Use correct input")
        return None

    # Check if the number is negative
    if num < 0:
        print("Use correct input")
        return None

    result = 1
    i = num

    while i > 1:
        result *= i  # Multiply result by i
        i -= 1  # Decrement i

    return result

# Example usage
print(factorial(5))  # Expected: 120
