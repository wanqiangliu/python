#1-10的平方数
squares = []
for square in range(1,11):
	squares.append(square**2)
print(squares)
print("----------------\n")
#平方数组中最小、最大、所有元素之和
print(min(squares))
print(max(squares))
print(sum(squares))
print("----------------\n")
#列表解析 (使代码更加简洁)
squares = [ square**2 for square in range(1,21) ]
print(squares)