age = 7
if age >= 18:
    print('your age is', age)
    print('adult')
elif age>6:
	print('小学生呀')
else:
	print('小屁孩')
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是teenager：
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if 'd':
    print('True')

if '':
	print('True')
else:
	print('False')
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = input('请输入您的身高：')
height = float(height)
weight = input('请输入您的体重：')
weight = float(weight)
s = weight/(height * height)
if s > 32:
	print('严重肥胖')
elif s >= 28:
	print('肥胖')
elif s >= 25:
	print('过重')
elif s >= 18.5:
	print('正常')
else:
	print('过轻')
