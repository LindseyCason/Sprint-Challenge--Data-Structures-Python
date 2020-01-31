import time
from bst import BinarySearchTree

start_time = time.time()

#O(n) because one by one names
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
#splitting at every new line
f.close()

#O(n) bc of 1 by 1 names
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
#splitting at every new line
f.close()

duplicates = []
# for name_1 in names_1: #for every name in names1
#     for name_2 in names_2:#compare to every name in name 2
#         if name_1 == name_2:#if they match
#             duplicates.append(name_1) #append the duplicate to the array

bst=BinarySearchTree(names_1[0])
# print("PRINTING BST",bst.value) #this would not run inside the loop, gave 0 duplicates, moved outside and set to var during debugging
for name_1 in names_1: #for every name in names1
    # print("****************", name_1) #checking loop
    bst.insert(name_1) #insert all names into the tree

for name_2 in names_2:
    # print("~~~~~~~~~", name_2) #checking loop
    if bst.contains(name_2):#if the BST contains the name already
        duplicates.append(name_2)

#runtime I THINK is 0(log(n)) but because there are two inputs, I'm not 100%
#64 duplicates
#runtime runtime: 0.13287711143493652 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
