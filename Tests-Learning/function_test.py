# Test function
# def means define a function
# describeRoom is the function's name
# () means it currently receives no arguments
# : begins the function body
# The indented line belongs to the function
# Defining a function does not run its body
# describeRoom() calls the function, causing its body to run
# Calling it twice runs the same reusable behaviour twice 

# def describe_room(description):
#     print(description)

# describe_room("Morning light leaks through the curtains.")
# describe_room("The kitchen smells faintly of cinnamon.")

# def describe_room(description):
#     return f"You look around. {description}"

# room_description=describe_room("Morning light leaks through the curtains.")
# print(room_description)

# kitchen_description=describe_room("The kitchen sings with the warmth of a freshly baked apple pie.")
# print(kitchen_description)

def describe_room(room):
    if room == "kitchen":
        return "The kitchen sings with the warmth of a freshly baked apple pie."
    elif room == "bedroom":
        return "Morning light leaks through the curtains."
    else:
        return f"Description missing for {room}!"

room_description = describe_room("kitchen")
print(room_description)

room_description = describe_room("bedroom")
print(room_description)

room_description = describe_room("bathroom")
print(room_description)