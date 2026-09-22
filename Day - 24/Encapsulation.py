# class company: 
#     def __init__(self,emp_name,emp_id,emp_salary):
#         self.emp_name = emp_name
#         self._emp_id = emp_id
#         self.__emp_salary = emp_salary

#     def emp_salaries(self):
#         return self.__emp_salary

#     def emp_details(self): 
#         print(f"employee name {self.name}, emp_id is {self.emp_id}")

# employee1 = company("Nayan",100,25000)
# print(employee1.emp_name)
# print(employee1._emp_id)
# print(employee1.emp_salaries())
# #print(employee1.emp_salaries)

class company: 
    def main_agenda(self):
        print("Abstract of company")

    def client(self):
        print("clients")

    def CEO(self):
        print("I am the CEO")

class cloud_company(company):
    def cloud(self):
        print("Comapany data in the cloud")

c = cloud_company()
c.main_agenda()
c.cloud()

class company: 
    def __init__(self,company_name,location,x):
        self.company_name = company_name
        self._location = location
        self.__x = x
    def main_agenda(self):
        print("Abstract of company")

    def client(self):
        print("clients")

    def CEO(self):
        print("I am the CEO")

class cloud_company(company):
    def cloud(self):
        print("Comapany data in the cloud")
    def comapany_details(self):
        print(f"Company name is {self.company_name} adn location is at {self._location}")
        print(self._company__x)

c = cloud_company("Google","Hyderabad","woooo")
c.main_agenda()
c.cloud()
c.comapany_details()
c.comapany_details()