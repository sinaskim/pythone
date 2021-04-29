#클래스 user 시작
class User:
    #생성자
    def __init__(self, name, number, sex):
        self.name = name
        self.number = number
        self.sex = sex
        
    #마지막에 결과 출력해주는 메소드
    def introduce_myself(self):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." %(self.name,self.number,self.sex)) 

    
#메인 함수 시작
list = []
while(True):
    name = input("이름을 입력하세요:")
    if(name=="그만"):
        for i in list:
            i.introduce_myself()
        break
        
    number = input("번호를 입력하세요:")
    sex = input("성별을 입력하세요:")
    
    if(sex=="female"or sex=="male"):
        sex = sex
    else:
        sex="unknown"

    user = User(name,number,sex)
    list.append(user)
    for i in list:
        i.introduce_myself()