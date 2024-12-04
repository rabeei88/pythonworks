class SuperHero:

    name:str

    suit:str

    def __init__(self,name,suit):

        self.name=name

        self.suit=suit

    def __str__(self):

        return self.name


class SpiderMan(SuperHero):

    def __init__(self, name, suit):
        super().__init__(name, suit)

    def super_power(self):
        print("stickyy handss")

SpiderMan_instance=SpiderMan("SPIDER MAN","SPIDER MAN SUIT")

print(SpiderMan_instance)

SpiderMan_instance.super_power()



class MinnalMurali(SuperHero):

    def __init__(self,name,suit):
        super().__init__(name,suit)

    def super_power(self):
        print("speedy run")

minnalmurali_instance=MinnalMurali("MINNAL MURALI","MINNAL MURALI SUIT")

print(minnalmurali_instance)

minnalmurali_instance.super_power()