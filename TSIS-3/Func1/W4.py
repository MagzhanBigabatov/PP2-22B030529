def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

prime_numbers = filter_primes(numbers)

print("Prime numbers:", prime_numbers)

