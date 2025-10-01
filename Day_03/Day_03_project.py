print("Welcome to Treasure  island your mission is to find the treasure")
print("you are at a cross road where do you want to go ?")
step_1 = input("left or right \n")

if step_1 == 'left' :
    print("you've come to a lake ,There is an isLand in the middle of the lake. \n"
          "Type  to wait for a boat, Type swim to swim across . ")
    step_2 = input("\n")
    if step_2 == 'wait' :
        print("now you reached in the island now choose the color of the door ? red , yellow ,blue")
        step_3 = input('\n')
        if step_3 == 'yellow' :
            print("you won .game over")
        else:
            print("you lost .you cannot find the treasure")
    else:
        print("game over. you are trapped in the water")
else:
    print("game over ,you fall into a  hole")

