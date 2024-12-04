
class grandparent:
    def m(self):
        print("grandparent class m method")

class parent:
    def m(self):
        print("parent class m method")

class child(parent,grandparent):
    def m3(self):
        print("child class m3 method")

child_instance=child()
child_instance.m3()
child_instance.m()

# here both parent & grandparent define (m) so python handle inherit orderwise
