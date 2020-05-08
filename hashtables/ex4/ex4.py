def has_negatives(a):

    result = []
    d = {}
    for num in a:
        
        if abs(num) in d:
            if num < 0 and d[abs(num)] == True:
                result.append(abs(num))
            elif num > 0 and d[abs(num)] == False:
                result.append(abs(num))
        else:
            if num < 0:
                d[abs(num)] = False
            else:
                d[num] = True
    
    return result



    """
    YOUR CODE HERE
    """

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
