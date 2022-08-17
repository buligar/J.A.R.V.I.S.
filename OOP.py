class Car():
    man_name= None
    color2 = None
    def __init__(self,color,name):
        self.name = name
        self.color = color



car1 = Car("Blue","Toyota")
car2 = Car("Red","Mazda")

car1.man_name = "Oleg"
print(car1.color,car2.color)
if car1.color == "Red":
    car2.color2 = "Blue"
print(car1.color,car2.color2)
print(car1.man_name)
print(car2.man_name)