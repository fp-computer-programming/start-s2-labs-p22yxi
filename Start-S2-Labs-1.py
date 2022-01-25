# Yongdong Xi
def products(number_lst, value):
#The function should return a list with the same number of elements where each element is equivalent to the value at the equivalent index in the passed list multiplied by the passed value.
    for index, element in enumerate(number_lst):
    # Get the indexes of the elements in the list
        number_lst[index] = index * value
        # Get the new number after index multiples value, then change the old number to the new number with the same index
    return number_lst


print(products([1, 2, 3, 4, 5, 6, 8], 4))