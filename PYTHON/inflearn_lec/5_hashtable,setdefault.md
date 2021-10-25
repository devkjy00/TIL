# 해시테이블(HashTable)
- key에 value를 저장하는 구조
    - 파이썬의 dict가 해쉬테이블의 예
- key 값의 연산 결과에 따라 value에 직접 접근이 가능 한 구조
- key 값에 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조
- ### **Hashable**
    - immutable형 값만 해쉬값을 가질 수 있다

# Dict Setdefault
- Dict형의 연산 속도를 더 향상 시킬 수 있다
- Setdefault
```py
source = (('k1', 'val1')
        ,('k1', 'val2')
        ,('k2', 'val3')
        ,('k2', 'val4'))

dict1 = {}
dict2 = {}

# No use Setdefault
for k, v in source:
    if k in dict1:
        dict1[k].append(v)
    else:
        dict1[k]=[v]

# Use Setdefault
for k, v in source:
    dict2.setdefault(k, [].append(v))
# setdefault()메서드로 같은 값을 키값으로 가진 밸류를 하나의 키값으로 선언한다

```