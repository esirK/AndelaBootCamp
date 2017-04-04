import numbers
import decimal
def primes_generator(n):
<<<<<<< HEAD
    primes=[]
    ikondaani=[]
    if type(n)==int:
        if n>1:                
            noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
            for x in range(2,n):
                if x not in noprimes:
                    primes.append(x)
=======
    primes=[2]
    if type(n)==int:
        if n>1:                
            for i in range(2,n+1):           
                if i%2==1:
                    primes.append(i)
>>>>>>> 7bcbb199e3131fbf7e59600ccb28e68f67787786
            return primes
        else:
            return "Not A Prime Number"
    elif type(n)==str:
        return 'Not A Prime Number'
    
    elif type(n)==list:
        return 'Not A prime Number'
<<<<<<< HEAD
#print primes_generator(300)
=======

#print primes_generator(19.9)
>>>>>>> 7bcbb199e3131fbf7e59600ccb28e68f67787786
