"""
python面向对象编程之继承
"""

# 基类对象
class people:

    # 属性
    name = ''
    age = 0
    # 私有属性
    __weight = 0

    # 定义构造方法
    def __int__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    # 定义方法
    def speak(self):
        print("s 说: 我 %d 岁。" % (self.name, self.age))

# 单继承
class student(people):
    # 属性
    grade = ''

    # 继承people的属性并初始化
    def __init__(self,n,a,w,g):
        people.__int__(self,n,a,w)
        self.grade = g

    # 冲洗父类方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法