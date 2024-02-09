def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

ll = int(input("Enter lower limit of the range: "))
ul = int(input("Enter upper limit of the range: "))

prime_numbers = []

for num in range(ll, ul + 1):
    if is_prime(num):
        prime_numbers.append(num)

if prime_numbers:
    print("Prime numbers between", ll, "and", ul, "are:")
    print(prime_numbers)
else:
    print("There are no prime numbers between", ll, "and", ul)
