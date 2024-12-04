
class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)

class StandardShipping(Shipping):
    def calculate_shipping_cost(self,weight):
     print(weight*10)

express_instance=ExpressShipping()
express_instance.calculate_shipping_cost(20)

standard_instance=StandardShipping()
standard_instance.calculate_shipping_cost(10)



