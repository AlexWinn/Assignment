import random
# The .random module is imported to create a random integer between values in the list.
PileA = random.randint(5, 15)
# PileA will be equilivent to a random value between 5 and 15.
PileB = random.randint(5, 15)
# PileB will be equilivent to a random value between 5 and 15.
PileC = random.randint(5, 15)
# PileB will be equilivent to a random value between 5 and 15.

print("===== Welcome to Nim Game =====")
# These print statements print the title of the game!
print("Below are 3 magic piles!")

SticksA = "Pile A:" + PileA * "*"
# This allows the piles to be visualised as "*"
print(SticksA)
SticksB = "Pile B:" + PileB * "*"
# This allows the piles to be visualised as "*"
print(SticksB)
SticksC = "Pile C:" + PileC * "*"
# This allows the piles to be visualised as "*"
print(SticksC)
# This converts the Piles into strings
print("(" + str(PileA) + ", " + str(PileB) + ", " + str(PileC) + ")")

player = "Player 2"


# The main function is the entry point of any program. Runs the functions
def main():
    subtract = int(input(("How many sticks would you like to remove: ")))
    while True:
        get_input()
        selectValue()
        error()
        UpdatedPiles()


def get_input():
    global player
    valid_piles = ["A", "B", "C", "a", "b", "c"]
    print()
    print(switch())
    while True:
        Choice = input("choose your pile (A, B or C): ")
        if Choice in valid_piles:
            break
        else:
            print(Choice + " is not a valid pile!")


def selectValue():
    global PileA, PileB, PileC, subtract
    valid_numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while True:
        try:
            if subtract in valid_numbers:
                break
            else:
                print(subtract + "is not a valid number!")

            if Choice == "A" or Choice == "a" and subtract < PileA:
                PileA = PileA - subtract
                print("Ok!")
                print()
                break
            elif Choice == "B" or Choice == "b" and subtract < PileB:
                PileB = PileB - subtract
                print("Ok!")
                print()
                break
            elif Choice == "C" or Choice == "c" and subtract < PileC:
                PileC -= subtract
                print("Ok!\n")
                break
        except ValueError:
            print("Error: Value entered is not a valid number of Matchsticks!")


def error():
    global subtract
    if subtract > PileA:
        print("There are not enough Matchsticks in the PileA")
    else:
        print("Ok")
    if subtract > PileB:
        print("There are not enough Matchsticks in the PileA")
    else:
        print("Ok")
    if subtract > PileC:
        print("There are not enough Matchsticks in the PileA")
    else:
        print("Ok")


def switch():
    global player
    if player == "Player 1":
        player = "Player 2"
    else:
        player = "Player 1"
    return player


def UpdatedPiles():
    global SticksA, SticksB, SticksC
    print(("Pile A:" + PileA * "*"))
    print(("Pile B:" + PileB * "*"))
    print(("Pile C:" + PileC * "*"))
    print("(" + str(PileA) + ", " + str(PileB) + ", " + str(PileC) + ")")
    if SticksB + SticksA + SticksC == 0:
        print("GAME OVER", )
        print(switch())
        print("WINS")
        main()


main()
