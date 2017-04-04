import numbers
import decimal
def primes_generator(n):
    primes=[2]
    if isinstance(n,numbers.Number):
        if n>1:                
            for i in range(2,n+1):           
                if i%2==1:
                    primes.append(i)
            return set(primes)
        else:
            return "Not A Prime Number"
    elif type(n)==str:
        return 'Not A Prime Number'
    
    elif type(n)==list:
        return 'Not A Prime Number'

print primes_generator("5")
