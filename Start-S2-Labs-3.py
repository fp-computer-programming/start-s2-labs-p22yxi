# Yongdong Xi
#What comes after?
def comes_after(st, l):
    answer = '' 
    # create a blank string is used to put the answer
    for x in range(len(st) - 1):
    # select an integer index from the length of the string minus one
        if st[x].lower() == l.lower() and st[x + 1].isalpha():
        # confirm that the position of the selected index is the same as the character that needs to find the subsequent content confirm the right side is alpha
            answer = answer + st[x + 1]
        
    return answer


            
print(comes_after('juesi', 'i'))
