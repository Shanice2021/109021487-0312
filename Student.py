class Student:
    def __init__(self, name, id):
        self.StuName = name
        self.StuId = id

x = Student("北北", "109021037")
y = Student("北北", "109021037")
 
print(x.StuName, "\t", x.StuId)
print(y.StuName, "\t", y.StuId)