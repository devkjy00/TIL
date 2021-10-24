# sequence 
- ### **시퀀스의 뜻**
    - ***일렬로 나열되 순서가 있는 자료***, 파이썬에는 리스트, 튜플, 문자열 등이 있다


## 파이썬의 시퀀스 자료형
- 컨테이너(Container : [list, tuple, collection.deque])
    - 서로 다른 자료형을 담을 수 있다.

- 플랫(Flat : [str, bytes, bytearray, array.array, memoryview]])
    - 한개의 자료형만 담을 수 있다.
    - 더 빠른 연산이 가능하다
### 가변형, 불변형
- 가변형 (mutable: [list, bytearray, array.array, memoryview, deque])
- 불변형 (imutable: [tuple, str, bytes])
- ### **그 외**
    - 가변형(mutable: )

### 지능형 리스트(Comprehending Lists)
- 데이터 양이 많을 수록 Comprehension을 사용하는 것이 조금 더 빠르다.
- 예제
    ```py
    chars = '!@#$%^&*()'
    code_list3 = [ord(s) for s in chars if ord(s) > 40]
    # ord(): 인자값의 유니코드값으로 변환해서 반환

    # Comprehening List + map, filter
    # iter를 함수에 대입,연산하고 조건문을 통해서 참인 값만 반환
    code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
    # 더 좋은 코드.
    
    ```

## Generator 
- iterable한 객체를 생성하는 역할
- 한 번에 한 개의 항목을 생성(메모리를 유지하지 않는다)
- yield 명령어를 사용해서 값을 반환
- 필요한 만큼만 연산하고 적은 메모리 사용량으로 iterator를 생성할 수 있다.
- Generator Expression
    ```py   
    tuple_g = (x for x in y)
    # x = ()로 실행
    print(next(tuple_g))
    # next()로 iter를 연산한 1개의 값을 반환 ,또 실행하면 그 다음값..

    import array

    array_g = array.array('I',(ord(s) for s in chars))
    
    print(array_g.tolist())
    # tolist() : array형을 list형으로 변환
    ```