#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program: Simulating webpage history storage with two stacks.
# Author: Harmanpreet Singh Phull
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    """
    Gets a correct action from the user
    Inputs: N/A
    Returns: str
    """
    ValidAction = ["=", "<", ">", "q"]
    UserAction = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if (UserAction in ValidAction):
        return UserAction
    else:
        raise Exception("Invalid entry.")

def goToNewSite(current, bck, fwd):
    """
    Clears the fwd stack and pushes the current page to the bck stack
    Inputs: str, stack, stack
    Returns: str
    """
    bck.push(current)
    fwd.clear()
    return input("URL: ")

def goBack(current, bck, fwd):
    """
    Removes the top most page from the bck stack and pushes the current page to the fwd stack
    Inputs: str, stack, stack
    Returns: str
    """
    try:
        Previous = bck.peek()
    except Exception:
        print("No webpage in history.")
        return current
    else:
        fwd.push(current)
        bck.pop()
        return Previous

def goForward(current, bck, fwd):
    """
    Removes the top most page from the fwd stack and pushes the current page to the bck stack
    Inputs: str, stack, stack
    Returns: str
    """
    try:
        Forward = fwd.peek()
    except Exception:
        print("No webpage to go forward to.")
        return current
    else:
        bck.push(current)
        fwd.pop()
        return Forward

def main():
    """
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    """
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()

    current = HOME
    quit = False

    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
        except Exception as actionException:
            print(actionException.args[0])
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == "<":
                current = goBack(current, back, forward)
            elif action == ">":
                current = goForward(current, back, forward)
            elif action == "q":
                quit = True

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()