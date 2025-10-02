def Lab2A():
    name = input("Enter a name: ")
    another_name = input("Enter another name: ")
    verb = input("Enter a verb: ")
    advervb = input("Enter and adverb: ")
    print(
        f"Once upon a time, there was a person named {name} who had a child named {another_name}. This child would {verb} {advervb} while singing to stangers.")


def Lab2B():
    print(
        """    ___*___
            __*_*__
            _*_*_*_
            *_*_*_*
            _*_*_*_
            __*_*__
            ___*___""")


def Lab2C():
    w = int(input("Enter a width: "))
    h = int(input("Enter a height: "))
    a = h * w
    p = 2 * (h + w)
    print(f"The area is {a}\nThe perimeter is {p}")


print(
    """
    Enter the respective number for each lab, then enter the respective leter.
    
        Lab 2 - Enter 2
            A) Story Maker
            B) Prints text art
            C) Area & Perimeter Calculator
    
        Lab 3 - Enter 3   
            A) Credit Cards
            B) GPA Calculator
            C) Sandwiches
        """)


def choose(number):
    # choice = input("Which Lab do you want to run? ")
    match number:
        case ("2A"):
            Lab2A()
        case "2B":
            Lab2B()
        case "2C":
            Lab2C()
        case _:
            choice = input("Which Lab do you want to run? ")


# Lab3A()
choose(input("Which one do you want to run? \n"))
