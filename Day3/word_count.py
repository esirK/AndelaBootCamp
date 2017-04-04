def words(A):#A String
    split_words=A.split()
    list_of_words=[]
    for word in split_words:
        list_of_words.append(word)

    count_words={i:list_of_words.count(i) for i in list_of_words}
    return count_words
