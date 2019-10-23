import requests

n = int(input('회차를 입력하세요: ')) #int로 변경,,


#이 주소로 요청을 보내야함.
url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
response = requests.get(url) #응답에 대한 모든 내용
#response.text #=>string
lotto = response.json() #=>dict
#num1=lotto['drwtNo1'] 단순반복


#winner = []
#for i in range(1, 7) :
#    winner.append(lotto[f'drwtNo{i}'])

#python comprehension, 위의 것보다 성능 좋음
winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]   

bonus = lotto['bnusNo']

print(f'당첨번호는 {winner} + {bonus} 입니다.')
