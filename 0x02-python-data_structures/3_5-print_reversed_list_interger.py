def print_reversed_list_integer(my_list=[None]):
    if my_list != None:
        my_list = [1, 2, 3, 4]
#    elif not my_list:
#        return None
    else:
        my_list = [1, 2, 3, 4]
        my_list.reverse()
    for i in my_list:
        print("{:d}".format(my_list[i]))