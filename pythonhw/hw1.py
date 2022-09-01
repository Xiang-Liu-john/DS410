

def q1(mystring):
    """ split the string by tabs to get an array and return the array """
    ans = mytring.split("\t")
    return ans
    pass


def q2(mystring):
    """ split the string by tabs to get an array and return the second element of the array """
    ans = mystring.split()
    return ans[1]
    pass



def q3(myarray):
    """ myarray is an list of pairs. this function should return the sum of the first
    items in the pair and the sum of the second items """
    ans = ((myarray[0][0] + myarray[1][0] + myarray[2][0]), (myarray[0][1] + myarray[1][1] + myarray[2][1])
    return ans
    pass
    


def q4(mystringarray):
    """ return the position of the first occurrence of the string 'hi' or -1 if it is not found.
    you cannot change how the array is iterated and you cannot use any list operations on mystringarray"""
    word = "hi"
    for i in range(len(mystringarray)):
        if mystringarray[i] == word:
            return i
        i = i + 1

    for mystring in mystringarray:
        pass


def q5(myarray):
    """ return a dictionary containing the counts of items in the input array """
    dict = {}
    for i in myarray:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
pass
