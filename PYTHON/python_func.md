# 파이썬 내장 함수

- chr(int)
    - 유니코드값을 문자열로 반환한다.
    - int값이 범위(0~1,114,111) 밖에 있을 때 ValueError발생
- filter(function, iterable)
    - iter를 조건문으로 불리언값을 반환하는 함수에 인자로 넣어서 이터레이터를 만들고 참인 return값을 반환한다.
    - 함수가 None이면 iter는 자기자신을 반환, 거짓인 값은 삭제된다
- map(function, iterable, ...)
    - iter의 모든항목에 함수를 적용하고 그 결과를 iter객체로 돌려준다.
    - 다중 iter를 인자로 받을 경우 가장 짧은 iter객체가 끝나면 멈춘다.

- next(iterator[,default]) 
    - --next--() 메서드를 호출 해서 iterator에서 다음 항목을 꺼낸다. 
- ord(chars)
    - 인자값의 유니코드값을 반환




# 외장 라이브러리 함수