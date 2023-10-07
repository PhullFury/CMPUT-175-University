#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: A very basic simulation of browser history storage#
# Author: Harmanpreet Singh Phull
#----------------------------------------------------

def getAction():
    """
    Gets a correct action from the user
    Inputs: N/A
    Returns: str
    """
    ValidAction = ["=", "<", ">", "q"]
    UserAction = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    # loops until the user enters a valid action
    while UserAction not in ValidAction:
        print("Invalid Entry. Please try again.\n")
        UserAction = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    return UserAction


def goToNewSite(current, pages):
    """
    Adds a new URL to the list
    Inputs: int, list
    Returns: int
    """
    URL = input("URL: ")
    NewIndex = current + 1
    # removes all the webpages that are after the NewIndex
    for i in range(NewIndex, len(pages)):
        pages.pop(NewIndex)
    # adds the new webpage to the list
    pages.append(URL)
    return NewIndex

    
def goBack(current, pages):
    """
    Goes back one index if one exists
    Inputs: int, list
    Returns: int
    """
    if (current == 0):
        print("Cannot go back.")
        return current
    else:
        return current - 1


def goForward(current, pages):
    """
    Goes forward one index if one exists
    Inputs: int, list
    Returns: int
    """
    if (current == len(pages) - 1):
        print("Cannot go forward.")
        return current
    else:
        return current + 1


def main():
    """
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    """
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False

    # loops until the user decides to quit
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()