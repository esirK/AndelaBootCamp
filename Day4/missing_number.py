def find_missing(A,B):
    #check if contents of list are numbers
    AandB=A+B
    if all(isinstance(item,int) for item in AandB)and all(pos>0 for pos in AandB):    
        set1=set(A)
        set2=set(B)

        d_set1_and_set2=len(set1-set2)
        d_set2_and_set1=len(set2-set1)

        
        if (d_set1_and_set2)>1 or (d_set2_and_set1)>1 or (d_set2_and_set1+d_set1_and_set2)>1:
            print "The arrays should be diffrent by only one extra number"
            #return "The arrays should be diffrent by only one extra number"
        else:
            if d_set1_and_set2>0:
                print list(set1-set2)[0]
                #return list(set1-set2)[0]
            elif (d_set1_and_set2==0)and(d_set2_and_set1==0):
                print "0"
                #return 0
            else:
                print list(set2-set1)[0]
                #return list(set2-set1)[0]
    
    else:
        print "The Arrays Should Only Contain positive Numbers"
        #return "The Arrays Should Only Contain Numbers"
#find_missing([0,2,3,4,5], [2,3,4,5])
