
### 슬라이싱을 이용해서 리스트값 바꾸기
```py
# Python's list slice syntax can be used without indices
# for a few fun and useful things:

# You can clear all elements from a list:
>>> lst = [1, 2, 3, 4, 5]
>>> del lst[:]
>>> lst
[]

# You can replace all elements of a list
# without creating a new list object:
>>> a = lst
>>> lst[:] = [7, 8, 9]
>>> lst
[7, 8, 9]
>>> a
[7, 8, 9]
>>> a is lst
True

# You can also create a (shallow) copy of a list:
>>> b = lst[:]
>>> b
[7, 8, 9]
>>> b is lst
False

```

# collections.Counter 활용해서 요소 카운트하기
- elements in an iterable:
```py
>>> import collections
>>> c = collections.Counter('helloworld')

>>> c
Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

>>> c.most_common(3)
[('l', 3), ('o', 2), ('e', 1)]
```
