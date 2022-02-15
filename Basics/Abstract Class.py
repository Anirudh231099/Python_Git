import abc #abstract base class
#class Shape(metaclass=abc.ABCMeta): #ABCMeta Class
class Shape(abc.ABC): #ABC helper class
   @abc.abstractmethod
   def area(self): #Abstract Method Declaration
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())