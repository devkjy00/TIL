# 해시테이블(HashTable)
- key에 value를 저장, 적은 리소스로 많은 데이터를 효율적으로 관리
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
# immutable Dict

```py
from types import MappingProxyType

d = {'key1': 'value1'}

# 실수로라도 수정할 수 없는 읽기전용 immutable Dict
d_frozen = MappingProxyType(d)
# MappingProxyType() 인자객체를 읽기전용 mappingproxy객체로 만든다
# 값을 수정,추가 할 수 없다
```
# immutable Set

```py
from types import MappingProxyType
s1 = {1,2,3}
# 중복되지 않고 정렬되지 않는 셋 객체

s_frozen = frozenset(s1)
# frozenset() 읽기전용 frozenset객체로 만든다
# 값을 수정,추가 할 수 없다
```

# 선언 최적화

```py
from dis import dis
# 바이트코드를 역 어셈블 해서 분석을 지원
# 명령어의 실제 과정을 볼 수있다

print(dis('{10}'))
print(dis('set([10])'))
# set()을 사용했을때 더 복잡한 과정으로 실행되는 것을 볼 수 있다
```