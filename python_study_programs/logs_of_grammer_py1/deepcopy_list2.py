import copy
a = [1,2,3,4,5]
b = copy.deepcopy(a) #b = a[:]와 같다
a[1] = 4
print(a)
print(b)