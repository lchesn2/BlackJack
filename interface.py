from hand import player, dealer


def check_hands():
    if player.hand == dealer.hand or (player.bust and dealer.bust):
        if player.bust and dealer.bust:
            print("Both hands busted.", 'Player:', player.hand, 'Dealer:', dealer.hand)
        else:
            player.bank += player.base_bet
            print("Push.", 'Player:', player.hand, 'Dealer:', dealer.hand)

    elif (dealer.hand > player.hand and not dealer.bust) or player.bust:

        if player.bust:
            print("You busted, you lose.", 'Player:', player.hand, 'Dealer:', dealer.hand)
        else:
            print("You lose.", 'Player:', player.hand, 'Dealer:', dealer.hand)

    elif (player.hand > dealer.hand and not player.bust) or dealer.bust:

        if player.black_jack:
            payout = int(player.base_bet / 5)
            player.bank += payout
            add_winnings3 = player.base_bet * 2
            player.bank += add_winnings3

        else:
            add_winnings2 = player.base_bet * 2
            player.bank += add_winnings2
        if dealer.bust:
            print("Dealer busted, you win.", 'Player:', player.hand, 'Dealer:', dealer.hand)
        else:
            print('You win.', 'Player:', player.hand, 'Dealer:', dealer.hand)

    player.clear_hands()
    dealer.clear_hands()


def dealer_and_check(dealer_turn):
    if dealer_turn:
        while dealer.turn:
            print("Dealer's hand is", dealer.hand)
            if (dealer.hand <= 17 and dealer.has_big_ace) or dealer.hand < 17:
                print("Dealer draws", dealer.draw())
                dealer.check_bust()
            else:
                dealer.turn = False
        check_hands()


def user_interface():
    print("Welcome to Black Jack")
    beginning = True
    while beginning:
        print("\n")
        print('New hand, place your bets in multiples of five')
        player.place_bets()
        # player.lucky_pair()

        player.turn = True
        player.draw()
        dealer.draw()
        player.draw()
        print('Dealer is showing', dealer.draw())

        beginning = False
        if dealer.check_hand_is_21() or player.check_hand_is_21():
            if dealer.black_jack:
                print('Dealer has Black Jack')
            elif player.black_jack:
                print("You have Black Jack")
                player.black_jack = True
            player.turn = False
            dealer.turn = True
            dealer_and_check(dealer.turn)
            beginning = True

        if player.has_big_ace:
            print('Your hand has an Ace')

        if player.hand == 10 or player.hand == 11:
            print("Your hand is", player.hand)
            if player.double_down(player.base_bet):
                player.draw()
                player.turn = False
                dealer.turn = True
                dealer_and_check(dealer.turn)
                beginning = True

        while player.turn:
            print("Your hand is", player.hand)
            try:
                if player.bust:
                    print('Oops, you busted')
                    player.turn = False
                    dealer.turn = True
                    dealer_and_check(dealer.turn)
                    beginning = True
                else:
                    user_answer = int(input("What would you like to do? '1' for hit, '2' for stay: "))

                    if user_answer == 1:
                        print('Player draws', player.draw())
                        player.check_bust()
                    elif user_answer == 2:
                        player.turn = False
                        dealer.turn = True
                        dealer_and_check(dealer.turn)
                        beginning = True
                    else:
                        print("Invalid response")

            except:
                (ValueError)
