from random import randint


end = 51
cards = [('dA', 11), ('d2', 2), ('d3', 3), ('d4', 4), ('d5', 5), ('d6', 6), ('d7', 7), ('d8', 8), ('d9', 9), ('d10', 10), ('dJ', 10), ('dQ', 10), ('dK', 10),
         ('hA', 11), ('h2', 2), ('h3', 3), ('h4', 4), ('h5', 5), ('h6', 6), ('h7', 7), ('h8', 8), ('h9', 9), ('h10', 10), ('hJ', 10), ('hQ', 10), ('hK', 10),
         ('sA', 11), ('s2', 2), ('s3', 3), ('s4', 4), ('s5', 5), ('s6', 6), ('s7', 7), ('s8', 8), ('s9', 9), ('s10', 10), ('sJ', 10), ('sQ', 10), ('sK', 10),
         ('cA', 11), ('c2', 2), ('c3', 3), ('c4', 4), ('c5', 5), ('c6', 6), ('c7', 7), ('c8', 8), ('c9', 9), ('c10', 10), ('cJ', 10), ('cQ', 10), ('cK', 10)]
reset = cards[:]


def print_cards(hand):
    length = len(hand)
    print('\033[30m+---------------------+  ' * length)
    for one in range(length):
        if hand[one][0][0] == 'h' or hand[one][0][0] == 'd':
            if hand[one][0][1:] == '10':
                print('\033[30m| {}                  \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
            else:
                print('\033[30m| {}                   \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end='  ')
        if hand[one][0][0] == 's' or hand[one][0][0] == 'c':
            if hand[one][0][1:] == '10':
                print('\033[30m| {}                  \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end = '  ')
            else:
                print('\033[30m| {}                   \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end='  ')
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
            if hand[one][0][1:] == '10':
                print('\033[30m|                  {} \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end = '  ')
            else:
                print('\033[30m|                   {} \033[30m|'.format('\033[01m\033[31m' + (hand[one][0][1:])), end='  ')
        if hand[one][0][0] == 's' or hand[one][0][0] == 'c':
            if hand[one][0][1:] == '10':
                print('\033[30m|                  {} \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end = '  ')
            else:
                print('\033[30m|                   {} \033[30m|'.format('\033[01m\033[30m' + (hand[one][0][1:])), end='  ')
    print()
    print('\033[30m+---------------------+  ' * len(hand))


def pick_card(hand):
    random = randint(0,end)
    hand.append(cards[random])
    cards.remove(cards[random])


def amount(hand):
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
        pick_card(dealer)
        end -= 2
    total = amount(player)
    print('\nDealer\'s Card: ')
    print_cards(dealer[:1])
    print('Your Cards: ')
    print_cards(player)

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
        total = amount(player)

    print('\n----> Round Results:')
    if total > 21:
        print('\nDealer\'s Card: ')
        print_cards(dealer[:1])
        print('Your Cards: ')
        print_cards(player)
        print('\n\33[31mYou bust!')
        chips -= int(bet)
    else:
        while amount(dealer) < 17:
            pick_card(dealer)
            end -= 1
        print('\nDealer\'s Cards: ')
        print_cards(dealer)
        print('Your Cards: ')
        print_cards(player)
        if amount(dealer) < amount(player) or amount(dealer) > 21:
            print('\n\33[32mYou Win!')
            chips += int(bet)
        else:
            if amount(dealer) == amount(player):
                print('\nPush!')
            else:
                print('\n\33[31mDealer Wins!')
                chips -= int(bet)
    
    cards = reset[:]
    end = 51
    round += 1
    file.seek(13)
    record = file.read()
    if chips > int(record):
        file.seek(13)
        file.write(str(chips))


print('\n\33[30m' + '-'*150)
file.seek(13)
record = file.read()
print('\n\033[31mOut of money!\n\n\033[30mRecord: {} \033[30mchips'.format('\033[33m' + str(record)))
file.close()
