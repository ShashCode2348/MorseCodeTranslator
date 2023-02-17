import re

morseCodes = {"A":".- ", "B":"-... ", "C":"-.-. ", "D":"-.. ", "E":". ", "F":"..-. ", "G":"--. ", "H":".... ", "I":".. ", "J":".--- ", "K":"-.- ", "L":".-.. ", "M":"-- ",
              "N":"-. ", "O":"--- ", "P":".--. ", "Q":"--.- ", "R":".-. ", "S":"... ", "T":"- ", "U":"..- ", "V":"...- ", "W":".-- ", "X":".--. ", "Y":"-.-- ", "Z":"--.. ",
              "0":"----- ", "1":".---- ", "2":"..--- ", "3":"...-- ", "4":"....- ", "5":"..... ", "6":"-.... ", "7":"--... ", "8":"---.. ", "9":"----. ",
              "&":".-... ", "'":".----. ", "@":".--.-. ", ")":"-.--.- ", "(":"-.--. ", ":":"---... ", ",":"--..-- ", "=":"-...- ",
              "!":"-.-.-- ", "+":".-.-. ", "\"":".-..-. ", "?":"..--.. ", "/":"-..-. ", ".":".-.-.- ", "-":"-....- ", " ":"/ "}
reverseMorse = {m:c for c,m in morseCodes.items()}

def encrypt(message):
    morseStr = ""
    for char in message:
        morseChar = morseCodes.get(char.upper())
        if morseChar != None:
            morseStr += morseChar
        else:
            raise SystemExit("Error encrypting. Please use characters from the given set only.")
    return morseStr.rstrip()

def decrypt(morseStr):
    message = ""
    morseChars = re.split('([^\s]*\s)', morseStr + " ")[1::2]
    print(morseChars)
    for morseChar in morseChars:
        char = reverseMorse.get(morseChar)
        if char != None:
            message += char
        else:
            raise SystemExit("Error decrypting. Please make sure you have copied all of the characters.")
    return message

option = (input("Do you want to encode or decode(e/d)? ").lower() == "e")
if option == True:
    print("The encoded message is " + encrypt(input("Enter the message. Use letters, digits, spaces and characters &'@():,=!+\?/.- only: ")))
else:
    print("The decoded message is " + decrypt(input("Enter the encoded message. Do not add a whitespace at the end: ")))
    
