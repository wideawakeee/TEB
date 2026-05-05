def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

# Input number
n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a Prime Number")
else:
    print(n, "is NOT a Prime Number")
