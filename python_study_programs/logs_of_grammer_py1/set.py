games = {'GTA5','OVERWATCH','LOL',"BS"}
print(type(games))

#set은 그저 포함된다. 라는 개념이 있는것뿐이다.
#따라서 이 .py파일 자체를 실행시킬때마다 모두 다른 순서로써 출력된다.
for i in range(0,10) :
    print(games)
#다만, 이런 set 요소들을 출력할때마다 바뀌는것은 아니다.


'''신기한점들은'''
dict1 = {"most_game":"GTA5","hate_game":"atr + f4"}
games = set(dict1)
print(games)
'''dic를 set형식으로 바꾸게 된다면, key 값만 살아남고 나머지 value는 없어져버린다는것이다.'''


games.add("R6S")
print(games)
#add 는 요소 하나만 추가할때 쓰는것이고,

games.remove('R6S')
print(games)
#remove는 요소를 제거할때 쓴다.
'''
games.remove("most_game","hate_game")
print(games)
'''
#다만 두개를 한꺼번에 지울 순 없다.

games.discard('GTA5')
#지금 위 코드를 보면 games라는 셋에는 없는 'GTA5'라는 요소를 지우라고 명령이 나와있는데, 이럼에도 불구하고
print(games)
#오류가 뜨지 않는다.
'''
discard는 remove와는 다르게 굉장히 유연하기 때문에
요소가 제거됨은 확신하기 위해서 쓰는 경우가 많다고 한다.
따라서 위의 구문의 의미는
'GTA5'라는 요소가 확실히 사라졌는지 알 수 없기에
games에 다시 한번 들어가서 'GTA5'라는 요소가 사라졌는지
확인한것이라고 보면 된다.
'''

games.update(("UTS","EFT"))
print(games)
#update는 요소 여러개를 추가할때 쓰는것이다.

'''
위의 update함수를 사용하는 부분에서 주의해야하는것은, update함수 내부에 한번 더 tuple형식으로 한번 더 감싸준 이유에 있다.
그저 games.update("UTS","EFT")라고 써버리면
games라는 셋에는
'U','T','S','E','F'가 들어가버린다.
하나하나 독립된 객체로써 접근하는것이 아닌
전체적으로 문자'열'로써 접근해버리기때문에
그저 UTSEFT라는 글자를 넣어버리는것처럼 반응해버린다.
따라서 괄호 한번을 더 묶어서 tuple이나 dict, list 형식으로
감싸줘야한다.
'''

