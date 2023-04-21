print('My name is %s' % 'hyunho') # My name is hyunho
print('x = %d, y = %d' % (1, 2)) # x = 1, y = 2
print('%d x %d = %d' % (2, 3, 2 * 3)) # 2 x 3 = 6


# 정수형 대입
print('%d %d' % (1, 2)) # 1 2

# 실수형 대입
print('%f' % 3.14) # 3.14

# 문자열 대입   
print('%s' % 'coding') # coding 

# format()
print('My name is %s' % 'hyunho') # before -- My name is hyunho
print('My name is {}'.format('hyunho'))  # after -- My name is hyunho


print('{} x {} ={}'.format(2, 3, 2 * 3)) # before -- 2 x 3 =6
print('{1} x {0} ={2}'.format(2, 3, 2 * 3))  # after - 괄호 안의 숫자는 순서를 지정 -- 3 x 2 =6


## 인덱싱
str1 = 'Hello world'
print(len(str1)) # 11, len은 길이를 구합니다.(공백 포함)
print(str1[0]) # H
print(str1[3]) # l
print(str1[5]) # 공백
print(str1[9]) # l


# 슬라이싱

str2 = 'Hello world'
print(str2[0:1]) # H
print(str2[3:9]) # lo war
print(str2[:6]) # Hello
print(str2[8:]) # rld
print(str2[0] + str2[1] + str2[2] + str2[3] + str2[4]) # Hello


# .split()
str3 = 'H,e,l,l,o, ,w,o,r,l,d'
print(str3.split()) # ['Hello', 'world']
print(str3.split(',')) # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(str3.split(',' , 6)) # ['H', 'e', 'l', 'l', 'o', ' ', 'w,o,r,l,d']
print(str3.split(sep=',', maxsplit=6)) # ['H', 'e', 'l', 'l', 'o', ' ', 'w,o,r,l,d']

# seq, end
print('hello', 'hi', 'world', sep="/") # hello/hi/world
print('hello', 'hi', 'world', end="coding") #hello hi worldcoding  