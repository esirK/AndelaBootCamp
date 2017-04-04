import numbers
import decimal
def primes_generator(n):
    primes=[2]
    if type(n)==int:
        if n>1:                
            for i in range(2,n+1):           
                if i%2==1:
                    primes.append(i)
            return primes
        else:
            return "Not A Prime Number"
    elif type(n)==str:
        return 'Not A Prime Number'
    
    elif type(n)==list:
        return 'Not A prime Number'

#print primes_generator(19.9)
