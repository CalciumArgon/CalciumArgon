##### 函数/方法 笔记

### 1. collections.deque()
## 优势: 入栈和出栈都是 O(1), 且支持各种操作
print("\n=====================================\n")

import collections
q = collections.deque([23,64,8,-13,0,43])        # deque()内部只有一个列表元素

q.clear()
q.extend([1,3,4,6,6])

q.appendleft(0)
q.append(7)

q.popleft()
q.pop()

n = 2
q.rotate(n)         # 顺时针转动 n 次
q.rotate(-1)        # 逆时针转动一次
print(q)        # deque([6, 1, 3, 4, 6])

q1 = q.copy()
print("q 的地址为: {}, 其副本 q1 的地址为: {}".format(id(q), id(q1)))

q.reverse()             # deque([6, 4, 3, 1, 6])
q.insert(1, 0)          # deque([6, 0, 4, 3, 1, 6])

print("6 的个数是: {}\n1 的个数是: {}".format(q.count(6), q.count(1)))

# 区间查找 list.index(Object, a, b) 在(a, b)区间内查找 Object 的索引
print("4 的位置是: {}".format(q.index(4,1,3)))          # 在(1,3)的范围内查找4的索引

q.remove(6)             # deque([0, 4, 3, 1, 6])    # 一次删除一个值

print("\n=====================================\n")

### 2. Sortedlist()
## 构建时刻排好序的数列

from sortedcontainers import SortedList

l = SortedList([2,5,3,1,8,4,9])
print(l)        # SortedList([1, 2, 3, 4, 5, 8, 9])

l.add(-1)
print(l)        # SortedList([-1, 1, 2, 3, 4, 5, 8, 9])


xs = {"ab":1, "cc":3}
xs["ab"] -= 1
print(xs)
xs["ccc"] -= 1