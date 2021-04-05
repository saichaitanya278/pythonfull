class Student:
    counter = 0

    def init(self, id, f_name, l_name, course, year, gpa, university, email, mobile):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        self.email = email
        self.mobile = mobile
Student.counter += 1

def getNewEmail(self):
        self.email = self.f_name+self.l_name+"@gmail.com"
        print(self.f_name + self.l_name + "@gmail.com")


student1 = Student(7, "sumanth", "S", "CSE", 2022, 9,
                   "klh", "sumanth.s@klh.edu.in", 9852128936)
student2 = Student(10, "hruthik", "B", "CSE", 2022, 9.1,
                   "klh", "hruthik.b@klh.edu.in", 45250128936)
student3 = Student(110, "ak", "T", "CSE", 2022, 8.8, "klh",
                   "ak.t@klh.edu.in", 955125936)

print(student2.getNewEmail())
print("Total number of objects created: ", Student.counter)
