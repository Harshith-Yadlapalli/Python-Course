# class a:
#     def sum(self):
#         print("sum")
# class b(a):
#     def sum(self):
#         print("addition")
# c1=b()
# c2=a()
# c2.sum()
# c1.sum()

# class cal:
#     def __init__(self,val):
#         self.val=val
#     def __add__(self,another):
#         self.another=another
#         return (self.val)+(self.another)
# a=cal(20)
# b=cal(30)
# print(a+b)
""""        Polymorphism        """
# there are two types in polymorphism :- 
# mthod overloading and Mthodoveriding
"""     Method Overloading       """
# class c:
#     def method2(self,a,b,c=0,d=0):
#         return a+b+c+d
# o = c()
# print(o.method2(10,20))
# print(o.method2(1,2,3))
# print(o.method2(100,200,300,400))

# class c2:
#     def method3(self,*a):
#         return sum(a)
# b = c2()
# print(b.method3(1,2,3,4,5,6,7,8,9,10))

"""     Duck Typing     """
# class employee:
#     def work(self):
#         return "Employee is working"
# class developer:
#     def work(self):
#         return "developer is working"
# res = [employee(),developer()]
# for i in res:
#     print(i.work())

"""         Methodoveriding        """
class a:
    def m1(self):
        print("parent m1")
class b(a):
    def m1(self):
        print("child m1")
        super().m1()
c1 = b()
c1.m1()
a.m1(c1)