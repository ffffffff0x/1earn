import random

print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# 返回随机生成的一个实数，它在[0,1)范围内。
print(random.random())
print((random.random()*21)+100)
print(random.uniform(100, 101))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ",  list)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


print ("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))

