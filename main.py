import random
from replit import clear
from art import logo

def deal_card():
    """ This function returns random card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(card_list):
    """ This function calculates the score of cards"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(user_score_input, computer_score_input):
    if user_score_input == computer_score_input:
        return "It's a Draw 😔"    
    elif user_score_input == 0:
        return "You won, You have a blackjack ♣︎"
    elif computer_score_input == 0:
        return "Computer Won, Computer have a blackjack 🥲"
    elif computer_score_input > 21:
        return "You Won 💪"
    elif user_score_input > 21:
        return "Computer Won 🥲"
    elif user_score_input > computer_score_input:
        return "You won!"
    else:
        return "You Lose!"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for count in range(1,3):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, Current Score: {user_score}")
        print(f" Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            darw_another_card = input("Do you want to draw another card? 'y' or 'n' to reply:")
            if darw_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #computer drawing new cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(compare(user_score, computer_score))

while input("Do you want to Play a game of Blackjack? Type 'y' and 'n': ") == "y":
    clear()
    play_game()