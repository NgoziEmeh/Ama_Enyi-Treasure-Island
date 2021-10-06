print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Awkuzu Juction.")
print("Your mission is to locate Ama Enyi and get the hidden treasures. Kindly read the readme file for instruction.")

turning_at_igbariam = input("You just reached Awkuzu junction from Nkpor and approaching Igbariam junction.Which way do you want to take? Left or Right:\n").lower()
if turning_at_igbariam == "left":
    print("Welcome to Igbariam Junction.Going straight leads you to Anambra State University campus at Igbariam but there are several villages in between.Some are walkable distances while some are far")
    transport_type = input("How will you like to continue? Walk,Vehicle,Boat or Bike:\n").lower()
    if transport_type == "walk":
        print("It will take you a bit longer to get there")
        print("You just reached River Oyi and it is already 10pm.Curfew starts by 10pm and anyone caught on the way by local vigilante, will be punished if they do not have good explanation for staying out late.")
        wait_at_oyi = input("What do you want to do? type STAY to stay at the river bank and continue in the morning. type CONTINUE to go ahead with the journey and hope for the best\n").lower()
        if wait_at_oyi == "stay":
            print("Good Morning. You are safe and can continue your journey now")
            print("You just crossed River Oyi and approaching Community Primary School")
            continue_from_school = input("Will you like to stop here or continue? type stop or continue:\n").lower()
            if continue_from_school == "stop":
                print("Game over! You cannot stop here.")
            else:
                print("You have reached Afor Junction.")
                from_afor = input("Will you like to take left or right?\n").lower()
                if from_afor == "right":
                    print("Approaching Cata's")
                    cata = input("Do you want to stop or continue?\n").lower()
                    if cata == "stop":
                        cata_turn = input("Turn right or left\n").lower()
                        if cata_turn == "right":
                            print(
                                "Congratulations!! You have reached Ama Enyi.There are 8 houses in Ama Enyi and the treasures are buried in just one of them.To the left of where you are standing,there are houses 1,2,3,4. In front of you,there are house 5 and house 6 behind it,leading to Nwogo river.To your right,there are houses 7 and 8.Hint: The treasure is in a house where no one leaves but guided heavily by unseen gods.")
                            select_house = input("Select a house to enter. Pick from 1 to 8\n")
                            if select_house == "6":
                                print(
                                    "Welcome to the Treasure house. The house has 4 rooms and the treasure is in one of them.")
                                door = input(
                                    "Which door do you want to enter? choose blue, grey, brown or black").lower()
                                if door == "grey":
                                    print(
                                        "Congratulations!!!!! You have done it. You now have the power of life and death in your mouth.Keep yourself pure.Love all men irrespective of background.Medidate untill you have utmost concentration,then pronouce whatever GOOD you desire to see.Remember,you can only keep your power active if you continue dwelling in love and purity")
                                elif door == "blue":
                                    print(
                                        "Game over!.You have entered the room of dangerous animals and have been bitten by a big scorpion. Please get a cure.")
                                elif door == "brown":
                                    print(
                                        "Game over! You have been chosen by the gods to serve them.You have 14 days to get ready for your traditional duties.")
                                elif door == "black":
                                    print(
                                        "Game over! You do not have the treasure but you have contacted power that is beyond your imagination.From now onwards,mind what you use say especially about yourself as your words has power to come through.")
                            else:
                                print("Game over! Sorry. You got the wrong house")


                        else:
                            print("Game over! You have been eaten by animal in the forest you entered")
                    else:
                        print("Game over! Welcome to Ukwulu. You have gone past where you are going.")
                else:
                    print("Game over! You just fell into mmiri ngbanenu")

        else:
            print("Game over! Local vigilante has caught you and believe you are a trespasser.You have been taken to the village jail.")
    #         Going by boat
    elif transport_type == "boat":
        print("Game over! There are no boats available")
    #     Going by vehicle
    elif transport_type == "vehicle":
        print("You will get there faster.Remind the driver to stop you at your bus stop")
        print("You just crossed River Oyi and approaching Community Primary School")
        continue_from_school = input("Will you like to stop here or continue? type stop or continue:\n").lower()
        if continue_from_school == "stop":
            print("Game over! You cannot stop here.")
        else:
            print("You have reached Afor Junction.")
            from_afor = input("Will you like to take left or right?\n").lower()
            if from_afor == "right":
                print("Approaching Cata's")
                cata = input("Do you want to stop or continue?\n").lower()
                if cata == "stop":
                    cata_turn = input("Turn right or left\n").lower()
                    if cata_turn == "right":
                        print(
                            "Congratulations!! You have reached Ama Enyi.There are 8 houses in Ama Enyi and the treasures are buried in just one of them.To the left of where you are standing,there are houses 1,2,3,4. In front of you,there are house 5 and house 6 behind it,leading to Nwogo river.To your right,there are houses 7 and 8.Hint: The treasure is in a house where no one leaves but guided heavily by unseen gods.")
                        select_house = input("Select a house to enter. Pick from 1 to 8\n")
                        if select_house == "6":
                            print(
                                "Welcome to the Treasure house. The house has 4 rooms and the treasure is in one of them.")
                            door = input("Which door do you want to enter? choose blue, grey, brown or black").lower()
                            if door == "grey":
                                print(
                                    "Congratulations!!!!! You have done it. You now have the power of life and death in your mouth.Keep yourself pure.Love all men irrespective of background.Medidate untill you have utmost concentration,then pronouce whatever GOOD you desire to see.Remember,you can only keep your power active if you continue dwelling in love and purity")
                            elif door == "blue":
                                print(
                                    "Game over!.You have entered the room of dangerous animals and have been bitten by a big scorpion. Please get a cure.")
                            elif door == "brown":
                                print(
                                    "Game over! You have been chosen by the gods to serve them.You have 14 days to get ready for your traditional duties.")
                            elif door == "black":
                                print(
                                    "Game over! You do not have the treasure but you have contacted power that is beyond your imagination.From now onwards,mind what you use say especially about yourself as your words has power to come through.")
                        else:
                            print("Game over! Sorry. You got the wrong house")


                    else:
                        print("Game over! You have been eaten by animal in the forest you entered")
                else:
                    print("Game over! Welcome to Ukwulu. You have gone past where you are going.")
            else:
                print("Game over! You just fell into mmiri ngbanenu")
    # Going on Bike
    elif transport_type == "bike":
        print("You just crossed River Oyi and approaching Community Primary School")
        continue_from_school = input("Will you like to stop here or continue? type stop or continue:\n").lower()
        if continue_from_school == "stop":
            print("Game over! You cannot stop here.")
        else:
            print("You have reached Afor Junction.")
            from_afor = input("Will you like to take left or right?\n").lower()
            if from_afor == "right":
                print("Approaching Cata's")
                cata = input("Do you want to stop or continue?\n").lower()
                if cata == "stop":
                    cata_turn = input("Turn right or left\n").lower()
                    if cata_turn == "right":
                        print("Congratulations!! You have reached Ama Enyi.There are 8 houses in Ama Enyi and the treasures are buried in just one of them.To the left of where you are standing,there are houses 1,2,3,4. In front of you,there are house 5 and house 6 behind it,leading to Nwogo river.To your right,there are houses 7 and 8.Hint: The treasure is in a house where no one leaves but guided heavily by unseen gods.")
                        select_house = input("Select a house to enter. Pick from 1 to 8\n")
                        if select_house == "6":
                            print("Welcome to the Treasure house. The house has 4 rooms and the treasure is in one of them.")
                            door = input("Which door do you want to enter? choose blue, grey, brown or black").lower()
                            if door == "grey":
                                print("Congratulations!!!!! You have done it. You now have the power of life and death in your mouth.Keep yourself pure.Love all men irrespective of background.Medidate untill you have utmost concentration,then pronouce whatever GOOD you desire to see.Remember,you can only keep your power active if you continue dwelling in love and purity")
                            elif door == "blue":
                                print("Game over!.You have entered the room of dangerous animals and have been bitten by a big scorpion. Please get a cure.")
                            elif door == "brown":
                                print("Game over! You have been chosen by the gods to serve them.You have 14 days to get ready for your traditional duties.")
                            elif door == "black":
                                print("Game over! You do not have the treasure but you have contacted power that is beyond your imagination.From now onwards,mind what you use say especially about yourself as your words has power to come through.")
                        else:
                            print("Game over! Sorry. You got the wrong house")


                    else:
                        print("Game over! You have been eaten by animal in the forest you entered")
                else:
                    print("Game over! Welcome to Ukwulu. You have gone past where you are going.")
            else:
                print("Game over! You just fell into mmiri ngbanenu")

else:
    print("Game over! You are heading to Nkwelle,Awkuzu")