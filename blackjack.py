#|||||||||||||||||||||||||||||||||||||||||||||||
# Black Jack
# by Team Black Jack
# Team: Smriti Ramakrishnan, ER, LB, HC 
#|||||||||||||||||||||||||||||||||||||||||||||||


#|||||||||||||||||||||||||||||||||||||||||||||||
# VARIABLES
#|||||||||||||||||||||||||||||||||||||||||||||||
import random
import time
# counts the  amount of points player and dealer has
# Coder: ER
points_player = 0 # amount of points player has
points_dealer = 0 #amount of points dealer has

#Keeps track of rounds won by player
player_rounds_won = 0


# List to set values for cards
full_deck = {
    "♠A" : 11,
    "♠K" : 10,
    "♠Q" : 10,
    "♠J" : 10,
    "♠10": 10,
    "♠9" : 9,
    "♠8" : 8,
    "♠7" : 7,
    "♠6" : 6,
    "♠5" : 5,
    "♠4" : 4,
    "♠3" : 3,
    "♠2" : 2,
    "♡A" : 11,
    "♡K" : 10,
    "♡Q" : 10,
    "♡J" : 10,
    "♡10": 10,
    "♡9" : 9,
    "♡8" : 8,
    "♡7" : 7,
    "♡6" : 6,
    "♡5" : 5,
    "♡4" : 4,
    "♡3" : 3,
    "♡2" : 2,
    "♣A" : 11,
    "♣K" : 10,
    "♣Q" : 10,
    "♣J" : 10,
    "♣10": 10,
    "♣9" : 9,
    "♣8" : 8,
    "♣7" : 7,
    "♣6" : 6,
    "♣5" : 5,
    "♣4" : 4,
    "♣3" : 3,
    "♣2" : 2,
    "♢A" : 11,
    "♢K" : 10,
    "♢Q" : 10,
    "♢J" : 10,
    "♢10": 10,
    "♢9" : 9,
    "♢8" : 8,
    "♢7" : 7,
    "♢6" : 6,
    "♢5" : 5,
    "♢4" : 4,
    "♢3" : 3,
    "♢2" : 2,
}


#the list of cards 
full_deck_list = list(full_deck) # Coder: Smriti Ramakrishnan

# List to keep track of a player’s and dealer’s cards
player_hand = [] # Coder: Smriti Ramakrishnan
dealer_hand = [] # Coder: Smriti Ramakrishnan

#|||||||||||||||||||||||||||||||||||||||||||||||
# FUNCTIONS
#|||||||||||||||||||||||||||||||||||||||||||||||

# Prints a hello message and the rules of blackjack    
def intro_message(): # Coder: Smriti Ramakrishnan & HC
    print("hello! welcome to black jack!")

    print("this is a card game that tests your luck!")
    print("-------------------------------")
    print("GOAL:")
    print("-------------------------------")
    print("the goal of the game is to get as close to 21 as you can")
    print("without going over.")
    print("you will be playing against the dealer")
    print("so you want a higher number than the dealer w/o going over")
    print("-------------------------------")
    print("RULES:")
    print("-------------------------------")
    print("you will start out with two cards.")
    print("from there you will choose to either:")
    print("hit (get another random card that will add to your total)")
    print("stay (keep the cards you already have)")
    print("if you hit and go over 21, its a bust (you lose)")
    print("                                                      ")
    print("a face card value is 10 and an ace is 11")
    print("jokers are not involved with with game")
    print("-------------------------------")
    print("POINTS:")
    print("-------------------------------")
    print("you will get 1 point for every time you beat the dealer")
    print("at the end of the rounds, we will print your final score")
    print("-------------------------------")
    print("now to start the game choose whether you want to play")
    print("with a timer or rounds:")




# Function to deal the first hand to the dealer and player
# Coder: ER
def deal_cards():
    for i in range(2):
        pnew_card = random.choice(full_deck_list)
        player_hand.append(pnew_card)
        full_deck_list.remove(pnew_card)
        dnew_card = random.choice(full_deck_list)
        dealer_hand.append(dnew_card)
        full_deck_list.remove(dnew_card)
    print("Your cards: " + str(player_hand))
   
    

#Functions for if the player wants to quit, stand (play the hand), or hit (get another card)
def user_turn(p_points): #Coder: HC
    print("The dealer has a", dealer_hand[0])
    if hand_value(player_hand) == 21:
        p_points = p_points
    else:
        while True:
            player_choice = input("(s)tand, (h)it, or (q)uit: ")
            if player_choice == "q":
                return player_choice
            if player_choice == "s":
                print("Your hand is:", str(player_hand) , "and it's value is:", str(hand_value(player_hand)))
                break
            if player_choice == "h":
                xtra_card = random.choice(full_deck_list) 
                player_hand.append(xtra_card)
                #full_deck_list.remove(xtra_card)
                print(player_hand)
                continue
        
        
        
