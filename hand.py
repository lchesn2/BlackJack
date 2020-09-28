import random


class Hand:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.hand = 0
        self.has_big_ace = False
        self.turn = False
        self.bust = False
        self.black_jack = False

    def clear_hands(self):
        self.hand = 0
        self.has_big_ace = False
        self.turn = False
        self.bust = False
        self.black_jack = False

    def check_bust(self):
        if self.hand > 21:
            self.bust = True

    def check_ace(self, card):
        if self.hand > 11 and card == 1:
            card = 1
        elif self.hand < 11 and card == 1:
            card = 11
            self.has_big_ace = True

        else:
            card = card

        return card

    def draw(self):
        index = random.randint(0, 12)
        self.hand += self.check_ace(self.cards[index])

        if self.hand > 21 and self.has_big_ace:
            self.hand -= 10
            self.has_big_ace = False

        return int(self.cards[index])

    def check_hand_is_21(self):
        if self.hand == 21:
            self.black_jack = True
            return True


class Player(Hand):

    def __init__(self):
        self.base_bet = 0
        self.buster_bet = 0
        self.lucky_pair_bet = 0
        self.bank = 10000
        self.max_bet = 20000
        Hand.__init__(self)

    def check_bet(self, bet):

        if self.bank < bet:
            print("You don't have enough money for this bet")
            return False
        elif bet > self.max_bet:
            print("Bet cannot be greater than $", self.max_bet)
        elif bet % 5 == 0:
            return True
        else:
            print("Bet must be a multiple of five")
            return False

    def place_bets(self):
        if self.bank < 5:
            print("You don't have enough money to place a bet! Better luck next time!")
            exit(-1)
        get_base_bet = True
        while get_base_bet:
            try:
                print("You have $", self.bank)
                base_bet = int(input("How much would you like to bet on the base bet? "))
                if base_bet == 0:
                    print("You must bet at least $5 to play.")
                    get_base_bet = True
                elif self.check_bet(base_bet):
                    self.base_bet = base_bet
                    self.bank -= base_bet
                    get_base_bet = False
                else:
                    get_base_bet = True
            except:
                ValueError

    def lucky_pair(self):
        get_lucky_pair_bet = True
        while get_lucky_pair_bet:
            try:
                print("You have$ $", self.bank)
                lucky_bet = int(input("How much would you like to bet on the lucky pair bet?"))
                if lucky_bet == 0:
                    get_lucky_pair_bet = False
                elif self.check_bet(lucky_bet):
                    self.lucky_pair_bet = lucky_bet
                    self.bank -= lucky_bet
                    get_lucky_pair_bet = False
                else:
                    get_lucky_pair_bet = False
            except:
                ValueError

    def double_down(self, bet):  
        get_double_down_response = True
        while get_double_down_response:
            try:
                double_down = int(input("Would you like to double down? '1' for yes '2' for no: "))
                if double_down == 1:
                    if self.bank < bet:
                        print("Oops, you don't have enough money to double down")
                        get_double_down_response = False
                        return False
                    else:
                        self.base_bet += bet
                        self.bank -= bet
                        self.ddown = True
                        return True
                elif double_down == 2:
                    get_double_down_response = False
                    return False
                else:
                    get_double_down_response = True
            except:
                ValueError


player = Player()
dealer = Hand()
