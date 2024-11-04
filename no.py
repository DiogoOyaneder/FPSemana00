room_descriptions = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y"]
]

room_exits = [
    [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)],
    [(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, False, True), (False, True, False, True), (True, False, True, False)],
    [(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]
]

position = (2, 2)

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

while True:
    x, y = position
    description = room_descriptions[y][x]
    print(position, ":", description)
    print("What now?")
    command = input().lower()

    if command == "north":
        if room_exits[y][x][NORTH]:
            print("You move north...")
            y -= 1
        else:
            print("Can't move north!")
    elif command == "south":
        if room_exits[y][x][SOUTH]:
            print("You move south...")
            y += 1
        else:
            print("Can't move south!")
    elif command == "east":
        if room_exits[y][x][EAST]:
            print("You move east...")
            x += 1
        else:
            print("Can't move east!")
    elif command == "west":
        if room_exits[y][x][WEST]:
            print("You move west...")
            x -= 1
        else:
            print("Can't move west!")
    elif command == "goodbye":
        break
    else:
        print("I don't understand", command)

    # Update position
    position = (x, y)
