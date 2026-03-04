#small personal project to make a password generator because i was tired of having to find one online (most of them are ad riddled)
import random as rdm

password = ""
characters = [
    list("abcdefghijklmnopqrstuvwxyz"),
    list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    list("1234567890"),
    list("!@#$%^&*()[]{}-_+=~")
]

# Get password length
while True:
    length = input("How many characters long?: ")
    if length.isnumeric():
        length = int(length)
        break
    else:
        print("You cannot enter anything other than a whole number!")

# Special character option
special = input("Are special characters allowed (y/n)?: ").lower()
if special in ["y", "yes"]:
    print("Ok, special characters added.")
    addSpecial = 1
else:
    print("Ok, no special characters added.")
    addSpecial = 0

# Generate password
for i in range(length):
    charType = rdm.randint(0, 2 + addSpecial)  # include specials if allowed
    amountOfChar = len(characters[charType])
    charPosition = rdm.randint(0, amountOfChar - 1)
    password += characters[charType][charPosition]

print("Your password is:", password)
