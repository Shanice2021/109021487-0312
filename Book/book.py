class Book:
    def __init__(self, name, id, language, pages, price):
        self.BookName = name
        self.BookId = id
        self.BookLanguage = language
        self.BookPages = pages
        self.BookPrice = price
    def showinfo(self):
        print(self.BookName)
        print(self.BookId)
        print(self.BookLanguage)
        print(self.BookPages)
        print(self.BookPrice)
        

x1 = Book("三隻小豬", "0001", "Chinese", "588", "489")
x2 = Book("安徒生童話", "0002", "Chinese", "643", "699")
x3 = Book("The third alternative", "English", "256", "369", "500")

x1.showinfo()
x2.showinfo()
x3.showinfo()