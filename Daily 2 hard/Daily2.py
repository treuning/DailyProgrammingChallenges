############################
#This problem was asked by Uber.
#
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
#Follow-up: what if you can't use division?

#With Division
def exProduct(arr):
    product = 1
    result = []
    step = 0

    for x in range(len(arr)):
        product = product * arr[x]
        step+=1 
    for x in range(len(arr)):
        result.append(product//arr[x])
        step+=1
    print(result,step)


#Without Division
def noDivProduct(arr):
    result = []
    product = 1
    step = 0
    for x in range(len(arr)):
        step+=1
        for i in range(len(arr)):
            step+=1
            if i==x:
                continue
            else:
                product = product * arr[i]
        result.append(product)
        product = 1
    print(result,step)

t = [23,5,32,7,44,11,88,76]

exProduct(t)

noDivProduct(t)