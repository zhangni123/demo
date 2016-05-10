class Shape(object):
    def area(self):
        pass
       
class Ellipse(Shape):
    l = 3.141592653
    def __init__(self, a=0, b=0):
        super().__init__()
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b * self.l
                
class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)

class Rectangle(Shape):
    def __init__(self, length=0,width=0):
        super().__init__()
        self.length = length
        self.width = width   
    def area(self):
        return self.length * self.width
                
class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
              
shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)] 
total_area = compute_area(shapes)
print('total_area: ', total_area)