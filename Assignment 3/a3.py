"""
Author: Harmanpreet Singh Phull
Desc: A foray into Metaprogramming
"""

from importlib import invalidate_caches
from importlib import import_module


def load_function(name):
    """
    load_function - imports a module recently created by name
    and returns the function of the same name from inside of it
    name - a string name of the module (not including .py at the end)
    """
    # invalidate_caches is necessary to import any files created after this file started!
    invalidate_caches()
    print(f" Attempting to import {name}...")
    module = import_module(name)
    print(f" Imported!")
    assert hasattr(module, name), f"{name} is missing from {name}.py"
    function = getattr(module, name)
    assert callable(function), f"{name} in {name}.py isn't a function"
    assert type(function) is type(
        load_function
    ), f"{name} in {name}.py isn't a function"
    return function

def write_py(Name, ParamList, Statements):
    """
    Takes in arguments and makes a python file
    Input: String, List, List
    Return: N/A
    """
    assert Name != "a3", "Name can't be the same as this file."
    Def = f"def {Name}("  # used for the function def line
    Name = f"{Name}.py"
    for Param in ParamList:  # Loops through all the params
        Def += f"{Param}, "
    Def = Def.rstrip(", ")  # strips extra comma
    Def += "):"
    with open(Name, "w") as file:
        file.write(f"{Def}\n")
        for Line in Statements:
            file.write(f"\t{Line}\n")  # writes all the statements to the file

def fixed_bubble(size):
    """
    Makes a python file for bubblesort
    Input: Int
    Return: N/A
    """
    Name = f"bubble{size}"
    Argument = ["List"]
    Statements = []
    # Normal bubble sort loops
    for last in range(size - 1, 0, -1):
        for current in range(last):
            # instead of comparing and swapping, adds lines to the statements list
            Statements.append(f"if (List[{current}] > List[{current + 1}]):")
            Statements.append(f"\tList[{current}], List[{current + 1}] = List[{current + 1}], List[{current}]")
    Statements.append("return List")
    write_py(Name, Argument, Statements)

def flip(symbol):
    """
    Flips the comparison symbol
    Input: String
    Return: String
    """
    if (symbol == ">"):
        return "<"
    elif (symbol == "<"):
        return ">"

def greatest_power_of_two_less_than(integer):
    """
    Returns the greatest power of two that's less than the specified integer
    Input: Int
    Return: Int
    """
    assert integer >= 1, "Can't use integers less than 1"
    if (integer <= 2):
        return 1
    power = 0
    lesser = True
    while lesser:
        # if the current power becomes bigger than the integer stops the loop
        if (pow(2, power) >= integer):
            lesser = False
        else:
            power += 1
    return pow(2, power - 1)  # returns the previous power

def bitonic(List):
    """
    Helper function that calls the Bitonic Sort
    Input: List
    Return: N/A
    """
    BitonicSort(List, 0, len(List), ">")

def BitonicSort(List, Start, End, Dir):
    """
    Sorts the list
    Input: List, Int, Int, String
    Return: N/A
    """
    if End > 1:
        Middle = End // 2  # gets the middle index
        BitonicSort(List, Start, Middle, Dir)  # Sorts the first half
        BitonicSort(List, Start + Middle, End - Middle, flip(Dir))  # Sorts the second half
        BitonicMerge(List, Start, End, Dir)  # Merges the entire list

def BitonicMerge(List, Start, End, Dir):
    """
    Merges the list
    Input: List, Int, Int, String
    Return: N/A
    """
    if End > 1:
        Distance = greatest_power_of_two_less_than(End)
        Middle = End - Distance
        for i in range(Start, Start + Middle):  # loops until the middle
            if (Dir == "<" and List[i] < List[i + Distance]):
                List[i], List[i + Distance] = List[i + Distance], List[i]
            elif (Dir == ">" and List[i] > List[i + Distance]):
                List[i], List[i + Distance] = List[i + Distance], List[i]
        BitonicMerge(List, Start, Middle, Dir)
        BitonicMerge(List, Start + Middle, End - Middle, Dir)

def Bitonic_File(List, size):
    """
    Helper function that calls the Bitonic Sort File
    Input: List
    Return: N/A
    """
    BitonicSort_File(List, 0, size, ">")

def BitonicSort_File(Statements, Start, End, Dir):
    """
    Sorts the list
    Input: List, Int, Int, String
    Return: N/A
    """
    if End > 1:
        Middle = End // 2
        BitonicSort_File(Statements, Start, Middle, Dir)
        BitonicSort_File(Statements, Start + Middle, End - Middle, flip(Dir))
        BitonicMerge_File(Statements, Start, End, Dir)

def BitonicMerge_File(Statements, Start, End, Dir):
    """
    Appends the correct Statements
    Input: List, Int, Int, String
    Return: N/A
    """
    if End > 1:
        Distance = greatest_power_of_two_less_than(End)
        Middle = End - Distance
        for i in range(Start, Start + Middle):
            # the same as BitonicMerge but appends statements instead of comparing and swapping
            if (Dir == "<"):
                Statements.append(f"if (List[{i}] < List[{i + Distance}]):")
            elif (Dir == ">"):
                Statements.append(f"if (List[{i}] > List[{i + Distance}]):")
            Statements.append(f"\tList[{i}], List[{i + Distance}] = List[{i + Distance}], List[{i}]")
        BitonicMerge_File(Statements, Start, Middle, Dir)
        BitonicMerge_File(Statements, Start + Middle, End - Middle, Dir)

def fixed_bitonic(size):
    """
    Makes a python file for Bitonic Sort
    Input: Int
    Return: N/A
    """
    Name = f"bitonic{size}"
    Argument = ["List"]
    Statements = []
    Bitonic_File(Statements, size)
    Statements.append("return List")
    write_py(Name, Argument, Statements)

def main():
    write_py("div", ["a", "b"], ["r = a / b", "return r"])
    div = load_function("div")
    assert div(1, 2) == 0.5
    fixed_bubble(2)
    print(greatest_power_of_two_less_than(32))
    List = [6,1,2,4]
    print(List)
    bitonic(List)
    print(List)
    fixed_bitonic(3)

main()