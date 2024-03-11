import random
from replit import clear
from art import logo
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

# a function to make the whole game start again without constantly stopping and rerunning
def play_again():
    again = input("Do you want to play again? Type 'y' or 'n'")
    if again == "y":
        clear()
        user_cards.clear()
        computer_cards.clear()
        blackjack()
    else:
        print("Goodbye! Thank you for playing!")

# a function to pick a random card
def deal_card():
    number = random.randrange(0,11)
    return cards[number]

# function for the start of the game
def start_game():
    for i in range(2):
        user_cards.append(deal_card())
    return user_cards

def dealers_move():
    while sum(computer_cards) < 21:
        if sum(computer_cards) < 17:
            computer_cards.append(deal_card())
        else:
            return computer_cards

# the whole game
def blackjack():
    end = False
    start_game()
    dealers_move()
    if sum(user_cards) > 21:
        for cards in range(len(user_cards)):
            if user_cards[cards] == 11:
                user_cards[cards] = 1
    if sum(user_cards) == 21: 
        print(f"Looks like you got a {user_cards} - a blackjack, you win!")
        print(f"The computer's cards are: {computer_cards}, total: {sum(computer_cards)}")
        end = True
        play_again()
    while not end:
        clear()
        print(f"Your cards are: {user_cards}, total:{sum(user_cards)}")
        if sum(user_cards) > 21:
            for cards in range(len(user_cards)):
                if user_cards[cards] == 11:
                    user_cards[cards] = 1
            print("Looks like you blew it, you lose.")
            end = True
            play_again()
        else:
            print(f"The computer's first card is: {computer_cards[0]}")
            draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw_card == "y":
                user_cards.append(deal_card())
                end = False
            elif draw_card == "n":
                end = True
                clear()
                print(f"Your cards are: {user_cards},and the total: {sum(user_cards)}")
                print(f"The computer's cards are: {computer_cards}, total: {sum(computer_cards)}")
                if computer_cards[0] + computer_cards[1] == 21:
                    print("Looks like you lost to a blackjack, you lose.")
                    play_again()
                if sum(user_cards) > sum(computer_cards):
                    print("Congratulations! You win!")
                    play_again()
                elif sum(computer_cards) > 21:
                    print("looks like computer blew it, You win!")
                    play_again()
                elif sum(user_cards) == sum(computer_cards):
                    print("It's a draw!")
                    play_again()
                else:
                    print("Unfortunately, you lose. Game Over")
                    play_again()
                    
            else:
                print("Invalid input. Please try again.")

print(logo)
input(f"Welcome to the Blackjack game! Press enter to start.")
blackjack()