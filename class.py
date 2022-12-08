class Shape:
    def __init__(self,name):
        self.name=name
obj = Shape(name = "I shape")
print(obj)

class Square(Shape):
    def __init__(self, name='zero', side1=4):
        super().__init__(name)
        self.side = side1
    def s(self):
        return self.side**2
print(Square().s()) 
#print(Square(side1=5).s()) 

class Pryamoygolnik(Shape):
    def __init__(self, name="none", side2=6, side3=3):
        super().__init__(name)
        self.side = side2
        self.side1 = side3
    def S(self):
        return self.side1*self.side
print(Pryamoygolnik().S())

from math import pi
class Okruzhnost(Shape):
    def __init__(self, name="like",side4=5):
        super().__init__(name)
        self.side=side4
    def So(self):
        return self.side**2*pi
print(Okruzhnost().So())

import unittest
class TestShapeMethods(unittest.TestCase):
    def test_none(self,name="zero"):
        G = Square(name,side1=7)
        i=49
        self.assertTrue(G.s()==i)
        self.assertEqual(G.s(),i)

    def test_two(self,name="zero"):
        G = Pryamoygolnik(name,side2=7,side3=9)
        i=63
        self.assertTrue(G.S()==i)
        self.assertEqual(G.S(),i)

    def test_tri(self,name="zero"):
        G = Okruzhnost(name,side4=9)
        i=pi*9**2
        self.assertTrue(G.So()==i)
        self.assertEqual(G.So(),i)

if __name__ == '__main__':
    unittest.main()

