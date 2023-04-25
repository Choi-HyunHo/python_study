# 함수 정의 및 호출
# def myfunc():
#     print('hello function')

# myfunc() # hello function

# # 파라미터, 인수
# num1 = 10
# num2 = 20
# def sum(val1, val2):
#     print(val1 + val2) # 30

# sol = sum(num1, num2)
# print(sol) # none

# # return
# def sum(val1, val2):
#     result = val1 + val2
#     return result

# solution = sum(num1, num2)
# print(solution) # 30

# 기본값 설정
def avg(val1=10, val2=20):
    return val1 + val2

result = avg()
print(result) # 30

result2 = avg(30);
print(result2) # 50

def avg2(val1, val2, val3=20):
    return val1 + val2 + val3

result3 = avg2(10, 30)
print(result3) # 60