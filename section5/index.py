colors = ['blue', 'red', 'green', 'yellow']

for color in colors : 
    print(color)

    # blue
    # red
    # green
    # yellow

for num in [1,2,3] :
    print(num)

    # 1
    # 2
    # 3

for name in 'hyunho' : 
    print(name)

    # h
    # y
    # u
    # n
    # h
    # o


# range
for num in range(1, 5) :
    print(num)

    # 1
    # 2
    # 3
    # 4

for sum in range(2, 10, 2) :
    print(sum)

    # 2
    # 4
    # 6
    # 8

for value in range(10, 2, -2) : 
    print(value)
    
    # 10
    # 8
    # 6
    # 4

for i in range(1, 10):
    print('{}x{}={}'.format(2, i, 2 * i))

    # 2x1=2
    # 2x2=4
    # 2x3=6
    # 2x4=8
    # 2x5=10
    # 2x6=12
    # 2x7=14  
    # 2x8=16
    # 2x9=18

# 구구단 출력 예시
for i in range(2, 10) :
    for j in range(1, 10) : 
        print('{}x{}={}'.format(j, i, j * i))


# 리스트 컴프리헨션
nums = []
for num in range(1, 11) :
    nums.append(num)

print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([num for num in range(1,11)]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([num * 2 for num in range(1,11)]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]