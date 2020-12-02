"""
python的面向对象编程
"""

# 类对象
# 包含类的属性,类的方法
class MyClass:
    i = 123
    def f(self):
        return "hello world"

# 初始化类对象
x = MyClass()

# 访问对象的属性
print("MyClass Object property i :", x.i)
print("MyClass Object method :", x.f())