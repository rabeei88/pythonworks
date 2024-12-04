
class animal:

    name=str

    species=str

    def __init__(self,name,species):

        self.name=name

        self.species=species

    def __str__(self):

            return self.name
    
class lion(animal):
    def __init__(self,name,species):
          super().__init__(name, species)

    def sound(self):
         print("ggggrrrrrr")   

lion_instance=lion("lion","carnivorous")
print(lion_instance)
print(lion_instance.sound())


class cat(animal):
    def __init__(self, name, species):
          super().__init__(name, species)

    def sound():
         print("meaowwwwww") 

       

     
        