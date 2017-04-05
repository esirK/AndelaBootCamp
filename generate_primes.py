def primes_generator(n):
    primes=[]
    if type(n)==int:
        if n>1:                
            noprimes = set(j for i in range(2, n+1) for j in range(i*2, n+1, i))
            for x in range(2,n+1):
                if x not in noprimes:
                    primes.append(x)
            print primes
        else:
            return "Not A Prime Number"
    elif type(n)==str:
        return 'Not A Prime Number'
    
    elif type(n)==list:
        return 'Not A prime Number'
# primes_generator(60)
