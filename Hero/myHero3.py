class Hero:
    def __init__(self, name, id, attack, defense, speed, blood):
        self.HeroName = name
        self.HeroId = id
        self.HeroAtk = attack
        self.HeroDefense = defense
        self.HeroSpeed = speed
        self.HeroHp = blood
    def showinfo(self):
        print(self.HeroName)
        print(self.HeroId)
        print(self.HeroAtk)
        print(self.HeroDefense)
        print(self.HeroSpeed)
        print(self.HeroHp)
        

x1 = Hero("蝦蝦", "0001", "1", "100", "50", "100000")
x2 = Hero("蟹蟹", "0002", "10", "10", "5", "1000")
x3 = Hero("魚魚", "0003", "100", "1", "500", "10")

x1.showinfo()
x2.showinfo()
x3.showinfo()