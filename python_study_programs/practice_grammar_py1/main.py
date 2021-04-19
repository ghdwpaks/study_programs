import random

print("Hello world!")


def setting_string() :
    print("setting_string1 진입함")
    r1 = random.randint(10,20)
    print("r1 :",r1)
    str1 = []
    for i in range(0,r1) :
        r2 = random.randint(1,100)
        if r2 % 2 == 0 :
            r2 = random.randint(65,90)
        else :
            r2 = random.randint(97,122)
        
        str1.append(chr(r2))
    print(str1)
    print(type(str1))
    str2 = "".join(str1)
    print(str2)
    print(type(str2))
    
print("Hello world!")
setting_string()
