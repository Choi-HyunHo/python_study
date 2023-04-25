# while
count = 0
while count < 5:
    print('반복 ', count)
    count += 1

    # 반복  0
    # 반복  1
    # 반복  2
    # 반복  3
    # 반복  4

# break
num = 0
while num < 5:
    num += 1
    if(num == 3):
        break # 반복 2 이후로 빠져나가서 멈춥니다.
    else:
        print('반복 ', num)

        # 반복  1 
        # 반복  2

# continue
my_num = 0
while my_num < 10:
    my_num += 1
    if my_num < 4:
        print('ing ', my_num)   
        # ing  1
        # ing  2
        # ing  3
        continue
    if my_num == 8:
        print('end' , my_num) 
        # end 8
        break