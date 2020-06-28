"""The __init__ method is similar to constructors in C++ and Java. Constructors
 are used to initialize the object’s state. The task of constructors is to 
 initialize(assign values) to the data members of the class when an object of 
 class is created.
 
 Like methods, a constructor also contains collection of statements(i.e. 
 instructions) that are executed at time of Object creation.It is run as soon as 
 an object of a class is instantiated. The method is useful to do any initializ
 ation you want to do with your object."""
 #https://www.geeksforgeeks.org/__init__-in-python/
 

class Computer:
    def __init__(self,cpu,ram,hdd):
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
    
    def config(self):
        print(self.cpu,self.ram,self.hdd)
        
comp1=Computer("corei5","8GB","1TB HDD")    
comp2=Computer("corei7","16GB","1TB HDD")

comp1.config()
comp2.config() 



#**********another example*************
#https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

class Car(object):
  """
    blueprint for car
  """
  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    

  def change_gear(self, gear_type):
    print("gear changed")
  
  def showinfo(self):
      print(self.model,self.color,self.company,self.speed_limit)
    
#Lets try to create different types of cars
maruthi_suzuki = Car("Ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

maruthi_suzuki.showinfo()
audi.showinfo()




