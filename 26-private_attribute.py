class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __ -> private

    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = Account(1234, "abcd")
print(acc1.acc_no)
print(acc1.reset_pass())

