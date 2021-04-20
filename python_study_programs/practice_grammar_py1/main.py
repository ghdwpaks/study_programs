import random
import copy as c
import os
str_t = ""
print("Hello world!")


def setting_string() :
    global str_t
    #print("setting_string1 진입함")
    r1 = random.randint(10,20)
    #print("r1 :",r1)
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
    os.system("cls")
    print("원문은 str_t : {} 입니다.".format(str_t))
    r1 = random.randint(1,3)
    if r1 == 1:
        #[r2:]
        r2 = random.randint(-len(str_t),len(str_t)-1)
        print("str_t[{}:] 은 뭘까요?".format(r2))
        ans = input("")
        check_ans(ans,str_t[r2:])
    elif r1 == 2 :
        #[r2:r3]
        r2 = random.randint(-len(str_t),len(str_t))
        r3 = 0
        if r2 < 0 :
            r3 = random.randint(len(str_t)+r2+1,len(str_t))
        else :
            r3 = random.randint(r2+1,len(str_t))
        print("str_t[{}:{}] 은 뭘까요?".format(r2,r3))
        ans = input("")
        check_ans(ans,str_t[r2:r3])
    elif r1 == 3 :
        #[:r2]
        r2 = random.randint(-len(str_t)+1,len(str_t))
        print("str_t[:{}] 은 뭘까요?".format(r2))
        ans = input("")
        check_ans(ans,str_t[:r2])
    setting_string()

def test_length() :
    global str_t
    print("원문은 str_t : {} 입니다.".format(str_t))
    print("len(str_t) 은 뭘까요?")
    ans = input("")
    check_ans(ans,str(len(str_t)))

def test_count() :
    global str_t
    print("원문은 str_t : {}입니다.".format(str_t))
    chr1 = str_t[random.randint(0,len(str_t)-1)]
    print("str_t.count('{}')은 뭘까요?".format(chr1))
    ans = input("")
    check_ans(ans,chr1)


def check_ans(user_ans , right_ans) :
    if user_ans == right_ans :
        print("맞았습니다!")
    else :
        print("아닙니다.")
        print("정답은 \n'{}'이고 , 당신은 \n'{}'을(를) 입력하셨습니다.".format(right_ans,user_ans))
    os.system("pause")

print("Hello world!")
setting_string()

while True :
    
    print("시험볼 과목을 선택해주세요.")
    print("1.len, 글자 수 세기")
    print("2.count 문자열에서 인자갯수 찾기")
    print("3.upper 모두 대문자로 변환하기")
    print("4.lower 모두 소문자로 변환하기")
    print("5.strip 왼쪽, 오른쪽 모두 공백 없애기")
    print("6.replace 문자열 대체하기")
    print("7.find 문자열에서 인자를 왼쪽부터 찾고 그 위치 알려주기")
    print("8.rfind 문자열에서 인자를 오른쪽부터 찾고 그 위치 알려주기")
    print("9.slicing 문자열 슬라이싱 테스트 진입")
    userans1 = int(input("입력 : "))
    for i in range(0,10) :
        setting_string()
        if userans1 == 1 :
            #len, 글자 수 세기
            test_length()
        elif userans1 == 2 :
            #count 문자열에서 인자갯수 찾기
            print(2)
        elif userans1 == 3 :
            #upper 모두 대문자로 변환하기
            print(3)
        elif userans1 == 4 :
            #lower 모두 소문자로 변환하기
            print(4)
        elif userans1 == 5 :
            #strip 왼쪽, 오른쪽 모두 공백 없애기
            print(5)
        elif userans1 == 6 :
            #replace 문자열 대체하기
            print(6)
        elif userans1 == 7 :
            #find 문자열에서 인자를 왼쪽부터 찾고 그 위치 알려주기
            print(7)
        elif userans1 == 8 :
            #rfind 문자열에서 인자를 오른쪽부터 찾고 그 위치 알려주기
            print(8)
        elif userans1 == 9 :
            #find 찾지 못하면 -1 리턴
            print(9)
        elif userans1 == 10 :
            print("문자열 슬라이싱 테스트 진입")
            test_slicing()