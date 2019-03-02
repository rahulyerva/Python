class car():
    def __init__(self,model,price,yearm):
        self.m = model
        self.p = price
        self.y = yearm
    def priceinc(self,h):
        self.y = h * 4

class SuperClass(car)
    pass
honda =  SuperClass("City", 100000, 2017)
print(honda.p)
honda.priceinc(4)
print(honda.y)