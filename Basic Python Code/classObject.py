class myclass:
    w=0
    b=0
    o=0
    def __init__(self,name):
        myclass.name=name

    def ck_color(self):
        print("Enter your Car's color name:")
        myclass.color=input()
        if myclass.color=="black":
            myclass.b+=1
        elif myclass.color=="white":
            myclass.w+=1
        else:
            myclass.o+=1
    def display(self):
        print("Hey,",myclass.name)
        print("black color size",myclass.b)
        print("white color size",myclass.w)
        print("Other color size",myclass.o)
print("Enter your name:")
obj=myclass(input())
obj.ck_color()
obj.display()
        
