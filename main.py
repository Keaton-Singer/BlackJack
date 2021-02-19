from random import randint


# The variable "end" holds the last current index of the "cards" array. As the
# player or dealer picks a card, "end" is simultaneously decremented so the randint
# function does not go out of bounds while choosing a random card. The "cards" array
# holds all the different selections of playing cards. Each tuple contains the cards
# suit and value (The value of Aces are malleable). The "reset" variable is used to
# store the original "cards" array so the program can reset the cards after a round.
end = 51
cards = [('dA', 11), ('d2', 2), ('d3', 3), ('d4', 4), ('d5', 5), ('d6', 6), ('d7', 7), ('d8', 8), ('d9', 9), ('d10', 10), ('dJ', 10), ('dQ', 10), ('dK', 10),
         ('hA', 11), ('h2', 2), ('h3', 3), ('h4', 4), ('h5', 5), ('h6', 6), ('h7', 7), ('h8', 8), ('h9', 9), ('h10', 10), ('hJ', 10), ('hQ', 10), ('hK', 10),
         ('sA', 11), ('s2', 2), ('s3', 3), ('s4', 4), ('s5', 5), ('s6', 6), ('s7', 7), ('s8', 8), ('s9', 9), ('s10', 10), ('sJ', 10), ('sQ', 10), ('sK', 10),
         ('cA', 11), ('c2', 2), ('c3', 3), ('c4', 4), ('c5', 5), ('c6', 6), ('c7', 7), ('c8', 8), ('c9', 9), ('c10', 10), ('cJ', 10), ('cQ', 10), ('cK', 10)]
reset = cards[:]


