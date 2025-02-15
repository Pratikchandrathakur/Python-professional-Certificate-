# Python code​​​​​​‌‌​​‌​‌​‌​‌‌‌​​​‌​‌‌​‌​​‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    # Return an empty list for numbers less than 2
    if num < 2:
        return []
    
    # Create a boolean array to represent primality
    primes = [True] * num
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    # Implement the Sieve of Eratosthenes
    for i in range(2, int(num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, num, i):
                primes[j] = False

    # Collect all prime numbers
    return [i for i in range(num) if primes[i]]

# Example usage
result = allPrimesUpTo(20)
print(result)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
pass
