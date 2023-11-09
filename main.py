#OOPS(Object Oriented Programming)
# class is a blueprint of object . means  contains all the details  and functionalities about object
class  car:
  def __init__(self,a,b,c):
    self.name=a
    self.year=b
    self.speed=c
  def speedup(self):
    self.speed=self.speed+20
  def small(self):
    print("small bike")
class bike(car):
  def __init__(self,a,b,d):
    self.name=a
    self.speed=b
    self.colour=df test(self):
    print("this is just a test function")

car1=car("safari",1992,300) # object ceration
car2=car("audi",1092,500) # object ceration
print(car1.speed,car2.speed,car1.name)
car1.speed=34
print(car1.speed)
car1.speedup()
print(car1.speed,car2.speed)
c=bike("yemaha",100,"black")
c.speedup()
c.small()
print(c.colour)
print(c.speed)

