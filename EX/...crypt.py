while True:
    print("Choose Your Option:\n1)\tEncrypt\n2)\tDecrypt\n3)\tExit")
    choice = input("Your Choice: ")
    if choice == "1":
        plain_text = input("text: ")
        encrypted_text = ""
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print("encrypted text: ", encrypted_text)
        print("*"*40+"\n")

    elif choice == "2":
        encrypted_text = input("encrypted text: ")
        plain_text =  ""
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print("plaintext:", plain_text)
        print("*"*40+"\n")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Your Choice is wrong!")
        print("*"*40+"\n")