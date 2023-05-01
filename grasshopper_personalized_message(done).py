'''Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

case	                return
name equals owner	    'Hello boss'
otherwise	            'Hello guest'
'''

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    return "Hello guest"

print(greet("Daniel","Daniel"))

#Done!!!!