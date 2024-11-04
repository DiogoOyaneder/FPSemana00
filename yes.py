room_descriptions = [
[ "A" , "B" , "C" , "D" ,"E"],
[ "F" , "G" , "H" , "I" , "J"],
["K", "L", "M","N", "O" ],
[ "P", "Q", "R", "S", "T"],
[ "U", "V", "W", "X", "y"]
]

position = (2, 2)

room_exits = [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True) ],
[(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False) ] ,
[(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True) ] ,
[(True, False, True, False), (False, True, True, False), (True, True, False, True), (False, True, False, True), (True, False, True, False) ],
[(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]

while (True):
    x, y = position
    description = room_descriptions[y][x]
    print(position, ":", description)
    print("What now?")
    command = input()
    if command == "north":
        print("You move north...")
        y = y -1
    elif command == "south":
        print("You move south...")
        y = y + 1
    elif command == "east":
        print("You move east...")
        x= x + 1
    elif command == "west":
        print("You move west...") 
        x = x - 1
    elif command == "goodbye":
        break

    else:
        print("I don't understand",command)
    if command == "north":
        if (room_exits[y][x][NORTH]):
            print("You move north...")
            y = y -1
        else:
            print("Can't move north!")
    if command == "south":
        if (room_exits[y][x][SOUTH]):
            print("You move south...")
            y = y +1
        else:
            print("Can't move south!")
    if command == "east":
        if (room_exits[y][x][EAST]):
            print("You move east...")
            x =  x + 1
        else:
            print("Can't move east!")
    if command == "west":
        if (room_exits[y][x][WEST]):
            print("You move west...")
            x =  x + 1
        else:
            print("Can't move west!")
    position = (x,y)
#broken fix later :)