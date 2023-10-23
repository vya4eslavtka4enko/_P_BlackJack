import random
from art import logo
import os
print(logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "Lose , opponent has blackJack"
    elif user_score == 0:
        return "Win with BlackJack"
    elif computer_score > 21:
        return "Opponent went over ,You win"
    elif user_score > 21:
        return "You went over, You lose"
    elif user_score > computer_score:
        return "Win"
    else:
        return "Lose"

def playGame():  
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f" Your cards: {user_card} current score: {user_score} ")
    print(f" Computer card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over=True
    else:
        user_should_deal = input('Type "y" to get another card, type "n" to pass: ')
        if user_should_deal == 'y':
            user_card.append(deal_card())
            # user_score = calculate_score(user_card)
            print(user_score)
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 18:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)




    print(compare(user_score,computer_score))
    
    
    
while input("Do you want play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    playGame()


