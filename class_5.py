class Human:
    'This class is belongs to method overloading.'
    def sayHello(self, name=None):
        if name is not None:
            print('Hello '+ name)
        else:
            print('Hello')

obj = Human()

obj.sayHello() #No parameter

obj.sayHello("Qwerty") #Parameter Present