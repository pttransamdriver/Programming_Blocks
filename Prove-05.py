# Space Adventure on Mars

print("""################################################################################################
################################################################################################""")
print("Welcome to Space Adventure on Mars!")
print("You play as Penny with Bolt, a dog with super powers, as you escape from an alien prison.")
print("""################################################################################################""")
print("Level 1: Escape from the cell") 
print("""################################################################################################""")

print("You and Bolt are locked in a cell. What do you do?")
print("A: Try to pick the lock")
print("B: Tell bolt to use his heat vision")

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
        
        choice3 = input("Choose carfully, this could be it! A, B or C?: ").upper()
        
        if choice3 == "A":
            print("Using Bolt's superspeed and supernose you find the keys in the kitchen and get Bolt a well deserved treat")
            print("!!!! Congratulations !!!!! You and Bolt successfully escaped from Mars and the alien prison.")
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
                    print("**************** THE END **************************")

                elif choice4 == "B":
                    print("B: You short out the rocket and all systems go dark. Oops...")
                    print("Well, that didn't work. You go to engineering and reboot the system")
                    print("")
                choice4 = input("Try again? A or B: ").upper()
            if choice4 == "A":
                    print("A: You open the cubbord and find your keys next to the dog treats!")
                    print("")
                    print("You pick up Bolts communicator to call him back from the backpack search")
                    print("then you see him out the window and he's already on his way.")
                    print("You notice that the aliens are hot on Bolts tail, ready to take you both back to the prison")
                    print("You run up the the bridge with the keys and as soon as bolt's on board")
                    print("you close the bay doors and esacape amid a hailstorm of alien weapon fire.")
                    print("You and Bolt barely make if off Mars in time but with some ship repairs needed. ")
                    print("**************** THE END **************************")

            elif choice4 == "B":
                    print("B: You short out the rocket and all systems go dark. Oops...")
                    print("Well, that didn't work. You go to engineering and reboot the system")
                    print("")
          


else:
    print("Invalid choice. Automatic Game Over")
    print("***************** Game Over **********************")