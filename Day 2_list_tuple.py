# 理解什么情况下会是True or False
print(bool("Ivan好帅")) # True
print(bool("Ivan好丑")) # True
print(bool(0)) # False
print(bool("_")) # 空格也是True

# 特殊False情况
print(bool("None")) # True
print(bool("none")) # True
print(bool(None)) # False


# if_else_语句练习
age = 19
has_ticket = True
is_vip = True
if (age >= 18 and has_ticket) or is_vip:
    print("欢迎来到迪士尼度假区")
else:
    print("抱歉，未通过")


# list语句练习（数据的存储与查看）
name_list = ["ivan","kitty","roby","mett"]
print(name_list)
print(name_list[0])