import numbers
import decimal
def primes_generator(n):
    primes=[]
    ikondaani=[]
    if type(n)==int:
        if n>1:                
            noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
            for x in range(2,n):
                if x not in noprimes:
                    primes.append(x)
            return primes
        else:
            return "Not A Prime Number"
    elif type(n)==str:
        return 'Not A Prime Number'
    
    elif type(n)==list:
        return 'Not A prime Number'
#print primes_generator(300)
