# Python code​​​​​​‌‌​​‌​‌‌​​‌​​‌‌‌‌‌‌‌​​​‌​ below
def triangle(num):
    """Returns the triangular number for the given num."""
    return (num * (num + 1)) // 2  # Formula for triangular numbers

def square(num):
    """Returns the square of a number using only the triangle function."""
    if num == 1:
        return 1  # Special case for 1 (edge case)
    return triangle(num) + triangle(num - 1)

# Testing the function
print(square(1))  # Output: 1
print(square(2))  # Output: 4
print(square(3))  # Output: 9
print(square(4))  # Output: 16
print(square(5))  # Output: 25
pass
