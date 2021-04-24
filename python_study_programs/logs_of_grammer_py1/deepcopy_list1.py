a = [1,2,3,4,5]
b = a[:] #deepcopy 와 같은 효과를 보인다.
a[1] = 4
print(a)
print(b)




