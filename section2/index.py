# 숫자형
int1 = 1
int2 = -2
int3 = 10000

float1 = 2.2
float2 = -2.0

print(int1) # 1
print(int2) # -2
print(int3) # 10000

print(float1) # 2.2
print(float2) # -2.0

# 문자열
str1 = 'a'
str2 = 'abc'
str3 = "Python's favorite food is perl"
str4 = '"Python is very easy." he says.'

print(str1) # a
print(str2) # abc
print(str3) # Python's favorite food is perl
print(str4) # "Python is very easy." he says.

# boolean
bool1 = True
bool2 = False
bool3 = 1 > 1.1
bool4 = 1 == 1.1

print(bool1) # True
print(bool2) # False
print(bool3) # False
print(bool4) # False

# List
list1 = []
list1.append(123) # 123 추가
list1.append('abc') # 'abc' 추가
list1.append(True) # True 추가

print(list1) # [123, 'abc', True]

# Tuple
tuple1 = ()
tuple2 = (1,)
tuple3 = ('a', 'b', 'c')
tuple4 = 3.14, 'Python', True

print(tuple1) # ()
print(tuple2) # (1,)
print(tuple3) # ('a', 'b', 'c')
print(tuple4) # (3.14, 'Python', True)

# Dictionary
dict = {}  # {}
dict[1] = 'a'  # {1: 'a'}
dict['b'] = 2  # {1: 'a', 'b': 2}
dict['c'] = 'd'  # {1: 'a', 'b': 2, 'c': 'd'}

print(dict)

# 자료형 변환
print(int(3.14)) # 3
print(float(2)) # 2.0

print(str(2))
print(type(str(2))) # <class 'str'>

print(list('3.14')) # ['3', '.', '1', '4']