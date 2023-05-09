#example taken from https://www.mygreatlearning.com/blog/python-init/#:~:text=The%20python%20__init__%20method%20is%20declared%20within%20a,object%20of%20the%20class%20itself.
class Default():
    
    #defining parameterised constructor
    def __init__(self, n1, n2):
        self.var1 = n1
        self.var2 = n2
        
    #class function for addition
    def add(self):
        print("Sum is ", self.var1 + self.var2)

obj = Default(12, 13)              #Creating object for a class with parameterised init
obj.add()