import random
playerIn = True
dealerIn = True
# deck of cards / player's hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A',]
dealerhand = []
playerhand = []
# deal the cards
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand

def determine_total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(2,11):
            total += card
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total

# check for winner

def revealdealerhand():
    if len(dealerhand) == 2:
        return dealerhand
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]
    
# game loop

for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)

while playerIn or dealerIn:
    print(f"Dealer hand {revealdealerhand()} and X")
    print(f"You have {playerhand} for a total of {determine_total(playerhand)}")
    if playerIn:
        stayOrhit = input("1:Stay\n2:Hit\n")
        if stayOrhit == '1':
            playerIn = False
        else:
            dealcard(playerhand)
    if determine_total(dealerhand) > 16:
        dealerIn = False
    else:
        dealcard(dealerhand)
    if determine_total(playerhand) >= 21:
        break
    elif determine_total(dealerhand) >= 21:
        break

if determine_total(playerhand) == 21:
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("Blackjack! YOU WIN !!!")
elif  determine_total(dealerhand) == 21:
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("Blackjack! DEALER WINS !!!")
elif  determine_total(playerhand) > 21:
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("You lost! Dealer wins!")
elif  determine_total(dealerhand) > 21:
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("Dealer lost! You win!")
elif 21 - determine_total(dealerhand) < 21 - determine_total(playerhand):
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("Dealer wins!")
elif 21 - determine_total(dealerhand) > 21 - determine_total(playerhand):
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {determine_total(dealerhand)}")
    print("You win!")