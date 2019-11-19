list/generator question
================
for x in list_a for y in list_b
tuple(x for x in list_a)
1. 此处是按照x进行排序
2. 写法可以连在一起，等同两个for缩进写法
3. 当表达式为函数调用的唯一参数时，不需要额外加()



tuple
============================
元组拆包
1. x, y, z = tuple(1, 2, 3)
2. 一种优雅的交换变量的方式
    a, b = b, a
3. 