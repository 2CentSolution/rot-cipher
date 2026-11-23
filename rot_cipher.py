import sys
def  rotate_text(message, rotation):
    encoded_message = ""
    for character in  message:
        if  65 <= ord(character) <= 90:
            base = 65
        elif 97 <= ord(character) <= 122:
            base = 97
        else:
            base = None
        if base is not None:
            result = (ord(character) - base + rotation) % 26 + base
            encoded_message += chr(result)
        else:
            encoded_message += character
    return encoded_message
if __name__ == "__main__":
   # message = sys.argv[1]
   # rotation = int(sys.argv[2])
    message =  input("Enter message: ")
    while True:
        try:
            rotation = int(input("Enter rotation (1-25): "))
        except ValueError:
            print("Error: Rotation must be a whole number.")
        else:
            if 1 <= rotation <= 25:
                break
            print("Error: Rotation must be between 1 and 25.")
        while True:
            answer = input("Try again? (Y/N) ").strip().lower()
            if answer == "y":
                 break
            elif answer == "n":
                raise SystemExit(0)
            else:
                print("Please enter Y or N. ")
    encoded = rotate_text(message, rotation)
    print("Result: ", encoded)
assert rotate_text("ABC", 13) == "NOP"
