a = [1,5,2,7,4,3,6]
print("정렬 안한 a 리스트 :",a)

a.sort(reverse=True)
print("내림차순 a 리스트 :",a)

## sort() 와 sort(reverse=False) 는 같다.
a.sort(reverse=False)
print("오름차순 a 리스트 :",a)
a.sort()
print("오름차순 a 리스트 :",a)
