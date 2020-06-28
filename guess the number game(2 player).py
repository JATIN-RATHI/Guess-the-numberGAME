if __name__ == '__main__':
    import random
    print("\nWelcome to the program\tcreated by \x1b[6;30;42m'Jatin Rathi'\x1b[0m")
    print("\nDISCRIPTION: This is a game in which one player have to enter two number.\n\tAfter which both player have to guess the number between those two number entered.")
    player1 = input("\nEnter Player 1's name : ").capitalize()
    gender1 = input("Enter player 1's Gender : ").capitalize()
    player2 = input("\nEnter Player 2's name : ").capitalize()
    gender2 = input("Enter player 2's Gender : ").capitalize()
    if gender1 == "Male" :
        m = "he"
    elif gender1 == "Female" :
        m = "she"
    else:
        m = "he/she"

    if gender2 == "Male" :
        m1 = "he"
    elif gender2 == "Female" :
        m1 = "she"
    else:
        m1 = "he/she"
    num1 = int(input("\nEnter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    #empty list initialised to store the number b/w num1 and num2
    list = []
    #loop to iterate the number in b/w num1 and num2 and storing all that numbers in list
    i = num1
    for i in range(num1, num2+1):
        list.append(i)
    #using random module to save any random item from the list and store it in other variable
    guess = random.choice(list)
    print(f"The numbers in b/w {num1} & {num2} are {list}")
    print("---------------------------------------------------------------------")
    print(f"{player1} will play first untill {m} guess the number correctly.")
    print("---------------------------------------------------------------------")
    # it is a variable which work as a counter for player 1
    j = 1
    #while loop will iterate till user's input == guess
    while True:
        choice1 = int(input(f"\n{player1} ,Choose any one number from the list  {list} : "))
        if choice1 == guess:
            print(f"Congratulation! {player1} Your {j} Guess is correct i.e. {guess}")
            break
        elif choice1 > guess:
            print(f"Your number {choice1} is higher than the Guess number. Try again!")
            j += 1
            continue
        elif guess > choice1:
            print(f"Your number {choice1} is smaller than the Guess number. Try again!")
            j += 1
            continue
        else:
            j += 1
            continue
    guess = random.choice(list)
    print("---------------------------------------------------------------------")
    print(f"Now, {player2} will play untill {m1} guess the number correctly.")
    print("---------------------------------------------------------------------")
    # it is a variable which work as a counter for player 2
    k = 1
    while True:
        choice2 = int(input(f"\n{player2} ,Choose any one number from the list  {list} : "))
        if choice2 == guess:
            print(f"Congratulation! {player2} Your {k} Guess is correct i.e. {guess}")
            break
        elif choice2 > guess:
            print(f"Your number {choice2} is higher than the Guess number. Try again!")
            k += 1
            continue
        elif guess > choice2:
            print(f"Your number {choice2} is smaller than the Guess number. Try again!")
            k += 1
            continue
        else:
            k += 1
            continue
    if k>j :
        print(f"\n\t{player1} had {j-k} guess lesser than {player2}.\n\t\t*****WINNER is {player1}*****.")
    elif j>k :
        print(f"\n\t{player2} had {k-j} guess lesser than {player1}.\n\t\t*****WINNER is {player2}*****.")
    elif j == k:
        print(f"\n\t{player1} and {player2} play again!! This Game is Draw.")
    else :
        print("YOU BOTH DON'T KNOW HOW TO PLAY , LOOSERS !!")


