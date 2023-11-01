'''
Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example: 

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
More examples in the test cases. 

Good luck!
'''

common = ([1,2,2,3],[5,3,2,2],[7,3,2,2])
total = 0
common1 = common[0]
commonn = list(set(common1))
for i in range(1, len(common)-1):
    for j in range(len(commonn)):
        for k in range(len(common[i])):
            if commonn[j] == common[i][k]:
                if commonn[j] == common[i+1][k]:
                    total += commonn[j]
print('Сумма повторяющихся чисел в common = ', total)