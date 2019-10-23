mulcam = {
    "location": ["역삼","선릉"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "딥러닝":  {
            "lecturer": "junwoo",
            "manager": "민채원",
            "groups": {
                "1조": ["윤선재", "이정서", "한대건", "문금란", "이진호"],
                "2조": ["유승우", "이효정", "임채명", "박병규"],
                "3조": ["김지현", "박희현", "강강토"],
            }
        },
        "블록체인": {
            "lecturer": "bing",
            "manager": "문정연"
        }
    }
}

#안되는 코드 
# loc_len=mulcam.get("location")
# len(loc_len)
# mulcam['location']

#1.
#mulcam['location'] # 해당 리스트 나옴
print(len(mulcam.get('location')))

#2. 해당 value이 있는 지 보는 것 in
print('request' in mulcam.get('language').get('python').get('python standard library'))

#3.
for key in mulcam.get('language').keys(): #dictionary
    print(key)

#4
for value in mulcam.get('classes').get('블록체인').values():
    print(value)

#5
#for item in mulcam.get('language').get('python').get('frameworks').items(): #키벨류페어로 튜플이 들어있음
 
for key, value in mulcam.get('language').get('python').get('frameworks').items(): #키벨류페어로 튜플이 들어있음
   # item[0] #key
   # item[1]
   print(f'{key}는 {value}이다')

#6
members = mulcam.get('classes').get('딥러닝').get('groups').get()
result=random.choice(members)
print(result)