class Employee:
    e_id=0;
    e_name=""
    def __init__(self,e_id,e_name):
        self.e_id = e_id
        self.e_name = e_name
        
    def display(self):
        print("Employee ID ",self.e_id," Employee Name: ",self.e_name)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name," destroyed.")

#Object Created
E = Employee(23545,"QWERTY")
E2 = Employee(56436,"RAM")
E3 = Employee(47367,"GOPAL")
E.display()
E2.display()
E3.display()
#Destroy Of Objects.
print(id(E),id(E2),id(E3))

del E
del E2
del E3
