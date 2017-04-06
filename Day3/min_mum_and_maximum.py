def find_max_min(L):
    #create a Set To remove duplicates
    set_of_numbers=set(L)

    #Change them To A List To Enable sort operation on The List
    newList=list(set_of_numbers)

    #sort the Numbers
    
    sortedList=sorted(newList)
    minimum=sortedList[0]
    maximum=sortedList[-1]
    if minimum==maximum:
        return [len(L)]
    else:
        print[minimum,maximum]
        #return[minimum,maximum]
#print find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
