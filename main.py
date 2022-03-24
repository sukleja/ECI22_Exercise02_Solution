def count_integer(numbers, integer):
    '''
    Counts the occurences of the given integer in a given array
    :param numbers: 2 integer array, integer
    :return: count of the integer in the array as integer
    '''
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
    # replace integer with 6
    for index, value in enumerate(numbers):
        if value == integer:
            numbers.pop(index)
            numbers.insert(index, 6)
    tmp_list = numbers.copy()
    tmp_list.reverse()
    print(tmp_list)
    return numbers

def compare_lists(list1, list2):
    result=[]
    for x in list1:
        if x in list2 and x not in result:
            result.append(x)
    return result

def remove_duplicates(text):
    result = []
    tmp_set = set(text)
    if len(tmp_set) != len(text):
        result = list(tmp_set)
    return result

def dict_func(dictionary):
    print(
        f'You have a {dictionary.get("Type", "unknown type")} from {dictionary.get("Brand", "unknown brand")} that costs: {dictionary.get("Price", "an unknown amount")}')
    dictionary.setdefault("OS", "Linux")
    return dictionary



