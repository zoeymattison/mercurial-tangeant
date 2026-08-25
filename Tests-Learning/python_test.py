# An entry point is simply the file we run to start the program. main.py is a common,
# clear name and not a requirement imposed by Python.
# Try to print something

#print("Your alarm cuts through the silence of the early morning, jolting you awake.")

# Print is a built-in function that displays information.
# Parentheses contain the information passed to the function (it takes an "argument")
# Quotation marks create a piece of text, called a string.
# Python executes this file from top to bottom.

# Input and variables
# The next goal is to ask the player's name, remember their answer, and greet them using that answer.
# Python asks for text with input()

# input("What is your name?")

# But to retain the answer, we need to store it in a variable. A
# variable is a name that refers to a value. You simply write the
# variable name and assign it, like so:

#player_name = input("What is your name? >> ")
#player_age = input("What is your age? >> ")
#player_pronoun1 = input("Enter your first pronoun (ie. \"She\") >> ")
#player_pronoun2 = input("Enter your second pronoun (ie. \"Her\") >> ")

# player_name is the variable
# = assigns the result
# input pauses the program and returns whatever the player types

# to insert a variable into displayed text, you can use an f-string:

#print(f"Good morning, {player_name}. It must feel nice to be {player_age}!")
#print(f"You'll be referred to as {player_pronoun1}/{player_pronoun2} from now on!")

# The f tells Python to replace expressions inside {}
# with their stored value.

# --- MAKING A DECISION --- #
# A narrative game needs to respond differently depending on a
# player's choice. Python uses "if" and "else" for this:

#weather = "rain"

#if weather == "rain":
#    print("You take an umbrella.")
#else:
#    print("You leave the umbrella behind.")

# = assigns a value
# == asks whether two values are equal
# The colon begins a block of related code
# Indentation tells Python which lines belong to that block
# else runs when the condition is false.

player_name = input("What is your name? >> ")

print(
    "Your alarm cuts through the silence of the early morning,",
    "jolting you awake"
)

choice = input("Get up, or stay in bed? >> ")

if choice == "Get up":
    print("You lazily slide out of bed, stretching on your way out.",
          "You hear a voice calling through the adjacent hall.",
          f"{player_name}, breakfast is ready!"
    )
else:
    print("You hit the snooze button, and roll over to face the wall.")

# Create a virtual environment
# In the root folder run python -m venv .venv
# Then run Activate.ps1 from the generated scripts folder

# Install Python-ce for GUI
# python -m pip install pygame-ce
# verify it with python -c "import pygame; print(pygame.version.ver)"

# python -m: asks Python to run an isntalled module
# venv: Python's virtual environment module.
# pip: installs specified python packages
# pygame-ce: the insatlled package
# -c: command, it tells Python to execute the quoted text directly (as opposed to reading it from a .py file)
# The semicolon separates statements written on the same line
# import pygame makes that package available inside Python code
