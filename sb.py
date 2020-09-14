# Calculate hold for American odds
# Takes 2 command-line arguments - Favourite and Underdog American odds

import sys


# Convert Decimal to American odds (amount to bet to win)
# e.g. 1.91 -> -110
# e.g. 2.35 -> +135
def convert_to_american(decimal_odds):
    if decimal_odds < 2:
        return round(100 / (1 - decimal_odds))
    else:
        return (decimal_odds - 1) * 100

# Convert American to decimal odds (decimal odds aka return per dollar)
# e.g. -110 -> 1.91
# e.g. +135 -> 2.35
def convert_to_dec(american_odds):
    if american_odds < 0:
        bet_size = -american_odds
        profit = 100
        total = bet_size + profit
        dec_odds = total / bet_size
        return round(dec_odds, 2)
    else:
        return (american_odds + 100) / 100


# Calculate hold - Hold is the profit that books make if there were even bets on both sides
# Takes odds in American
def hold(fav_odds, dog_odds):
    dog_decimal = convert_to_dec(dog_odds)
    fav_bets = -fav_odds
    fav_profit = 100
    dog_bets = (fav_bets + fav_profit) / dog_decimal

    total = fav_bets + dog_bets
    payout = fav_bets + 100 # The payout amount to the winner

    return (total - payout) / total


# Calculate holds for decimal values
def dec_hold(fav_odds, dog_odds):
    fav_bets = 100 # Assuming a bet of 100 on the favourites
    total_return = 100 * fav_odds
    dog_bets = total_return / dog_odds

    total_bets = fav_bets + dog_bets

    return (total_bets - total_return) / total_bets



# Calculate the probability required to breakeven for a given decimal odd 
# Derived from Expected Value formula
def breakeven(decimal_odds):
    return 1 / decimal_odds


# Take program input
fav_odds = float(sys.argv[1])
dog_odds = float(sys.argv[2])

# Output the breakeven and hold percentage
print("Breakeven: " + str(round(breakeven(fav_odds), 2)))
print("Breakeven: " + str(round(breakeven(dog_odds), 2)))
print("Hold = " +  str(round(dec_hold(fav_odds, dog_odds) * 100, 2)) + "%")
