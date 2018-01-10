class parent:
    def myPrntMethod(self):
        print("It's parent method")
    def myMethod(self):
         print("It's parent self method")
        
class child(parent):
    def mychildMethod(self):
        print("it's child method")
    def myMethod(self):
         print("it's child self method")
obj=child()
obj.myPrntMethod()
obj.mychildMethod()
obj.myMethod() #method overriding
