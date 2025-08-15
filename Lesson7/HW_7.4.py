def common_elements():

    my_set_3 = {x for x in range(100) if x % 3 == 0}
    my_set_5 = {x for x in range(100) if x % 5 == 0}

    return  my_set_3.intersection(my_set_5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("ОК")