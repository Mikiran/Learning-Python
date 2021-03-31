def tictac():
    mapA = [[" ", "|", " ", "|", " "],
            [" ", "|", " ", "|", " "],
            [" ", "|", " ", "|", " "]]

    def printMap():
        # prints out the map
        map = ["".join(mapA[0]),
               "".join(mapA[1]),
               "".join(mapA[2])]
        print(map[0])
        print(map[1])
        print(map[2])

        # makes a list of just the fields with x and o
        mapB = [map[0].split("|"),
                map[1].split("|"),
                map[2].split("|")]

        for x in range(3): # converts the board to numbers
            for y in range(3):
                if mapB[x][y] == "X":
                    mapB[x][y] = 1
                elif mapB[x][y] == "O":
                    mapB[x][y] = -1
                elif mapB[x][y] == " ":
                    mapB[x][y] = 0

        for x in range(3):
            if abs(sum(mapB[x])) == 3: # checks for full rows
                return "END"
            elif abs(int(mapB[0][x]) + int(mapB[1][x]) + int(mapB[2][x])) == 3: # checks for full columns
                return "END"
        if abs(int(mapB[0][0]) + int(mapB[1][1]) + int(mapB[2][2])) == 3: # checks for full right diagonal
            return "END"
        elif abs(int(mapB[0][2]) + int(mapB[1][1]) + int(mapB[2][0])) == 3: # checks for full left diagonal
            return "END"
        counter = 0


    def choice(): # allows the user to choose O or X
        print("O or X?")
        symbol = input().lower() # case insensitive
        if symbol == "o":
            return ["O", "X"]
        elif symbol == "x":
            return ["X", "O"]
        else:
            print("Invalid symbol")
            return choice() # restarts the function if the user input neither O nor X

    def placement(symbol):
        print("Place " + symbol + " in form: rowNumber columnNumber")
        x = input()
        coordinates = x.split(" ")
        while len(coordinates) != 2 or coordinates[0].isnumeric() != True or coordinates[1].isnumeric() != True:
            print("Invalid input.")
            print("Place " + symbol + " in form: rowNumber columnNumber")
            x = input()
            coordinates = x.split(" ")
        while mapA[int(coordinates[0]) - 1][int(coordinates[1]) * 2 - 2] != " ":
            if mapA[int(coordinates[0]) - 1][int(coordinates[1]) * 2 - 2] != " ":
                print("That space is taken.")
            else:
                print("Invalid input.")

            print("Place " + symbol + " in form: rowNumber columnNumber")
            x = input()
            coordinates = x.split(" ")

        if coordinates[0] == "1" and coordinates[1] == "1":
            mapA[0][0] = symbol
        elif coordinates[0] == "1" and coordinates[1] == "2":
            mapA[0][2] = symbol
        elif coordinates[0] == "1" and coordinates[1] == "3":
            mapA[0][4] = symbol
        elif coordinates[0] == "2" and coordinates[1] == "1":
            mapA[1][0] = symbol
        elif coordinates[0] == "2" and coordinates[1] == "2":
            mapA[1][2] = symbol
        elif coordinates[0] == "2" and coordinates[1] == "3":
            mapA[1][4] = symbol
        elif coordinates[0] == "3" and coordinates[1] == "1":
            mapA[2][0] = symbol
        elif coordinates[0] == "3" and coordinates[1] == "2":
            mapA[2][2] = symbol
        elif coordinates[0] == "3" and coordinates[1] == "3":
            mapA[2][4] = symbol
        return printMap()

    symbol = choice()
    printMap()
    end = ""

    while end != "END":

        end = placement(symbol[0])

        if end == "END":
            print("Game Finished")
            break
        end = placement(symbol[1])
        if end == "END":
            print("Game Finished")
            break


tictac()