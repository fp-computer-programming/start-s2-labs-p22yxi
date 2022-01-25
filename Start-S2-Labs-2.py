# Yongdong Xi
last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
index = 0
for row in rows:
# select the lists in order from the selected large list containing multiple lists
    for name in (row):
    # select the elements in order from the selected list    
        print("{0} {1}".format(name, last_initials[index]))
        # print the first name in order also print the last name corresponding to the current index
        index += 1
        # every time a name is printed, move the last name one index along the list
        
