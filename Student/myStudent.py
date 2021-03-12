class Student:
    def __init__(self, name, id, kg, cm, gender):
        self.StudentName = name
        self.StudentId = id
        self.StudentKg = kg
        self.StudentCm = cm
        self.StudentGender = gender
    def showinfo(self):
        print(self.StudentName)
        print(self.StudentId)
        print(self.StudentKg)
        print(self.StudentCm)
        print(self.StudentGender)
        

x1 = Student("北北", "01", "77", "177", "boy")
x2 = Student("東東", "02", "66", "166", "boy")
x3 = Student("西西", "03", "60", "160", "girl")

x1.showinfo()
x2.showinfo()
x3.showinfo()