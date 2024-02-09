def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = 0
composite_count = 0

while True:
    number = int(input("Enter a number (-1 to stop): "))
    
    if number == -1:
        break
    
    if is_prime(number):
        prime_count += 1
    else:
        composite_count += 1

print("Count of prime numbers entered:", prime_count)
print("Count of composite numbers entered:", composite_count)
