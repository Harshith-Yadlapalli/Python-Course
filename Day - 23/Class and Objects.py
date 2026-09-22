class pfs_66:
    python_falculty = "Nandini"
    def __init__(self,name,roll_no,marks):          # This is Constructor
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def student_details(self,dept):
        self.dept = dept
        print(f"Name is {self.name}, Roll_no. is {self.roll_no}, and marks is {self.marks}, from dept of {self.dept}")
    def exam(self):
        print("exam")
    def attendance(self):
        print("attending the class")
    def assignment(self):
        print("assignment")
    def python_weeklyexam(self):
        print("python Weekly Exam")
student1 = pfs_66("dileep",202,435)
student1.exam()
student1.assignment()
student1.student_details("PFS-66")
student1.attendance()
print()
student2 = pfs_66("rajesh",203,897)
student2.student_details("PFS-66")

class employee:
    def __init__(self,name,id,salary,age):
        self.name = name
        self.id = id
        self.salary = salary
        self.age = age
    def employee_details(self):
            print(f"Employee name is {self.name}, his employee_id is {self.id}, and his salary is {self.salary} and the age is {self.age}")
    def hike(self,hike):
        self.hike = hike
        print(f"Hike of {self.hike}%, for the employee {self.name}")
employee1 = employee("Nayan",500,20000,21)
employee2 = employee("yadagiri",501,25000,23)
employee3 = employee("ruthvik",502,100000,19)
employee4 = employee("harshith",503,45000,22)
employee1.employee_details()
employee1.hike(10)
print()
employee2.employee_details()
employee2.hike(10)
print()
employee3.employee_details()
employee3.hike(30)
print()
employee4.employee_details()
employee4.hike(20)