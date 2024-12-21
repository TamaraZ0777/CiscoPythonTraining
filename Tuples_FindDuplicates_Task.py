tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = 0
for elem in tup:
    if elem == 2:
        duplicates += 1 
 
print(duplicates) # outputs: 4

# same with count method
duplicates = tup.count(2)

print(duplicates)

