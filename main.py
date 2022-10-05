#Roulette, how long will the game go on?

import random

cash_reserve = 100
#variable holding the starting cash amount for each round
roulette_roll = 0
#variable to hold the roulette rolls
turn_counter = 0
#a counter for the number of turns in each round
total_turns = 0
#a counter for the total number of turns across all rounds
wins_per_visit = 0
#Win counter to be reset each new round
wins_total = 0
#win counter for the total number of win across all rounds

for j in range(10000):
#setting the total number of rounds we want to have played
  wins_per_visit = 0
  #resetting the wins from the round
  turn_counter = 0
  #resetting the turns from the round
  roulette_roll = 0
  #resetting the roulette roll
  cash_reserve = 100
  #resetting the cash reserve
  for i in range(1000000000):
  #setting the total number of times the player can continue playing. 
  ###I found that when I set this too low I cut some games short. So I set it arbitrarily high.###
    if cash_reserve == 0:
    #If the player has lost all their money:
      total_turns = total_turns + turn_counter
      #an addition collecting all turns from the previous round
      wins_total = wins_total + wins_per_visit
      #an addition collecting all wins from the previous round
      break
      #go back to the earlier for loop, and make all the calculations for the totals of the round.
    else:
    #If the player still has money to bet:
      turn_counter += 1
      #add one more turn that the player has played
      cash_reserve -= 1
      #subtract one unit of money from the player's reserve
      roulette_roll = random.randrange(1,38)
      #Roll the roulette wheel for any number between and including 1 and 37.
      if roulette_roll == 27:
        #Picking an arbitrary win roll that the player will bet on
        cash_reserve = cash_reserve + 36
        #If the wheel produces a 27, then the cash reserve has 36 units of money added to it
        wins_per_visit += 1
        #Add one to the counter of total wins.
  
#print("win turn ratio =", win_turn_ratio)
print("wins average across total turns=", wins_total / total_turns)
#This calculates the percentage of wins out of total plays
#Could be interpreted as a factor of wins/100 plays
#Comes out to .0270 just about every time for a high number of rounds

print("The average number of turns (one bet and one roulette roll = one turn) the player was able to participate in, when starting with 100 money units, is:", total_turns/10000)
#This calculates the average number of turns across however many rounds we had the player played
#Seems to fluctuate between 3500-3800 or so 