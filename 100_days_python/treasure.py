  
print('''                  ::: =,    ;
                             ;;=;;===      M
                ,=YVRMBBMMR=,   :i=
              :iVRRMMMMMMBMMM :=;  ==;======
             =tYMMMMMMBBMMM;=Y ,::;==iMMMMMMMMMM
            ;tYVBBMMVMMMM =; .,,,::;;=YVBBMMMMMMMMM
            ;tYVVYRMMM;=ti ...,,,;::==iMVMMMMMMMMMMMM
            ,=tYRBM;;tVB, ....,  ,::;====YVBMMMMMMMMMM
        ..   ,=t =tYVRB, .....,,,,=:;:;;i=VYMMRMMMMMMMM
       ;;..  ,===iYVVRY .....,,,;,,,,,:;;==t=RBMMMMMMMMM
     :;;:;=;,...       .......,,,,,,,,,:;;==Y=tYMMMMMMMM
    ;.,:,.....         ....,,,,,,,,,,,,,:;;;==YYMRMMMMMM
    .......             .,,,,,,,,,,,,,,,,::;;;=YtVBMMMMM
  ;t ...                .,,,,,,,,,,,,,,,,,::;;i=RiRMMMMM
  ,=..                    .,,,,,,,,,,,,,,,:::;;=iYBBMM
                           .,,,,,,,,,,,,,,,,::;;;;tVB
          :VMM               .,,,,,,,,,,,,:,,,::;;=
         ,;VBM                 .,,,,,,,,,,,,,:,::
         ,,==                      `,,,,,,,         
''')

print("Welcome to the treasure Island")
print("Your mission is to find the hidden treasure!")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat.Type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors. Red, Yellow and blue. Which colour do you want to choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win")
        elif choice3 == "red":
            print("It's a room full of fire. Game over!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You have chosen a door that doesn't exist. Game over")
        
    else:
        print("You are attacked by an angry crocodile. Game over.")
else:
    print("Game Over")