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
# This allows the piles to be visualised as *
print(SticksA)
SticksB = "Pile B:" + PileB * "*"
# This allows the piles to be visualised as *
print(SticksB)
SticksC = "Pile C:" + PileC * "*"
# This allows the piles to be visualised as *
print(SticksC)
# This converts the Piles into strings
print("(" + str(PileA) + ", " + str(PileB) + ", " + str(PileC) + ")")
player = "Player 2"

winn = False


# The main function is the entry point of any program. Runs the functions
def main():
    while not winn:
        get_input()
        selectValue()
        UpdatedPiles()
        win()


# This get input function checks if the value inputed into Choice is in the string of valid letters.
# If they are not contained it will then produce an error with the input that is not valid!
# This is done by a while true loops.
def get_input():
    global player
    valid_piles = ["A", "B", "C", "a", "b", "c"]
    global Choice, subtract
    print()
    print(switch())
    while True:
        Choice = input("choose your pile (A, B or C): ")
        if Choice in valid_piles:
            break
        else:
            print(Choice + " is not a valid pile!")


# The selectValue Function requires an input which will then be subtracted from the values of Pile A, B and C.
# If the letter inputted into choice then it will subtract the value inputted into subtract from the chosen pile!
# If the value is not a integer. Or the value is larger than the value in the pile. Or the value is to small
# It will through an error with the use of the while true statement!
def selectValue():
    global PileA, PileB, PileC
    while True:
        try:
            subtract = int(input(("How many sticks would you like to remove: ")))
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
            while True:
                try:
                    if subtract < PileA:
                        print("There are not enough Matchsticks in the PileA")
                    elif subtract < PileB:
                        print("There are not enough Matchsticks in the PileB")
                    elif subtract < PileC:
                        print("There are not enough Matchsticks in the PileB")
                except TypeError:
                    if subtract > PileA:
                        print("There is not enough sticks to remove in PileA!")
                    elif subtract > PileB:
                        print("There is not enough sticks to remove in PileB!")
                    elif subtract > PileC:
                        print("There is not enough sticks to remove in PileC")
        except ValueError:
            print("Error: There is either not a valid number of Matchsticks!")
            return


# Win() function governs if the player has won. The player can only win if the Piles A, B and C are equivilent to 0.
# Then the value of Winn is changed to True. Once this is done it will go back to the main function. and the While not
# function will stop the main function from looping again. It also prints the player that was the next turn!
def win():
    global PileA, PileB, PileC, winn
    if PileB + PileA + PileC == 0:
        winn = True
        print("===== GAME OVER =====")
        print(switch())
        print("WINS\n")

    return


# This function allows the program to swap player after a value has been subtracted. This then will return the value and
# Not excute the rest of the function if there was more below.
def switch():
    global player
    if player == "Player 1":
        player = "Player 2"
    else:
        player = "Player 1"
    return player


# The UpdatePiles function will print the new values of each of the piles as strings. It will display these piles after
# Win has been completed/True.
def UpdatedPiles():
    global SticksA, SticksB, SticksC
    print(("Pile A:" + PileA * "*"))
    print(("Pile B:" + PileB * "*"))
    print(("Pile C:" + PileC * "*"))
    print("(" + str(PileA) + ", " + str(PileB) + ", " + str(PileC) + ")\n")
    return

# This calls the main function again
main()
