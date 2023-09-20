def getInputFile():
    """Ask the users for a file name and returns it if it's a ".txt" file."""
    FileName = input("Write the name of the file: ")
    #Ask users to input the name of the file
    while FileName[len(FileName)-4:len(FileName)] != ".txt":
        print(f"The entered file \"{FileName}\" doesn't have the correct extension.\nPlease provide a file with the \".txt\" extension.\n")
        FileName = input("Write the name of the file: ")
    #Loops till the last four characters of the entered name are ".txt"
    return FileName

def decrypt(filename):
    """Takes in a filename as an argument, gets the encrypted text from it and then prints the decrypted text."""
    with open(filename, "r") as file:
        Shift = int(file.readline().strip())
        #Gets the shift value from the first line of the file and turns it into an int
        Text = file.readline().strip()
        #Gets the encrypted text from the second line of the file
    while Shift > 26:
        Shift -= 26
        #If the shift value is larger than 26, keeps subtracting until the value is lower than or equal to 26
    EncryptList = []
    LastSpace = False
    for i in Text:
        if (i == chr(32) or i == chr(9)):
            #Checks for white space
            if(not LastSpace):
                EncryptList.append(" ")
                #Appends a space if LastSpace is false
            LastSpace = True
        else:
            EncryptList.append(ord(i.lower()))
            #Converts characters into unicode
            LastSpace = False
    DecryptList = []
    for i in EncryptList:
        if (i == " "):
            DecryptList.append(i)
        else:
            i -= Shift
            if (i < 97):
                i += 26
                #If the decrypted unicode goes belows 97 adds 26 to it so that it loops around
            if (i > 122):
                i -= 26
                #If the decrypted unicode goes above 122 subtracts 26 from it so that it loops around
            DecryptList.append(chr(i))
    print("".join(DecryptList))

def main():
    help(getInputFile)
    help(decrypt)
    decrypt(getInputFile())

main()