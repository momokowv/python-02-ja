def mystery_function(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i ** 2)
        else:
            result.append(i)
    print(result)
    return result


if __name__ == "__main__" :
    list1= [1, 2, 3, 4, 5]
    list2= [4, 1, 6, 2, 10]
    mystery_function(list1)
    mystery_function(list2)