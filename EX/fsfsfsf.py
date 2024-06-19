import os
from random import randint

pas = input("send the password: ")

keys = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8"
        , "9" , "0" , "a" , "b" , "c" , "d" , "e" , "f" ,
        "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" ,
        "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v"
        , "w" , "x" , "y" , "z", "A" , "B" , "C" , "D" , "E" , "F" ,
        "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" ,
        "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V"
        , "W" , "X" , "Y" , "Z"]

pwg = ""
while(pwg!=pas):
    pwg=""
    for i in range(len(pas)):
        guesspass = keys[randint(0,4)]
        pwg = str(guesspass)+str(pwg)
        print(pwg)
        print("attacking... please wait!")
        os.system("cls")

print(f"the passs is : {pwg}")
input("press any key and enter to exit: ")