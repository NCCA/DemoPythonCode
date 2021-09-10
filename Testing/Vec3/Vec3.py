import math
class Vec3 :
    def __init__(self, x=0.0, y=0.0,z=0.0) :
        try :
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except ValueError as e:
            raise ValueError("this class only accepts numeric values") from e
    def __str__(self) :
        return '{} {} {}' .format(self.x,self.y,self.y)
    def __eq__(self,rhs) :
        return self.x==rhs.x and self.y == rhs.y and self.z == rhs.z
    def __add__(self,rhs) :
        return Vec3(self.x+rhs.x,self.y+rhs.y,self.z+rhs.z) 
    def __sub__(self,rhs) :
        return Vec3(self.x-rhs.x,self.y-rhs.y,self.z-rhs.z)
    def __mul__(self,rhs) :
        if isinstance(rhs,Vec3) :
            return Vec3(self.x*rhs.x,self.y*rhs.y,self.z*rhs.z)
        else :
            return Vec3(self.x*rhs,self.y*rhs,self.z*rhs)

    def length(self)  :

        return math.sqrt(((self.x*self.x) + (self.y*self.y) + (self.z*self.z)))
    def normalize(self) :
        length=self.length()
        return Vec3(self.x/length,self.y/length,self.z/length)

