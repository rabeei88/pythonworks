
class BankAccount:

    def __init__(self,customer_name,mpin,account_type,balance):
        
        self.customer_name=customer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance

    def get_mpin(self):
        print(self.__mpin)

    def get_balance(self):
        print(self.__balance)

    def __str__(self):
        return self.customer_name
    

bank_accnt_instance=BankAccount("rabi",5230,"savings",50)
print(bank_accnt_instance)
bank_accnt_instance.get_balance()
bank_accnt_instance.get_mpin()


#  *,+ perform string operation



