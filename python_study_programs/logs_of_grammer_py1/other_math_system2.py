'''
아래코드와 같은 방식으로써 변수를 만들게 된다면
정수가 들어가더라도(예 : 8+24j)
전부 실수(float)형식이 된다.
'''

print("\n\n1")
print(8+24j)
print(type(8+24j))
#실수 8 + 허수 24



print("\n\n2")
print(13.3+21.4j)
print(type(13.3+21.4j))
#실수 8 + 허수 24



print("\n\n3")
c = 8+24j
print(c)
print("실수부분 :",c.real)
print("허수부분 :",c.imag)
print("켤레복소수 :",c.conjugate())


print("\n\n4")
d = 1j
#d 는 허수 1
print(d)
print("실수부분 :",d.real)
print("허수부분 :",d.imag)
print("켤레복소수 :",d.conjugate())




