class Chess:
    def __init__(self, name, color, quantity, id, English):
        self.ChessName = name
        self.ChessColor = color
        self.ChessQuantity = quantity
        self.ChessId = id
        self.ChessEnglish = English
    def showinfo(self):
        print(self.ChessName)
        print(self.ChessColor)
        print(self.ChessQuantity)
        print(self.ChessId)
        print(self.ChessEnglish)

x1 = Chess("將", "black", "1", "001", "General")
x2 = Chess("仕", "red", "2", "002", "official")
x3 = Chess("兵", "red", "5", "007", "Soldier")

x1.showinfo()
x2.showinfo()
x3.showinfo()