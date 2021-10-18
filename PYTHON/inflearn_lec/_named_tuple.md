
# 네임드 튜플(namedtuple)
- ## **특징**
    - 이뮤터블(immutable)객체이다
    - 클래스로 랩핑되어서 클래스객체로 인식
    - 클래스 처럼 틀을 만들고 객체를 생성
    - 딕셔너리와 같이 키와 밸류값으로 접근가능한 튜플

- ## 선언방법
```py
from collection import namedtuple

pt1 = namedtuple('Point', ['x', 'y'])    
pt2 = namedtuple('Point', ['x, y'])
pt3 = namedtuple('Point', ['x y'])
pt4 = namedtuple('Point', ['x y x class', rename=True])
        # 중복되는 키나 예약어는 쓸 수 없지만 rename=True로 하면 새로운 변수명을 자동으로 만들어서 생성할 수 있다, Default는 False로 설정되어 있다
p1 = pt1(x=10, y=35)
p2 = pt2(20, 40)
p3 = pt3(45, y=20)
p4 = pt4(10,20,30,40)
        # 모든 원소를 정확하게 입력해야 오류없이 실행이 된다
```

- ## 네임드 튜플 사용예제
    
```py
# 직각삼각형의 빗변을 구하는 식
# d = 루트(x1-x2)** + (y1-y2)##

from math import sqrt   # 루트함수

# 일반적인 튜플 선언
pt1 = (1.0, 5.0)
pt2 - (2.5, 1.5)

# 길이구하는 식
l_leng1 = sqrt((pt1[0] - pt2[0])**2 +pt1[1] - pt2[1] **2)

print(l_leng1)

from collection import namedtuple
# 네임드 튜플 선언
Point = namedtuple('point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1,5)

print(pt3, pt3.x, pt3[0])
# 키값과 인덱스로 접근가능

l_leng2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)
# 네임드 튜플을 사용해서 가독성에 좋고 관리하기도 편하다
print(l_leng2)

```

- ## Dict to Unpacking
```py
temp_dict = {'x':75, 'y':55}
pt = namedtuple('Point', 'x y')
p = pt(**temp_dict)
# **를 사용해서 사전을 언팩킹해서 x=75, y=55와 같이 키값에 맞게 값을 대입한다

```
- ## 네임드튜플 메소드
```py
temp = [52, 38]
# _make() : 새로운 객체 생성, 리스트를 대입할 수 있게해준다
p = pt._make(temp) 
# _fields : 필드 네임 확인, 네임트튜플의 키값을 반환한다
print(p.fields)
# _asdict() : Ordered Dict(정렬된 사전) 반환한다
print(p._asdict())

```

- ## 실습 예제
```py
Classes = namedtuple('Classes', ['rank', 'number'])
# List Comprehension
numbers = [str(n) for n in range(1,21)] 
ranks = 'A B C D'.split() # 공백을 기준으로 나눠서 리스트로 반환

students = [Classes(rank, number) for rank in rank for number in numbers]

print(students)
# 체계적으로 관리할 수있게 된다

# 가독성을 위한 코딩 Comprehension 사용과 띄어쓰기,들여쓰기 간단하게
students = [Classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]



```