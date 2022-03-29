def count_integer(numbers, integer):
    count = 0
    for index, value in enumerate(numbers):
        if value == integer:
            count += 1
    if count == 0:
        count = 42
    return count

def list_func(numbers, integer):
    if integer not in numbers:
        return []
    for index, value in enumerate(numbers):
        if value == integer:
            numbers[index] = 6
    tmp_list = numbers.copy()
    tmp_list.reverse()
    print(tmp_list)
    return numbers

def compare_lists(list1, list2):
    result=[]
    for x in list1:
        #this verion only adds one of the common elements to the new list
        if x in list2 and x not in result:
            result.append(x)
    return result

def remove_duplicates(lst):
    result = list(lst) # making sure that the given argument will become a list
    tmp_set = set(lst)
    if len(tmp_set) != len(lst):
        result = list(tmp_set)
    return result

def dict_func(dictionary):
    '''The .setdefault() function works like the .get function, the get function
    fetches the value from the key and returns a given default if no key was found, the .setdefault function does the
    same but also adds the default key and value to the dictioniary if no key was found'''
    print(
        f'You have a {dictionary.setdefault("Type", "unknown type")} from {dictionary.setdefault("Brand", "unknown brand")} that costs: {dictionary.setdefault("Price", "an unknown amount")}')
    dictionary.setdefault("OS", "Linux")
    return dictionary

