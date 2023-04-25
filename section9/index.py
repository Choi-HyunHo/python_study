# dictionary
dic = {}
dic2 = dict()

print(dic)  # {} 빈 딕셔너리 선언
print(dic2) # {} 빈 딕셔너리 선언


# 딕셔너리 값 추가
my_dic = {} # {}
my_dic[1] = 'a' # {1: 'a'}
my_dic['apple'] = 2 # {1:'a', 'apple' : 2}
my_dic[3] = 'c' # {1: 'a', 'apple': 2, 3: 'c'}

print(my_dic) # {1: 'a', 'apple': 2, 3: 'c'}

# 딕셔너리 값 수정
my_dic[3] = 'korea'

print(my_dic) # {1: 'a', 'apple': 2, 3: 'korea'}

# 딕셔너리 삭제
del(my_dic[3])

print(my_dic) # {1: 'a', 'apple': 2}

# 딕셔너리 키 구하기
a = my_dic.keys()

print(a) # dict_keys([1, 'apple'])

a = list(my_dic.keys())

print(a) # [1, 'apple']

b = list(my_dic.values())

print(b) # ['a', 2]

# get
# {1: 'a', 'apple': 2}
print(my_dic.get(1)) # a

# update
# {1: 'a', 'apple': 2}
my_dic.update({'banana' : 3, 123 : 555})

print(my_dic) # {1: 'a', 'apple': 2, 'banana': 3, 123: 555}


# key
# {1: 'a', 'apple': 2, 'banana': 3, 123: 555}
print(1 in my_dic) # True
print('apple' in my_dic) # True
print('melon' in my_dic) # False