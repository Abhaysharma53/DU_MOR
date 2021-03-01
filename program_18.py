class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
    def printemp_id(self):
        print('In Employee Class, The employee ID is', self.emp_id)
        
class Manager(Employee):
    def __init__(self,emp_id, fname, lname):
        super().__init__(emp_id)
        self.fname = fname
        self.lname = lname
    def printmanager(self):
        print('In Manager class, The emp_id is ',self.emp_id,' and the firstname and lastname are - ',self.fname,self.lname)
        
class Clerk(Employee):
    def __init__(self, emp_id,fname, lname):
        super().__init__(emp_id)
        self.fname = fname
        self.lname = lname
    def printclerk(self):
        print('In Clerk Class, The emp_id is ',self.emp_id,' and the firstname and lastname are - ',self.fname,self.lname)
        


obj1 = Employee('1601')
obj1.printemp_id()
obj2 = Manager('1602','Abhay','Sharma')
obj2.printmanager()
obj3 = Clerk('1603','Mohd','Anas')
obj3.printclerk()