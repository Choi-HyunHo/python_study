# 할당
my_int = 1
my_float = 2.0
my_list = []

# 산술
print(1 + 2) # 3
print(14 - 5) # 9
print(2 * 2) # 4
print(12 / 3) # 4.0

# 특수 연산자
print(2 ** 2) # 2의 2제곱 : 4
print(8 // 3) # 8 나누기 3의 몫 : 2
print(8 % 2) # 8 나누기 2의 나머지 : 0

# 홀짝 구분
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number % 2 == 1:
        print(number, ': 홀수')
    else:
        print(number, ': 짝수')

        # 1 : 홀수
        # 2 : 짝수
        # 3 : 홀수
        # 4 : 짝수
        # 5 : 홀수
        # 6 : 짝수
        # 7 : 홀수

# 문자열
print('hello' + 'world') # helloworld
print('hello' + ' ' + 'world') # hello world

# 문자열 반복
print(('hello' + ' ' + 'world') * 3) # hello worldhello worldhello world


# 비교 연산자
print(3 < 4) # True
print(1 > 2) # False
print(11 == 11) # True
print(12 != 1) # True
print(4 <= 6) # True
print(7 <= 5) # False


# 논리 연산자
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not False) # True
print(not True) # False


# 포함 연산자

nums = [1,2,3,4,5]
print(1 in nums) # True
print(2 not in nums) # False
print(3 in nums) # True
print(4 not in nums) # False