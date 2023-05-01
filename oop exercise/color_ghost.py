'''Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated'''

class Ghost(object):
    def __init__(self, color):
        self.color = color
    
    def color(self):
        if self.color in range(100):
            self.color = 'yellow' or 'white' or 'purple' or 'red'

#Struggling with this one
    