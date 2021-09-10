import unittest
from Vec3 import Vec3
import math


class TestVec3(unittest.TestCase) :

    def test_default(self) :
        a=Vec3()
        self.assertAlmostEqual(a.x,0.0)
        self.assertAlmostEqual(a.y,0.0)
        self.assertAlmostEqual(a.z,0.0)

    def test_user(self) :
        a=Vec3(1,2,3)
        self.assertAlmostEqual(a.x,1.0)
        self.assertAlmostEqual(a.y,2.0)
        self.assertAlmostEqual(a.z,3.0)

    def test_nonNumericCtor(self) :
        with self.assertRaises(ValueError) : 
            a=Vec3('a','b','c')

    def test_equal(self) :
        a=Vec3(0.1,0.2,0.3)
        b=Vec3(0.1,0.2,0.3)
        self.assertTrue(a==b)


    def test_add(self) :
        a=Vec3(0.1,0.1,0.2)
        b=Vec3(0.2,0.3,0.5)
        c=a+b
        self.assertAlmostEqual(c.x,0.3,5)
        self.assertAlmostEqual(c.y,0.4,5)
        self.assertAlmostEqual(c.z,0.7,5)

    def test_sub(self) :
        a=Vec3(0.2,0.3,0.4)
        b=Vec3(0.1,0.1,0.1)
        c=a-b
        self.assertAlmostEqual(c.x,0.1,5)
        self.assertAlmostEqual(c.y,0.2,5)
        self.assertAlmostEqual(c.z,0.3,5)

    def test_multScalar(self) :
        a=Vec3(0.2,0.3,0.4)
        c=a*2
        self.assertAlmostEqual(c.x,0.4,5)
        self.assertAlmostEqual(c.y,0.6,5)
        self.assertAlmostEqual(c.z,0.8,5)

    def test_multVector(self) :
        a=Vec3(0.2,0.3,0.4)
        b=Vec3(2,2,2)
        c=a*b
        self.assertAlmostEqual(c.x,0.4,5)
        self.assertAlmostEqual(c.y,0.6,5)
        self.assertAlmostEqual(c.z,0.8,5)
    def test_length(self) :
        a=Vec3(0.2,0.3,0.4)
        b=a.length()
        # https://onlinemschool.com/math/assistance/vector/length/
       # gives 0.5385164807134504 
        self.assertAlmostEqual(b,0.5385,4)

    def test_normalize(self) :
        a=Vec3(0.1,0.2,0.3)
        b=a.normalize()
        # result from here
        # https://calculator.academy/normalize-vector-calculator/#f1p1|f2p0
        self.assertAlmostEqual(b.x,0.2672,3)
        self.assertAlmostEqual(b.y,0.5345,3)
        self.assertAlmostEqual(b.z,0.8017,3)


    def test_zeroNormalize(self) :
        a=Vec3()
        with self.assertRaises(ZeroDivisionError) :
            a.normalize()
