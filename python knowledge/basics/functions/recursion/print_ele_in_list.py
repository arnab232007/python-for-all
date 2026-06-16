def printlist(list):
    if len(list) == 0 :
        return 
    print(list[-1])
    printlist(list[:len(list)-1])

printlist([1,2,3,4,5,6,7,8,9,10])