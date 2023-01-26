class Emp:
    comp ="visa"
    e_code = 12456
class Freelancer:
    comp = "Fiver"
    level = 3
    def upgradeLevel(self):
        self.level += 1

class Programmer (Emp,Freelancer): # Parental class Priority Emp>Freelancer (bcz emp assign 1st then freelancer)

    name = "Rohit"
    

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.e_code)
print(p.comp)







