#만들어본 회원가입하고 로그인
ID =  input("아이디:")
PW = input("비밀번호:")

print(ID+"님 회원가입이 완료되었습니다.\n 로그인 하시겠습니까?(Y/N):")
answer = input();
if(answer=="Y"):
    l_id = input("아이디:")
    if(l_id==ID):
        l_pw = input("비밀번호:")
        if(l_pw == PW):
            print(l_id+"님 로그인 되셨습니다.")
        else:
            print("비밀번호가 틀렸습니다.")
    else:
        print("존재하지 않는 아이디입니다.")
else:
    print("종료되었습니다.")
