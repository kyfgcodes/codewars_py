import math
'''Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)

Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)'''


class Sphere(object):
    def __init__(self,radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = (1.3333333 * math.pi) * self.radius ** 3
        #Calculation not right: Should be 33.51032

        return round(volume, 5)
        pass

    def get_surface_area(self):
        s_area = (4 * math.pi) * self.radius ** 2

        return round(s_area, 5)

        pass

    def get_density(self):
        density = self.mass /  ((1.33333 * math.pi) * (self.radius ** 3))
        
        return round(density, 5)

        pass

ball = Sphere(2, 50)

print(ball.get_volume())

#Struggling with this one
