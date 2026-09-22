"""         Single Inheritance      """
# class emp:
#     def work(sect): 
#         print("working")
# class dev:
#     def develope(self): 
#         print("Developing")
# d = dev()
# d = emp()
# d.work()
# d.develope()

"""        Multiple Inheritance         """
# class emp:
#     def work(sect): 
#         print("working")
# class dev:
#     def develope(self): 
#         print("Developing")
# class test(emp,dev): 
#     def tester(self): 
#         print("Testing")
# t= test()
# t.develope()
# t.work()
# t.tester()

"""        Multi Level      """
# class emp:
#     def work(sect): 
#         print("working")
# class dev(emp):
#     def develope(self): 
#         print("Developing")
# class test(dev): 
#     def tester(self): 
#         print("Testing")
# t= test()
# t.develope()
# t.tester()
# t.work()

"""         Hierarchical Inheritance        """
# class company:
#     def rules(self):
#         print("follow the ccompany rules")
# class HR_Team:
#     def hiring(self):
#         print("hiring the employees")
# class Frontend_team(company):
#     def design(self):
#         print("designing the website")
# class Backend_team(company): 
#     def python_operations(self):
#         print("writing the python code to develope the company")
# hr = HR_Team()
# f = Frontend_team()
# b = Backend_team()
# f.design()
# hr.hiring()
# b.python_operations()
# b.rules()

"""         Hybrid Inheritance          """
# class company:
#     def rules(self):
#         print("follow the ccompany rules")
# class HR_Team(company):
#     def hiring(self):
#         print("hiring the employees")
# class Frontend_team(company):
#     def design(self):
#         print("designing the website")
# class Backend_team(company): 
#     def python_operations(self):
#         print("writing the python code to develope the company")
# class clients(HR_Team,Backend_team):
#     def meetups(self):
#         print("Client meetings")
# client = clients()
# hr = HR_Team()
# f = Frontend_team()
# b = Backend_team()
# f.design()
# hr.hiring()
# b.python_operations()
# b.rules()
# client.meetups()

# class company:
#     def rules(self):
#         print("follow the ccompany rules")
# class HR_Team(company):
#     def hiring(self):
#         print("hiring the employees")
# class Frontend_team(company,HR_Team):
#     def design(self):
#         print("designing the website")
# front = Frontend_team()
# front.design()
# front.hiring()
# front.rules()

class company:
    def rules(self):
        print("follow the ccompany rules")
class HR_Team(company):
    def hiring(self):
        print("hiring the employees")
class Frontend_team(HR_Team,company):
    def design(self):
        print("designing the website")
front = Frontend_team()
front.design()
front.hiring()
front.rules()


"""         super method()"""
# class A:
#     def method(self):
#         print("this is parent method")
# class B(A): 
#     def method(self):
#         super().method()
#         print("this is child")
# b = B()
# b.method()