# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['lizhenye','buxizhou','peakli']
for name in names:
	print(name)
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
	sum=sum+x
print(sum)
# 注意一句话 有冒号的下一行往往要缩进，该缩进就缩进

# range(start, stop[, step])
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
sum = 0
list = list(range(101))
for i in list:
    print(i)
    sum += i
print(sum)

# while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

# break 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 小结

# 循环是让计算机做重复任务的有效的方法。

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，
# 都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

# 请试写一个死循环程序。
n = 0
while n>=-10000:
    print("n:",n)
    n -= 1