import math, random

jokers=False

number_of_decks=1

cards_per_deck=52

cards_per_hand=2

players=3

blackjack = 21

limit_cards_per_hand = 5

house_player=True

house_rule_play_while_less_than = 16

suits = ['clubs', 'diamonds', 'hearts', 'spades']

ace_high = False

face_cards = ['ace','2','3','4','5','6','7','8','9','10','jack', 'queen', 'king']



cards_per_suit = cards_per_deck/len(suits)

def tallied_choose_card(previous_chosen_cards):
    card = None
    while card == None or card in previous_chosen_cards:
        card = int(random.random()*number_of_decks*cards_per_deck)
    return card

def deal_card(hand, count_high=True):
    card = tallied_choose_card(previously_chosen_cards)
    previously_chosen_cards.append(card)
    face_value = card%cards_per_suit
    hand_value = face_value+1
    if hand_value > 10:
        hand_value = 10
    
    if count_high and hand_value ==1 and sum(hand)+11<=blackjack:
        hand_value=11
    
    if 11 in hand and sum(hand)>blackjack:
        print 'replacing ace 11 with ace 1'
        hand.replace(11, 1)
    
    hand.append(hand_value)
    print face_cards[face_value], 'of', suits[card/cards_per_suit]
    print 'total: ', sum(hand)
    
def player_choice():
    return choice
    
def house_choice():
    return choice
    
deal_card.previously_chosen_cards = []

previously_chosen_cards = []

all_hands=[]

hand = []

input='y'

print "cards per suit: ", cards_per_suit

while input=='y':
    for j in range(players):
        #begin each hand as the first after starting a game (default, )
        input='y'
        
        #print which player this hand is being dealt to
        print 'player',j+1
        for i in range(cards_per_hand):
            deal_card(hand)
        
        #if there's no house player or this is not the houseplayer and player has not won or bust
        if not house_player or (house_player and j != (players-1)) and sum(hand)<blackjack:
            input=raw_input('another card?')
        #if there is a house player, make the houses choices
        elif house_player and j==(players-1):
            #if hand is more than the min req hand for house
            if sum(hand) > house_rule_play_while_less_than:
                #stay
                input = 'n'
            #if hand is less than the house rule for min hand
            else:
                #hit
                input = 'y'
                
        #for any player, stay on blackjack!
        if sum(hand)==blackjack:
            input='n'
        
        
        while input=='y':
            deal_card(hand)
            
            if house_player and j == (players-1):
                print 'house'
                if sum(hand) < house_rule_play_while_less_than:
                    print 'following house rules'
                    input = 'y'
                else:
                    print 'stay'
                    input = 'n'
            else:
                print 'player', j+1, 'has', len(hand), 'of', limit_cards_per_hand
                if len(hand) < limit_cards_per_hand and sum(hand)<blackjack:
                    
                    input=raw_input('another card?')
                else:
                    if sum(hand) > blackjack:
                        print 'bust!'
                        
                    elif sum(hand) == blackjack:
                        print 'blackjack!'
                        
                    else:
                        print 'all cards'
                    input='n'
        
        #print hand
        if sum(hand)>blackjack:
            all_hands.append(0)
        else:
            all_hands.append(sum(hand))
        
        hand = []
        winner = [0,all_hands[0]]
    
    #print all_hands
    for k in range(0,players):
        #print k
        if winner[1]<all_hands[k]:
            winner[0]=k
            winner[1]=all_hands[k]
            #winner.append(k)
            
    print 'player', winner[0]+1, 'wins!'
    all_hands = []
    #print previously_chosen_cards
    input= raw_input('play a hand?')
    
    