def adLibs(): # you write a function using def
    adj = 'Happy'
    verb = 'Sleeping'
    object = 'Dinosaur'
    TOD = 'Morning'
    location = 'Bedrock'

    print(f"The {object} was {adj} ")
    print(f"He was {verb} until {TOD}")
    print(f'the {object} was a resident of {location}')

adLibs() # you can call a function many times
adLibs() # the naming conventions of a function is the same as variables
adLibs() # use functions so the code is cleaner and much more optimized

def arithmetic():
    return 5 * 15 # use return to return a value back

result = arithmetic()
print(result) # you can assign the value into a variable
print(arithmetic()) # or just return it directly

#arguments and parameters
def username(user = "Viper"): # user is a parameter because it is listed inside the parantheses of the function
    print(f'Hello {user}')

username('Kelsier') # all of these are arguments because we are using it to call upon the function
username('Will')
username("Kristen")
username() # you can assign a set value to the parameter and if you dont have an argument it just uses the default value

def avatar(ava, name): # if there are 2 parameters
    print(ava + " " + name)

avatar("Avatar", "Aang") # you also have to have 2 arguments or else it will cause an error

