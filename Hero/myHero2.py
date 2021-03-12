class Hero:
    def __init__(self, name, id, attack, defense, speed, blood):
        self.HeroName = name
        self.HeroId = id
        self.HeroAtk = attack
        self.HeroDefense = defense
        self.HeroSpeed = speed
        self.HeroHp = blood
def showinfo(x):
    print(x.HeroName, "\t", x.HeroId, "\t", x.HeroAtk, "\t", x.HeroDefense, "\t", x.HeroSpeed, "\t", x.HeroHp)
        

x1 = Hero("蝦蝦", "0001", "1", "100", "50", "100000")
x2 = Hero("蟹蟹", "0002", "10", "10", "5", "1000")
x3 = Hero("魚魚", "0003", "100", "1", "500", "10")
 
print(x1.HeroName, "\t", x1.HeroId, "\t", x1.HeroAtk, "\t", x1.HeroDefense, "\t", x1.HeroSpeed, "\t", x1.HeroHp)
print(x2.HeroName, "\t", x2.HeroId, "\t", x2.HeroAtk, "\t", x2.HeroDefense, "\t", x2.HeroSpeed, "\t", x2.HeroHp)
print(x3.HeroName, "\t", x3.HeroId, "\t", x3.HeroAtk, "\t", x3.HeroDefense, "\t", x3.HeroSpeed, "\t", x3.HeroHp)
