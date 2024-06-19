from art import text2art
name = input("enter your name: ")
count = int(input("enter number of repeat: "))
def ascii(text, font):
    art = text2art(text=f"{text}", font=f"{font}", chr_ignore=True)
    print(art)
for i in range(0,count):
    ascii(name, "random")
input("press any key and enter to exit:")