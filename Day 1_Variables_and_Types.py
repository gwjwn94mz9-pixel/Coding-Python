# print语句练习
print(123)
print(456)
print("I love u")

"""
8.7 Python练习 print语句练习
- print 123
- print 456
- print I love u
"""
print(123)
print(456)
print("I love u")


# 变量定义和print练习
money = 50
print("钱包里还有： ", money, "元")


# 变量小练习
money = 50
print("当前钱包余额： ", money,"元")
print("购买了冰淇淋，花费了： ", 10,"元")
print("购买了可乐，花费了： ", 10,"元")
print("最终钱包剩余： ", money - 20,"元")


# type()语句套娃练习
money = 50
money_type = type(money)
print(money_type)


# 将数字转换为字符串
num_str = str(1314)
print(type(num_str), num_str)


# 将字符串转换为数字
str_num = int("963")
print(type(str_num), str_num)


# 将字符串转换为浮点数
str_float = float("13.14")
print(type(str_float), str_float)


"""
# 将字符串转换为数字的错误示范
str_num = int("ivanhu963")
print(type(str_num), str_num)
"""