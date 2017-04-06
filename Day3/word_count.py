def words(A):#A String
    split_words=A.split()
    list_of_words=[]
    for word in split_words:
        list_of_words.append(word)

    lis={i:list_of_words.count(i) for i in list_of_words if not i.isdigit()}
    #{'testing': 2, 1: 1, 2: 1}
    count_words={int(k):list_of_words.count(k) for k in list_of_words if k.isdigit()}
    count_words.update(lis)
    #return count_words
    print count_words

#print words("testing 1 2 testing")
#print words('car : carpet as java : javascript!!&@$%^&')
