num = int(input("Enter a number: "))
is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1
print("Prime" if is_prime else "Not Prime")
