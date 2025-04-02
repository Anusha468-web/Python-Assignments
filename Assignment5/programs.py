#prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n//2) + 1):
        if n % i == 0:
            return False
    return True
#Factorial 
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# sum of digits
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

#Reverse a Number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev* 10 + n % 10
        n //= 10
    return rev

# Palindrome Number
def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    return original == reverse

# Armstrong Number 
def is_armstrong(n):
    digits = 0
    temp = n
    while temp > 0:
        digits += 1
        temp //= 10
    total = 0
    temp = n
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    
    return total == n

#Perfect number
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
