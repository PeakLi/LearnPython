# 函数就是最基本的一种代码抽象的方式。
# 调用函数
help(abs)
print(abs(-1.23))
# 参数个数、类型都得正确否则会报TypeError的错误

# abs
# 取绝对值
abs(-1.29)
# max 
# max函数max()可以接收任意多个参数，并返回最大的那个：
a = max(1,12.3,-1.2,-4)
print(a)

# 数据类型转换
# int()
# 函数可以把其他数据类型转换为整数：
a = int('123')
print(a)
a = int(12.3)
print(a)
a = float('12.3')
print(a)
a = str(12.3)
print(a)
a = str(100)
print(a)
a = bool(1)
print(a)
a = bool('')
print(a)
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-13.1))
# 练习 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
help(hex)
n1 = 255
n2 = 1000
s = str(hex(n2))
print(s)
print(3*16*16+14*16+8)

