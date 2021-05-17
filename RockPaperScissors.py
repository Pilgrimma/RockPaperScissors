def checkInput(inp):
    if inp == "r" or "s" or "p":
        return True
    else:
        print("That is not a correct input!")
        return False

play = True
while play == True:
    inputCheck = False
    p1 = ""
    p2 = ""
    print("Player 1: rock (r)/scissors (s)/paper (p)")
    while inputCheck == False:
        p1 = input()
        inputCheck = checkInput(p1)
    inputCheck = False
    print("Player 2: rock (r)/scissors (s)/paper (p)")
    while inputCheck == False:
        p2 = input()
        inputCheck = checkInput(p1)
    if p1 == p2:
        print("It's a draw!")
    elif p1 == "r" and p2 == "s":
        print("Player 1 wins!")
    elif p1 == "r" and p2 == "p":
        print("Player 2 wins!")
    elif p1 == "s" and p2 == "r":
        print("Player 2 wins!")
    elif p1 == "s" and p2 == "p":
        print("Player 1 wins!")
    elif p1 == "p" and p2 == "r":
        print("Player 1 wins!")
    elif p1 == "p" and p2 == "s":
        print("Player 2 wins!")
    answer = ""
    while (answer != "y") or (answer != "n"):
        print("Would you like to start a new game? (y/n)")
        answer = input()
        if answer == "n":
            exit()
        if answer == "y":
            break