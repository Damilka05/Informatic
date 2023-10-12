'''
Given three arrays of integers, return the sum of elements that are common in all three arrays.
For example:
common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
'''
common = ([1,2,3],[5,3,2],[7,3,2])
a = []
total = 0
for i in range(len(common)):
    for j in range(3):
        a.append(common[i][j])
for k in range(len(a)):
    for l in range(len(a)-1, 0, -1):
        if a[k] == a[l]:
            total += 1
print(total)

