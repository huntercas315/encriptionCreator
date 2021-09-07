from random import randrange ###Used to randomize encription later

# Message Scrambler:

alphabetScramble = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

alphabet = {
    "a": "0",
    "b": "1",
    "c": "2",
    "d": "3",
    "e": "4",
    "f": "5",
    "g": "6",
    "h": "7",
    "i": "8",
    "j": "9",
    "k": "10",
    "l": "11",
    "m": "12",
    "n": "13",
    "o": "14",
    "p": "15",
    "q": "16",
    "r": "17",
    "s": "18",
    "t": "19",
    "u": "20",
    "v": "21",
    "w": "22",
    "x": "23",
    "y": "24",
    "z": "25",
    " ": "/"}

def scrambler(message: str) -> str:
    returnMessage = ""


    for character in message:
        if character.isdigit():
            returnMessage += f"({character})-"
        elif character.isupper():
            returnMessage += f"^{character}-"
        else:
            returnMessage += f"{alphabet.get(character)}-"

    if returnMessage.endswith("-"):
        returnMessage.rstrip("-")

    return returnMessage


# Get Message

message = str(input("Enter a message: "))

while (message.isalnum() == False):
    print("\nAlphanumeric Characters Only")
    message = str(input("Enter a message: "))

message = message.casefold()

print(scrambler(message))

print(message)###temp###