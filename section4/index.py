# 빈 리스트
list1 = []
print(type(list1)) # <class 'list'>

# 값을 가지고 있는 리스트
list2 = ['a','b','c']
print(list2) # ['a', 'b', 'c']

# .append()
list3 = [1,2,3]
list3.append(4)
list3.append(5)
list3.append(6)
list3.append('hi')
print(list3) # [1, 2, 3, 4, 5, 6, 'hi']

# .del

list6 = [1,2,4,5,6,7]
del(list6[2:])
print(list6)

# 인덱싱
list4 = [1,2,3,4,5]
print(list4[0]) # 1
print(list4[2]) # 3


# 마이너스를 사용하면 뒤에서부터 순서대로 가져옵니다.
print(list4[-1]) # 5
print(list4[-3]) # 3

# 슬라이싱
list5 = [1,2,4,5,6,7]
print(list5[::2]) # [1, 4, 6]

list5[2:4] = [99,100]
print(list5) # [1, 2, 99, 100, 6, 7]
