def primes_generator(n):
    primes=[2]
    for i in range(2,n+1):
        if i%2==1:
            primes.append(i)
    return set(primes)


print primes_generator(5)
