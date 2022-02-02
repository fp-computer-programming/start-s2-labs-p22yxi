# Yongdong Xi
# Double Every Other
def double_every_other(lst):
    x = []
    # A new empty list is used to place the results
    for i in range(len(lst)):
        if i % 2 != 0:
        # Select the number in the even position
            x.append(lst[i] * 2)
        # The number in the even digits is multiplied by two 
        # and added to the list that will be the result    
        else:
            x.append(lst[i])
        # Numbers in odd positions are added directly to the resulting list
    return x