# The "print_cards" function takes in a current hand, either from the player or dealer,
# and displays the cards onto the console using ASCII characters. This function is 
# relatively large and repetitive because the cards are displayed sideways, which means
# we must first print all of the cards together row by row. (This program was originally
# created using the PyCharm IDE with a white console. Use this environment for best user
# experience)
def print_cards(hand):
    length = len(hand)
    print('\033[30m+---------------------+  ' * length)
    for one in range(length):
        if hand[one][0][0] == 'h' or hand[one][0][0] == 'd':
            if hand[one][0][1:] == '10': print('\033[30m| {}                  \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
            else: print('\033[30m| {}                   \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
        else:
            if hand[one][0][1:] == '10': print('\033[30m| {}                  \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end = '  ')
            else: print('\033[30m| {}                   \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|                     |', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|          \033[31m*          \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|          \033[30m*          \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|        \033[30m*****        \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|    \033[31m****     ****    \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|         \033[31m***         \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|         ***         \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|       *******       \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|  \033[31m*******   *******  \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|        \033[31m*****        \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|       *******       \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|        *****        \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|  \033[31m******** ********  \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|       \033[31m*******       \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|     ***********     \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|   *****  *  *****   \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|   \033[31m***************   \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|      \033[31m*********      \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|    *************    \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|  *****************  \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|     \033[31m***********     \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|       \033[31m*******       \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|     ***** *****     \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|   *****  *  *****   \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|       \033[31m*******       \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|        \033[31m*****        \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|          *          |', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|          *          |', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|         \033[31m***         \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|         \033[31m***         \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|         ***         \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|         ***         \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h': print('\033[30m|          \033[31m*          \033[30m|', end = '  ')
        if hand[one][0][0] == 'd': print('\033[30m|          \033[31m*          \033[30m|', end = '  ')
        if hand[one][0][0] == 's': print('\033[30m|        *****        \033[30m|', end = '  ')
        if hand[one][0][0] == 'c': print('\033[30m|        *****        \033[30m|', end = '  ')
    print()
    for one in range(length):
        if hand[one][0][0] == 'h' or hand[one][0][0] == 'd':
            if hand[one][0][1:] == '10': print('\033[30m|                  {} \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
            else: print('\033[30m|                   {} \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
        else:
            if hand[one][0][1:] == '10': print('\033[30m|                  {} \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end = '  ')
            else: print('\033[30m|                   {} \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end= '  ')
    print()
    print('\033[30m+---------------------+  ' * length)


# The "pick_card" function is used to choose a card from the "cards" array and append it to
# the hand provided. Once the function appends a random card to the hand, it removes the card
# from the deck/array.
def pick_card(hand):
    random = randint(0,end)
    hand.append(cards[random])
    cards.remove(cards[random])


# The "hand_amount" function takes in a hand of cards as input, and counts the current value of
# all of the cards in the hand. If there is an Ace within the hand, and the hands value is above
# 21 (A losing hand), the function will automatically change the value of the Ace to make the deck
# less than 21, otherwise Aces will always hold a value of 11.
def hand_amount(hand):
    val = 0
    for card, value in hand:
         val += value
    if val > 21:
        for ind, (card, value) in enumerate(hand):
            if card[1] == 'A' and value != 1 and val > 21:
                    hand.remove(hand[ind])
                    hand.insert(ind, (card, 1))
                    val -= 10
    return val

# The first portion of the "main" code is used to initialize each round. The user will always start
# with 500 chips in their account. While the user still has chips, the while loop will continue to
# operate. Within the while loop, the code prompts the user for a bet, which is error checked by a 
# nested while loop. If the users bet is not an integer, or if it is below 1 or above the chip amount,
# it will continue to prompt the user for a valid bet. Once the user enters a valid bet, the code
# intializes a hand for both the player and dealer (The two arrays), and it will add cards to their hands.
# Lastly, the code checks the total of the user's hand and displays the cards to the console.
file = open('BlackJackRecord.txt', 'r+')
round = 1
chips = 500
while chips > 0:
    print('\n\033[01m\33[30m' + 'Hand {} -'.format(round), end = ('-'*150))
    bet = input('\n\nHow many chips would you like to bet? ({} chips remaining) '.format(chips))
    while not bet.isdigit() or int(bet) not in range(1,chips+1):
        print('\nInvalid bet!')
        bet = input('\nHow many chips would you like to bet? ({} chips remaining) '.format(chips))
    player, dealer = [], []
    for num in range(2):
        pick_card(player)
        end -= 1
        pick_card(dealer)
        end -= 1
    total = hand_amount(player)
    print('\nDealer\'s Card: ')
    print_cards(dealer[:1])
    print('Your Cards: ')
    print_cards(player)

    # This section of code is what allows the user to "play" Blacjack. The while loop continues
    # to operate as the user requests to hit, and while their hand is less than 21. The nested
    # while loop is used as an error-check to ensure that the user has entered in valid input.
    # It will keep requested either "hit" or "stay" until the user enters one of the two (Not case
    # sensitive). Each time the player "hits", the code will pick a card and display the cards to the
    # user.
    decision = 'hit'
    while decision == 'hit' and total < 21:
        decision = (input('\nWould you like to stay or hit? '))
        while decision.lower() != 'hit' and decision.lower() != 'stay':
            print('\nInvalid decision!')
            decision = (input('\nWould you like to stay or hit? '))
        if decision == 'hit':
            pick_card(player)
            end -= 1
            print('\nDealer\'s Card: ')
            print_cards(dealer[:1])
            print('Your Cards: ')
            print_cards(player)
        total = hand_amount(player)

    # The code below is used to determine if the user has lost, tied, or won against the dealer.
    # If the user's hand value is above 21, the code automatically prints the cards from the round
    # and subtracts the user's bet from his current chip amount. If the user's hand value is below 21
    # or equal to 21, the code enters an else block that has a while loop that is used to pick cards for
    # the dealer until his hand value is 17 or over. Once the dealer is finished picking his cards, the
    # code determines who won between the two of them. If the dealer has a lower hand value or goes over 21, the
    # user wins and his chip count is incremented accordingly, otherwise the code checks to see if they tied,
    # or finally, if the user has lost (In which case his chips will be decremented by his bet).
    print('\n----> Round Results:')
    if total > 21:
        print('\nDealer\'s Card: ')
        print_cards(dealer[:1])
        print('Your Cards: ')
        print_cards(player)
        print('\n\33[31mYou bust!')
        chips -= int(bet)
    else:
        while hand_amount(dealer) < 17:
            pick_card(dealer)
            end -= 1
        print('\nDealer\'s Cards: ')
        print_cards(dealer)
        print('Your Cards: ')
        print_cards(player)
        if hand_amount(dealer) < hand_amount(player) or hand_amount(dealer) > 21:
            print('\n\33[32mYou Win!')
            chips += int(bet)
        elif hand_amount(dealer) == hand_amount(player):
            print('\nPush!')
        else:
            print('\n\33[31mDealer Wins!')
            chips -= int(bet)
    

    # Once each round of Blackjack is over, this portion of code resets the deck of cards and
    # the ending index of the "cards" array. The round is then incremented by one and we use
    # an if statement to see if the current chip record in the record file should be updated.
    cards = reset[:]
    end = 51
    round += 1
    file.seek(13)
    record = file.read()
    if chips > int(record):
        file.seek(13)
        file.write(str(chips))


# At the end of the program, we seek to the 13th character within the record file, and display the
# current chip record to the user once the game is finished. Lastly, we close the file.
print('\n\33[30m' + '-'*150)
file.seek(13)
record = file.read()
print('\n\033[31mOut of money!\n\n\033[30mRecord: {} \033[30mchips\n'.format('\033[33m' + str(record)))
file.close()
