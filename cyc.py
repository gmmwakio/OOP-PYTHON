#super class bicycle
class bicycle:
    def __init__(self,manufacturer,size,color,serial_no): #attributes 
        self.manufacturer = manufacturer
        self.size = size
        self.color = color
        self.__serial_no = serial_no

    def color_d(self): #Color Method
        print(f"This bike is  color {self.color}")

    def size_d(self): #Size Method
        print(f"This bike is of size {self.size}")

    def brand(self): #Brand Method
        print (f"This is a {self.manufacturer} bike")

    def get_serial(self):
        return self.__serial_no

b1 = bicycle('Colnago',29,'blue',453)
b2 = bicycle('Giant',27.5,'black',56)
b3 = bicycle('Carerra',26,'blue',987)


b1.brand()
b2.color_d()
b3.size_d()

class MTB(bicycle):#Child class to class bicycle
    def __init__(self, manufacturer, size, color,suspension, serial_no):
        super().__init__(manufacturer, size, color, serial_no)
        self.suspension = suspension

    def susp(self): #Suspension method 
        print(f"This is an MTB with a {self.suspension} suspension")

b4 = MTB('BMW',20,'grey', 'rigid',78) 

b4.susp()
print(f"The serial number is",b3.get_serial())

