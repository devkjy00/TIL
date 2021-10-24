## Unpacking
    
```py
# 언팩킹으로 함수 인자값 전달
divmod(100,9) #몫과 나머지반환
divmod(*(100,9))
# (11, 9) 반환

print(*(divmod(100,9)))
# 튜플을 언팩킹해서 11, 9를 반환

# 예상을 벗어나는 양의 자료를 팩킹해서 저장할 수 있다
x, y, *rest = range(10)

x, y, *rest = range(2)
# 언팩킹은 값을 받지 않아도 오류를
# 일으키지 않고 빈 리스트로 반환된다



```
- ### ***핵심 정리***
    - 시퀀스형 객체를 한 꺼풀 벗겨내는 기능 (괄호를 1차원 벗긴다)
    - 동적인 양의 데이터를 오류없이 저장할 수 있다
    - 값을 받지 않아도 오류없이 빈 리스트를 반환한다
#
## Mutable(가변) vs Immutable(불변)
- in-place operation
    - 가변형 변수(list..)를 사용하면 같은 메모리 주소값에 결과 값이 저장된다.
    - 불변형 변수(tuple..)를 사용하면 다른 메모리 주소에 결과 값이 저장된다.

#
## sort vs sorted
- sorted
    - 정렬 후 새로운 객체값 반환
    - 옵션
    ```py
    sorted(x, reverse=True)
    # 반대로 정렬한다
    sorted(x, key=len)
    # len함수를 call back해서 반환된 각 원소의 길이를 기준으로 정렬
    sorted(x, key=lambda x: x[-1])
    # lambda함수 인자로 원소값을 받아서 인덱스의 값을 기준으로 정렬    
- sort
    - 정렬 후 객체값 직접 변경

    ```py
    print(x.sort())
    # 반환 값은 None
    ```

    