'''The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.

Define these methods:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`'''

class Block():
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        volume = self.height * (self.height * self.width)
        return volume
        pass

    def get_surface_area(self):
        s_area = self.height * self.width
        return s_area
        pass

block1 = Block(2, 2, 2)

print(block1.get_surface_area())

#Struggling with this one