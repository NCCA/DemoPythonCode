#!/usr/bin/python

from Sphere import Point3,Colour,Sphere,Ellipse

#Pos, colour, radius,name
s1=Sphere(Point3(3,0,0),Colour(1,0,0,1),2,"Sphere1")
s1.Print()

p1=Point3(3,4,5)
c1=Colour(1,1,1,1)
s2=Sphere(p1,c1,12,"New")
s2.Print()


s3=Sphere(Point3(3,0,2),Colour(1,0,1,1),2,"Sphere2")
s3.Print()

e1=Ellipse()
e1.Print()