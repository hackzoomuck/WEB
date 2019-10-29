class Person(): #클래스(집단)
    #멤버변수
    name = '사람의 고유한 속성'
    age = '출생 이후부터 삶을 마감할 때까지의 기간'

    #멤버 메소드(행동)
    def greeting(self):
        print(f'{self.name}이 인사합니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

jieun = Person() #인스턴스
print(jieun.name)
print(jieun.age)
jieun.name='jieun'
jieun.age='26'
print(jieun.name)
print(jieun.age)
print(Person.name)
print(Person.age)
jieun.greeting()

