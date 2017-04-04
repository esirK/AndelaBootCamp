def data_type(A):
    if type(A) is str:
        return len(A)
    elif A is None:
        return 'no value'
    elif type(A) is bool:
        return A
    elif type(A) is int:
        if A<100:
            return 'less than 100'
        elif A==100:
             return 'equal to 100'
        else:
            return 'more than 100'
    elif type(A) is list:
        if len(A)>=3:            
            if A[2]!=None:
                return A[2]
        else:
            return "None"

#print data_type("andela")