# Determine the computer's algorithm for playing against an opponent
def computer_turn(d_points): # Coder: Smriti Ramakrishnan
    while True:
        if hand_value(player_hand) >= 21:
            break
        elif hand_value(dealer_hand) == 21:
            break
        elif hand_value(player_hand) > hand_value(dealer_hand) or hand_value(player_hand) == 21:
            new_card = random.choice(full_deck_list)
            #full_deck_list.remove(new_card)
            dealer_hand.append(new_card)
            hand_value(dealer_hand)
        else:
            break
    print("The dealer’s hand is:", dealer_hand, "and the dealer's hand value is:", hand_value(dealer_hand))
 
 
 
# Calculates points won per round
def points_calc(p_points, d_points):
    if hand_value(dealer_hand) == hand_value(player_hand):
        print("It's a tie")
        return p_points
    
    elif hand_value(player_hand) > hand_value(dealer_hand):
        if hand_value(player_hand) < 21:
            print("Your hand is higher than the dealer's!")
            p_points += 1
            return p_points
            
        elif hand_value(player_hand) == 21:
            if len(player_hand) == 2:
                print("You have a blackjack!")
                p_points += 2
                return p_points
            else:
                print("You win with 21!")
                p_points += 1
                return p_points
            
        elif hand_value(player_hand) > 21:
            if hand_value(dealer_hand) > 21:
                print("Both player's lose")
                return p_points
                
            elif hand_value(dealer_hand) <= 21:
                print("You busted. Dealer wins")
                d_points += 1
                return p_points
                
    elif hand_value(dealer_hand) > hand_value(player_hand):
        if hand_value(dealer_hand) < 21:
            print("The dealer's hand is higher than yours")
            d_points += 1
            return p_points
            
        elif hand_value(dealer_hand) == 21:
            if len(dealer_hand) == 2:
                print("Dealer has a blackjack")
                d_points += 2
                return p_points
            else:
                print("Dealer wins with 21!")
                d_points += 1
                return p_points
            
        elif hand_value(dealer_hand) > 21:
            if hand_value(player_hand) <= 21:
                print("Dealer busted. You win!")
                p_points = p_points + 1
            return p_points
    

# after each draw and at the beginning of the round, 
# add up the values of each card and store them in a variable
def hand_value(hand):
    hand_total = 0
    num_aces = list(str(hand))
    for i in range (len(hand)):
        hand_total = hand_total + full_deck[hand[i]]
    
    if hand_total > 21:
        for i in range(num_aces.count("A")):
            # Subtract 11 for normal ace count, add one for alternate ace count = 10
            hand_total = hand_total - 10
            if hand_total > 21:
                continue
            else:
                break
    
    return hand_total


# add up games played and the games the player won
# print the amount of winning games for the player and the total games
# print a goodbye message 
def game_stats_calc(points, rounds):  # Coder: LB
    if urounds_or_timer == "r":
        print("You played Black Jack for a total of " + str(num_rounds) + " rounds.")
    print("You won " + str(rounds) + " rounds.")
    print("You scored " + str(points) + " points. Good job!")
    print("Thank you for playing Black Jack!")



#keeps track of the amount of rounds won by player
def rounds_won(rounds):
    if hand_value(player_hand) <= 21 and hand_value(player_hand) > hand_value(dealer_hand):
        rounds = rounds + 1
    elif hand_value(dealer_hand) > 21 and hand_value(player_hand) <= 21:
        rounds = rounds + 1
    return rounds

    
    
#|||||||||||||||||||||||||||||||||||||||||||||||
# MAIN
#|||||||||||||||||||||||||||||||||||||||||||||||



intro_message()
print()
while True:
    points_player = 0
    points_dealer = 0
    player_rounds_won = 0
    urounds_or_timer = input("Do you want to play with (r)ounds, or with a (t)imer?: ")
    if urounds_or_timer == "r":
        num_rounds = int(input("How many rounds do you want? (Type in a number): "))
        print()
        for i in range(num_rounds):
            full_deck_list = list(full_deck)
            player_hand = []
            dealer_hand = []
            deal_cards()
            if user_turn(points_player) != "q":
                computer_turn(points_dealer)
                player_rounds_won = (rounds_won(player_rounds_won))
                points_player = (points_calc(points_player, points_dealer))
            else:
                print("You quit this round")
            print()
    elif urounds_or_timer == "t":
        start_time = time.time()
        deal_cards()
        if user_turn(points_player) != "q":
            computer_turn(points_dealer)
            end_time = time.time()
            total_time = round((end_time - start_time), 0)
            player_rounds_won = (rounds_won(player_rounds_won))
            points_player = (points_calc(points_player, points_dealer))
            print("You took around", str(int(total_time)), "seconds to finish one round!")
        else:
            print("You quit the game")
        print()
    else:
        print("Not an option")
        print()
        continue
    
    game_stats_calc(points_player, player_rounds_won)
    print()
    replay = input("Do you want to play again? (Type (y) for yes and anything else for no): ")
    if replay == "y":
        player_hand = []
        dealer_hand = []
        print()
        continue
    
    
    
    
############################
    else:
        print("Hope you had a good time!")
        break