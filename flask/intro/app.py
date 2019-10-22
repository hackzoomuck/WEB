from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

print(__name__)
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!' 

@app.route('/mulcam')
def mulcam():
    return 'This is mulcam'

#if __name__=='__main__':
#    app.run(debug=True)

# Path Variable / Variable Routing
@app.route('/greeting/<string:name>')
def greeting(name): #name parameter can using in def
    return f'Hi, {name}' #f string / 'hi, {}'.format(name) : 3.6이전

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{num}의 세제곱은 {result}입니다'

#사람 수를 path를 통해 받아, 사람 수 만큼 메뉴 추천
@app.route('/dinner/<int:person>')
def dinner(person):
    menu=['a','b','c','d','e','f','g','j','i']
    result = random.sample(menu,person) #비복원추출
    #['e', 'd', 'c']
    # return str(result)
    #특정 문자열
    return ','.join(result) 

@app.route('/html')
def html():
    multiline = """
        <h1>hi, hello</h1>
        <p>만나서 반갑습니다</p>
    """
    #return '<h1>Hi, hello</h1>'
    return multiline     

#html 파일을 보여주는 코드
@app.route('/html_file')
def html_file():
    return render_template('file.html')

#Template Variable
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)
    # 값만 넘기는 것을 위치인자
    # 넘어갈 변수명까지 지정 값만 넘기는 위치인자

@app.route('/list')
def list1():
    menu=['a','b','c','d','e','f','g','j','i']
    return render_template('list.html', menu=menu)

#def a(x,y,z):
    #return x,y,z
#a(1,z=1,y=2) #키워드 인자