# 파이썬 내장 함수
- abs(x)
    - 인자값의 절댓값을 반환한다

- aiter(async_iterable)
    - async_iterable(비동기 이터레이터)
- all(iterable)
    - iterable의 모든 요소가 참 이거나 모두 비어있으면 True값을 반환하는 함수
- any(iterable)
    - iterable의 요소증 하나라도 참이면 True반환 비어있으면 False 반환
- bin(x)
    - 정수를 '0b'가 앞에 붙은 이진 문자열로 반환
- bool(x)
    - 인자값이 참인지 거짓인지를 반환
- breakpoint(*args, **kws)
    - 호출 지점에서 디버거로 진입하게 만든다
- class bytearray([source[,encoding[,errors]]])
    - class형으로 새로운 바이트 배열을 돌려준다.
    - 0 <= x < 256 범위의 정수의 가변 시퀀스이다
    - bytes형과 가변 시퀀스형의 메서드 대부분을 포함
- class bytes([source[,encoding[,errors]]])
- callable(object)
    - 인자가 callable이면 True값 반환   
    - True 값이어도 호출을 실패 할 수 있다

- chr(int)
    - 유니코드값을 문자열로 반환한다.
    - int값이 범위(0~1,114,111) 밖에 있을 때 ValueError발생
    
- delattr(object, name)
    - 허용된 속성을 삭제한다
    - delattr(x, 'foobar') = del x.foobar
- divmod(a,d)
    - a값을 b로 나눈 몫과 나머지를 반환한다
- enumerate(iterable, start=0)
    - iterable객체의 --next--()메서드를 실행해서 카운트값을 반환하고 객체값을 반환한다
- filter(function, iterable)
    - iter를 조건문으로 불리언값을 반환하는 함수에 인자로 넣어서 이터레이터를 만들고 참인 return값을 반환한다.
    - 함수가 None이면 iter는 자기자신을 반환, 거짓인 값은 삭제된다
- id(object)
    - 객체의 고유한 값(아이덴티티)를 반환한다
        - 객체 값이 저장되어있는 동안 바뀌지 않음이 보장되는 정수이다,
        - 객체가 지워지면 새로 생성된 객체가 이전 객체의 id값을 가질수 있다
- map(function, iterable, ...)
    - iter의 모든항목에 함수를 적용하고 그 결과를 iter객체로 돌려준다.
    - 다중 iter를 인자로 받을 경우 가장 짧은 iter객체가 끝나면 멈춘다.

- next(iterator[,default]) 
    - --next--() 메서드를 호출 해서 iterator에서 다음 항목을 꺼낸다. 
- ord(chars)
    - 인자값의 유니코드값을 반환
## Str 함수
- rjust(자릿수, 공백에채울텍스트)
    - 문자열의 길이를 정하고 공백을 정해서 채울 수 있다

## Int 함수
- 
## Dictionary 함수
- setdefault(key,[default])
    - key 값이 dict에 없으면 default를 저장
    - iteration시에 중복 되는 키값은 한개의 키값만 남게된다
    - value값을 넣지 않으면 None이 저장된다
    - *setdefalut(key,[]).append(value)*
        - []를 넣어서 관련함수 append()를 사용
        - 같은 키값을 가진 모든 밸류를 하나의 키값으로 append시킬 수 있다
        - 튜플을 통해 값을 대입하면 더 빠른 연산이 가능하다


# 외장 라이브러리 함수