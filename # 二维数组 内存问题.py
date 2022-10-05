# 二维数组 内存问题

# 用 * 来定义数组会带来相同的储存地址
# list dict 等结构中的元素可被修改, 因此list本身存储地址不会改变
# 而str tuple不能修改, 因此实际"修改"list中元素时所做的是"重赋值", 即重建一个新地址
a = [[0]*3] * 3

print(id(a))                                        # X
print(id(a[0][0]), id(a[1][0]), id(a[2][0]))        # A A A
print(id(a[0][1]), id(a[1][1]), id(a[2][1]))        # A A A

a[2][1] = -1
print(a)    # [[0, -1, 0], [0, -1, 0], [0, -1, 0]]

print(id(a))                                        # X
print(id(a[0][0]), id(a[1][0]), id(a[2][0]))        # A A A
print(id(a[0][1]), id(a[1][1]), id(a[2][1]))        # B B B