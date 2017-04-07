class BinarySearch(list):
    def __init__(self,a,b):
        #a------Length of list to create
        #b------diffrence between consecutive values
        self.length=a
        
        for i in range(b,(a*b)+1,b):
            self.append(i)
        #self
    def search(self,val_to_search):
        solution={}
        count=0
        minimum=0
        maximum=self.length
        while minimum<maximum:
            count=count+1
            midpoint=minimum+(maximum-minimum)//2

            if val_to_search==self[midpoint]:
                break
            elif val_to_search>self[midpoint]:
                if minimum==midpoint:
                    solution['count']=0
                    solution['index']=-1
                    return solution
                minimum=midpoint
            elif val_to_search<self[midpoint]:
                maximum=midpoint
        solution['count']=count
        solution['index']=midpoint
        return solution
        #return solution
        
#a=BinarySearch(20,1)
#a.search(16)
#b=BinarySearch(20,1)
#print b.search(16)
#c=BinarySearch(100, 10)
#print c.search(10000)
