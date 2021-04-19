import random
import copy as c
str_t = ""
print("Hello world!")


def setting_string() :
    global str_t
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
    str2 = "".join(str1)
    str_t = c.deepcopy(str2)

def test_slicing() :
    global str_t
    for i in range (0,10) :
        print("원문은 str_t : {} 입니다.".format(str_t))
        r1 = random.randint(1,3)
        if r1 == 1:
            #[r2:]
            r2 = random.randint(-len(str_t),len(str_t)-1)
            print("str_t[{}:] 은 뭘까요?".format(r2))
            ans = input("")
            chech_ans(ans,str_t[r2:])
        elif r1 == 2 :
            #[r2:r3]
            r2 = random.randint(-len(str_t),len(str_t))
            r3 = 0
            if r2 < 0 :
                r3 = random.randint(len(str_t)-r2+1,len(str_t))
            else :
                r3 = random.randint(r2+1,len(str_t))
            print("str_t[{}:{}] 은 뭘까요?".format(r2,r3))
            ans = input("")
            chech_ans(ans,str_t[r2:r3])
        elif r1 == 3 :
            #[:r2]
            r2 = random.randint(-len(str_t)+1,len(str_t))
            print("str_t[:{}] 은 뭘까요?".format(r2))
            ans = input("")
            chech_ans(ans,str_t[:r2])
        setting_string()



def chech_ans(user_ans , right_ans) :
    if user_ans == right_ans :
        print("맞았습니다!")
    else :
        print("아닙니다.")
        print("정답은 '{}'이고 , 당신은 '{}'을(를) 입력하셨습니다.".format(right_ans,user_ans))
        

print("Hello world!")
setting_string()
test_slicing()
