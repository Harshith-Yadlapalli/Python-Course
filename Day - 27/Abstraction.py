from abc import ABC, abstractmethod
# class shape(ABC): 
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side = side
#     def square_details(self):
#         return f'square side is {self.side}'
#     def area (self):
#         area = self.side*self.side
#         return area
#     def perimeter(self):
#         p = 4*self.side
#         return p
# class rectangle(shape): 
#     def __init__(self,length,width):
#         self.length = length 
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*(self.length+self.width)

# square = square(4)
# print(square.area())
# print(square.perimeter())
# print(square.square_details())
# print()
# rectangle = rectangle(10,5)
# print(rectangle.area())
# print(rectangle.perimeter())


class features:
    @abstractmethod
    def messenger(self):
        pass
    @abstractmethod
    def Calls(self):
        pass
    @abstractmethod
    def search(self):
        pass

class whatsapp(features):
    def messenger(self):
        print("Whatsapp Messenger")
    def Calls(self):
        print("Whatsapp Calls")
    def search(self):
        print("Whatsapp Searches")
    def status(self):
        print("Status uploaded")
class instagram(features):
    def messenger(self):
        print("Instagram Messenger")
    def Calls(self):
        print("Instagram Calls")
    def search(self):
        print("Instagram Searches")
    def reels(self):
        print("Reels")
    
w=whatsapp()
w.Calls()
w.messenger()
w.search()
w.status()
print()
i=instagram()
i.search()
i.messenger()
i.Calls()
i.reels()
