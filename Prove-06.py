"""
File: Prove-05.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Amusement park ride requirements.
"""


# Space Adventure on Mars
# For Prove-06 I added an easter egg and a grading system for game completion. Hopefully the user takes the hint when they see the B grade
# Print an introduction to the game
print("""################################################################################################
################################################################################################""")
print("Welcome to Space Adventure on Mars!")
print("You play as Penny with Bolt, a dog with super powers, as you escape from an alien prison.")
print("""################################################################################################""")
print("Level 1: Escape from the cell")
print("""################################################################################################""")


# Print first choices
print("You and Bolt are locked in a cell. What do you do?")
print("A: Try to pick the lock")
print("B: Tell bolt to use his heat vision")
print("C: See if bolt can dig you out of the prison through the floor")


choice1 = input("Quick! You don't have much time! A or B?: ").upper()


if choice1 == "A":
   print("You try to pick the lock but the aliens catch you")
   print("************************ Game Over *********************************")
elif choice1 == "B":
   print("Bolt uses his powers to melt the bars of the cell and you escape.")


   print("")
   print("""################################################################################################""")
   print("Level 2: Get to the spaceship ")
   print("""################################################################################################""")
   print("You and Bolt must get back to your spaceship to escape Mars. What do you do?")
   print("A: Sneak around and see if you can find out what the aliens are up to before you leave")
   print("B: Use Bolt's super speed to tow you on your scooter back to the spaceship")
  
   choice2 = input("A or B?:> ").upper()
  
   if choice2 == "A":
       print("You trip an alarm and go to another cell. The aliens remove Bolt's powers.")
       print("*******************************  Game Over **************************************")
   elif choice2 == "B":
       print("Bolt uses his super speed to get you to the spaceship quickly and safely.")
       print("")
       print("""################################################################################################""")
       print("Level 3: Escape from Mars ")
       print("""################################################################################################""")
       print("You and Bolt must escape from Mars before the aliens catch up. Where did you put your keys!?")
       print("A: Search the ship to find your keys. Hoping they are here somewhere and that you're not wasting time")
       print("B: *Facepalm* YOU LEFT YOUR KEYS IN YOUR BACKPACK AND HAVE TO GO BACK FOR IT!")
       print("C: Send Bolt back for the backpack and tell him to be very fast and to to get caught")
      
       choice3 = input("Choose carefully, this could be it! A, B or C?: ").upper()
      
       if choice3 == "A":
           print("Using Bolt's superspeed and supernose you find the keys in the kitchen and get Bolt a well deserved treat")
           print("**** You beat the game! You did well but your Grade is only a 'B' Try again to do better***")
           print("**** Hint: You can beat this game with an 'A' grade but you need to think outside the original choices ***")
           print("********************  THE END   *****************************")
       elif choice3 == "B":
           print("The aliens catch you looking for your backpack. Game over.")
       elif choice3 == "C":
           print("Bolt confidently Bolt charges back to the prison in search of the keys")
           print("")
           print("But it's been a solid 5min and no sign of the aliens or Bolt")
           print("A: You decide to calm your nerves and get a snack from the kitchen: ")
           print("B: Attempt to hotwire the spaceship")


           choice4 = input("What do you do now?: ").upper()
          
           while choice4 != "A":
               if choice4 == "A":
                   print("A: You open the cubbord and find your keys next to the dog treats!")
                   print("")
                   print("You pick up Bolts communicator to call him back from the backpack search")
                   print("then you see him out the window and he's already on his way.")
                   print("You notice that the aliens are hot on Bolts tail, ready to take you both back to the prison")
                   print("You run up the the bridge with the keys and as soon as bolt's on board")
                   print("you close the bay doors and esacape amid a hailstorm of alien weapon fire.")
                   print("You and Bolt barely make if off Mars in time but with some ship repairs needed. ")
                   print("**** You beat the game but just barely. Your Grade 'C' Try again to do better***")
                   print("**************** THE END **************************")


               elif choice4 == "B":
                   print("B: You short out the rocket and all systems go dark. Oops...")
                   print("Well, that didn't work. You go to engineering and reboot the system")
                   print("")
               choice4 = input("Try again? A or B: ").upper()
           if choice4 == "A":
                   print("A: You open the cupboard and find your keys next to the dog treats!")
                   print("")
                   print("You pick up Bolts communicator to call him back from the backpack search")
                   print("then you see him out the window and he's already on his way.")
                   print("You notice that the aliens are hot on Bolts tail, ready to take you both back to the prison")
                   print("You run up the the bridge with the keys and as soon as bolt's on board")
                   print("you close the bay doors and escape amid a hailstorm of alien weapon fire.")
                   print("You and Bolt barely make if off Mars in time but with some ship repairs needed. ")
                   print("**** You beat the game but just barely. Your Grade 'C' Try again to do better***")
                   print("**************** THE END **************************")


           elif choice4 == "B":
                   print("B: You short out the rocket and all systems go dark. Oops...")
                   print("Well, that didn't work. You go to engineering and reboot the system")
                   print("")
###########################################################################################
#############################  Secret Area easter egg  ####################################
#################### Why did you went to mars in the first place ##########################
###########################################################################################
elif choice1 == "C":
   print("""################################################################################################""")
   print("You follow bolt as he digs down and sideways using your scooter's headlight to see where you're going")
   print("After some time of doing your best dig forward and shove the dirt behind you to keep the aliens from following you, you begin to run out of air")
   print("With you and bolt weakening due to lack of oxygen you come to a very thick concrete wall")
   print("What do you do now?!: ")
   print("A: Tell Bolt to use his heat vision to cut through the wall")
   print("B: Tell Bolt to bark down the walls because you're worried that his heat vision might use the last of your air")
   choice5 = input("You're running out of time! A or B: ").upper()
   print("""################################################################################################""")
   if choice5 == "A":
       print("Bolt's heat vision cuts a circle in the wall. You he push on it till it pops out the other side")
       print("and get a badly needed needed breath of fresh air")
       print("""################################################################################################""")
       print("Once you regain your strength you lookup and see your parents rushing toward you")
       print("You shed grateful tears and tell them you came to rescue them! ")
       print("Your parents gratefully applaud your courage at the same time laughingly scold you for making such a dangerous trip")
       print("Your parents explain that the aliens had abducted them hoping to get their brilliant genetic minds to augment them like Bolt had been")
       print("In captivity they had found that using the aliens genetic code they could give themselves super powers")
       print("They were about to use their new powers to escape when you and bolt burst into their prison laboratory ")
       print("You told them that you have a ship just to the south of the prison. You all decide to escape and make a break for your ship")
       print("**************** Congratulations! You completed the game! Grade of 'A+'  ******************************")
   elif choice5 == "B":
       print("The bark causes a cave in and you and bolt are buried without the air or strength to dig out")
       print("************** Game Over  **********************")



else:
   print("Invalid choice. Automatic Game Over")
   print("***************** Game Over **********************")

