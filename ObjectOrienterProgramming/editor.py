
class editor:

    name=str

    vendor=str

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def __str__(self):
       
       return self.vendor

    def display(self):
      print(self.name,self.vendor)

editor_instance1=editor("pycharm","jebrains")
editor_instance2=editor("intellij","jetbrains")
editor_instance3=editor("vscode","microsoft")

print(editor_instance2)
