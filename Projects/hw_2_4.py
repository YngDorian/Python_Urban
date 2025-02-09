numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list
not_primes = list
i = 0
for numbers[i] in numbers:
    if numbers[i] % numbers[i] == 0 and numbers[i] != 0:
        primes[i].append(numbers[i])
    elif numbers[i] % numbers[i] != 0 or numbers[i] == 0:
        continue