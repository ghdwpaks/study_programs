s1 = "xx::yy::zz"
print(s1)

print("\n\n1")
print(s1.split("::"))
print(type(s1.split("::")))

print(s1.split(":"))
print(type(s1.split(":")))

print("\n\n2")
s2 = s1.split("::")
print(",".join(s2))
print(", ".join(s2))
print(":::".join(s2))