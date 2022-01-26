def comes_after(st, l): 
    answer = ""
    for i in range(len(st) - 1):    # loop through characters in st
        if st[i].lower() == l.lower():  # .lower() is used to not be case-sensitive
            if st[i + 1].isalpha():  # checks if next character is a letter
                answer = answer + st[i + 1]  # appends to answer
    return answer



print(comes_after('wear', 'a'))