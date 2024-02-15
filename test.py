def describe_pet(animal_type, pet_name):
    
    print(f"I have {animal_type.title()}")
    print(f"{pet_name.title()} is my pet")
    
describe_pet("rockiet", "rocky")

#8-3. 
# T-Shirt: Write a function called make_shirt() that accepts a size and the 
#text of a message that should be printed on the shirt. The function should print 
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the 
#function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"{size} should be size of my shirt")
    print(f"Make a beautiful design text like: {text.upper()}")
    
make_shirt(12, "you are born great")

#8.4
def make_shirtt():
    