lunch = {
    '중국집': '양자강',
    '한식집': '시래기', #tralling comma마지막까지 코드를 작성하는 것
}
#lunch= dict(중국집='양자강')
lunch['분식집']='김밥카페' #[키]=값
lunch['중국집'] #return 값이 => '양자강'

dinner = { #중첩된 dictionary
    '한식집' : { #string, int, float, boolean만 가능
        '고갯마루' : '02-3456-7890',
        '순남시래기' : '02-3456-1234',
    }
}

dinner['한식집']['고갯마루'] #=>02....
dinner.get('한식집').get('고갯마루')

#기본 활용
for key in lunch: #lunch 변수 안에 것을 반복
    print(key)
    print(lunch.get(key))

#key 가져오기
for key in lunch.keys(): #lunch안의 모든 dictionary 반환
    print(key)           # [key, key, ...]
    print(lunch.get(key))

#value 가져오기
for value in lunch.values(): # [value, value,...]
    print(value)

#key value 동시에 가져오기
for key, value in lunch.items(): #key value pair 가져옴 , list 안의 tuple로써 [(key, value),(key,value)...]
    print(key)
    print(value)