from flask import Flask, render_template, request #flask import
import requests

app = Flask(__name__)#초기화
#input이라는 tag는 input만 존재 했을 때 의미 없고 데이터 담고만 있음
#다른 페이지, 서버로 전달하는 코드를 작성할 것이다.

#form으로 html을 보내주는 것
@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html') #어떤 html 파일을 보여주는 것

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    #request.args #=> {'username':'epik_j', 'message':'집가고싶다'}
    username = request.args.get('username') #=> 'epik_j'
    message = request.args.get('message')
    return render_template('receive.html', username=username, message=message)

@app.route('/check_lotto')
def check_lotto():
    return render_template('check_lotto.html') #회차 정보를 입력 받는 폼


@app.route('/result_lotto')
def result_lotto():
    n = request.args.get('round_lotto') #=>800 request는 flask에서 제공함
    #my_n = request.args.get('my_lotto')

    #이 주소로 요청을 보내야함.
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
    response = requests.get(url) #응답에 대한 모든 내용
    lotto = response.json() #=>dict

    #python comprehension, 위의 것보다 성능 좋음
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]   
    bonus = lotto['bnusNo']

    #my_lotto랑 로또 번호 비교
    #my_n.split(' ')
    #list comprehension으로 
    my_n = [int(number) for number in request.args.get('my_lotto').split()]
    #교집합/ 이거 말고 이중for문으로 가능, set(winner): set으로 변환하는 것
    cmp_w = len(list(set(winner) & set(my_n))) 
    #cmp_b = len(list(set(bonus) & set(my_n)))

    if cmp_w == 6 :
        lotto_re = '1등'
    #elif cmp_w + cmp_b == 6 :
    #    lotto_re = '2등'
    elif cmp_w == 5 :
        if bonus in my_n : 
        #if cmp_b == 1 : 
            lotto_re = '2등'
        else :
            lotto_re = '3등'
    elif cmp_w == 4 :
        lotto_re = '4등'
    elif cmp_w == 3 :
        lotto_re = '5등'
    else :
        lotto_re = '꼴등'

    return render_template('result_lotto.html', winner=winner, bonus=bonus, round_lotto=n, lotto_re=lotto_re)

if __name__ == '__main__':
    app.run(debug=True)
