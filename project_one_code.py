import random
import os

ANSWERS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# clear screen function that was remembered from the exercises w/ Kenneth
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# check to see if the user input is an acceptable number
def check_guess(guess):
    try:
        guess = float(guess)
        # check to see if the number guess is within the ANSWERS tuple
        if guess in ANSWERS:
            return int(guess)
        else:
            return False
    except ValueError:
        return "ValueError"


# check if the play again response is ok
def play_again_check():
    play_again = input("Would you like to play again? (y/n)\n")
    while True:
        if play_again.lower() == "y":
            return play_again
        elif play_again.lower() == "n":
            return play_again
        else:
            clear_screen()
            print("Sorry, your answer, '{}' is neither y nor n!".format(play_again))
            print("Please enter a valid answer!")
            play_again = input("Would you like to play again? (y/n)\n")
            clear_screen()


# function that actually plays the game
def start_game(high_score):
    # define the answer
    correct_answer = random.choice(ANSWERS)

    number_of_guesses = 1
    guess_message = ""
    while True:
        # header of game w/ higher or lower message as well
        if guess_message == "":
            my_guess = input("*** Please guess a round number from 1 to 10 ***\nGuess attempt number {}!\n".format(number_of_guesses))
        else:
            my_guess = input("*** Please guess a round number from 1 to 10 ***\nGuess attempt number {}!\n{}\n".format(number_of_guesses,guess_message))

        clear_screen()
        valid_guess = check_guess(my_guess)

        if valid_guess == "ValueError":
            print("*** Sorry, your guess '{}' is not a valid numerical guess! ***".format(my_guess))
            input("\nPlease press return to continue")
            clear_screen()
            continue
        if valid_guess == False:
            print("*** Sorry, your guess {} is not a whole number in the range 1 to 10 ***".format(my_guess))
            input("\nPlease press return to continue")
            clear_screen()
            continue

        # my guess becomes the valid_guess
        my_guess = valid_guess

        if my_guess == correct_answer:
            print("Congratulations! Your guess of {} was the correct answer!".format(my_guess))
            print("You got the right answer in {} tries!".format(number_of_guesses))
            return number_of_guesses
        elif my_guess > correct_answer:
            guess_message = "The correct answer is lower than your previous guess of {}.".format(my_guess)
            # add number of guesses
            number_of_guesses+=1
            continue
        else:
            guess_message = "The correct answer is higher than your previous guess of {}.".format(my_guess)
            # add number of guesses
            number_of_guesses+=1
            continue


# play the game
if __name__ == "__main__":

    high_score = None
    games = 0
    while True:

        print("\nWelcome to the number guessing game!\n")
        if high_score != None:
            print("The current high score to beat is {}! Good luck!".format(high_score))
        else:
            print("There is no high score yet! Good luck!")

        play_game = input("\n*** PLEASE PRESS RETURN TO BEGIN, OR WRITE 'QUIT' TO EXIT THE GAME ***")
        clear_screen()

        if play_game.lower() == "quit":
            clear_screen()
            if games > 0:
                print("You've exited the game!")
                print("You played {} games, with a high score of {}!".format(games, high_score))
            else:
                print("You exited the game, without playing any games!")
                print("Come back and play! Cya later!")
            break

        games += 1
        my_score = start_game(high_score)

        if high_score == None:
            high_score = my_score
        elif high_score > my_score:
            high_score = my_score

        print("")
        play_again = play_again_check().lower()
        if play_again == "y":
            clear_screen()
            continue
        else:
            clear_screen()
            print("You've left the game!")
            print("In {} games the highscore was {}!".format(games, high_score))
            print("Thanks for playing!")
            break
