# function

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 입금 후 잔액 정보 반환
    
# 전달값과 기본값

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance # 기존 잔액 반환
    
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금
print(balance) # 현재 잔액

# 출금 시도
balance = withdraw(balance, 2000) # 2000원 출금 시도 시 잔액이 부족하므로 실패
balance = withdraw(balance, 500) # 500원 출금 시도 시 성공
print(balance) # 현재 잔액

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 출금 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 반환
    
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 기본값
def profile (name, age= 17, main_lang= "python"):
    print("이름은 : {0}\t나이 : {1}\t메인언어 : {2}" \
          .format(name, age, main_lang))
    # \를 쓰면 문장 이어서 쓸수 있음
profile("Kim")
profile("Chang")

# 키워드 인자
profile(age = 19, name = "eo", main_lang="JAVA")

# 가변인자
def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
# print(type(language)) # tuple
    for lang in language:
        print(lang, end=" ") # 언어들을 모두 한 줄에 표시
    print() # 줄바꿈 목적

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") # JavaScript 추가
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수 전역변수