import pandas as pd

def pridict(grid, y):
    end = False

    def next_move_win(grid, player):
        get_indexes = lambda x, gird: [i for (y, i) in zip(grid, range(len(grid))) if x == y]
        for index in get_indexes(2, grid):
            #print(index)
            gridc2 = grid.copy()
            gridc2[index] = player
            #printgrid(gridc2)
            for i in range(3):
                if gridc2[3*i] == gridc2[1+ 3*i] and gridc2[1 + i*3] == gridc2[2 + i*3] and gridc2[i*3] == player:
                    return True, index
                elif gridc2[i+3] == gridc2[i+6] and gridc2[i] == gridc2[i+3] and gridc2[i] == player:
                    return True, index
            if (gridc2[0] == gridc2[4] and gridc2[8]== gridc2[4] and gridc2[4] == player) or (gridc2[2]== gridc2[4] and gridc2[6]== gridc2[4] and gridc2[4] == player):
                    return True, index
        return False, -1

    def check_win(gridc):
        for i in range(3):
            if gridc[3*i] == gridc[1+ 3*i] and gridc[1 + i*3] == gridc[2 + i*3] and gridc[i*3] != 2:
                return True, gridc[i*3]
            elif gridc[i+3] == gridc[i+6] and gridc[i] == gridc[i+3] and gridc[i] != 2:
                return True, gridc[i]
        if (gridc[0] == gridc[4] and gridc[8]== gridc[4] and gridc[4] != 2) or (gridc[2]== gridc[4] and gridc[6]== gridc[4] and gridc[4] != 2):
                return True, gridc[4]
        return False, -1

    def check_move(position, player):
        gridc = grid.copy()
        gridc[position] = player
        #print("1 step")
        #printgrid(gridc)
        #print(check_win(gridc))
        return check_win(gridc)
        
    def next_move(bpi, player):
        #only one block left empty
        if len(bpi) == 1:
            grid[bpi[0]] = player
            return check_win(grid)
        if len(bpi) == 0:
            return True, 2
        for i in range(len(bpi)):
            #print("yes")
            result, who = check_move(bpi[i], player)
            if (result and who == player):
                return True, player
        # if in next move opponent win
        #print("yes")
        next_move, to_move = next_move_win(grid, not player)
        #print(next_move,to_move)
        if(next_move):
            grid[to_move] = player
            #print("yes")
            return False, -1
        else:
            #grid[bpi[0]] = player
            return True, 2



    def count(grid):
        get_indexes = lambda x, gird: [i for (y, i) in zip(grid, range(len(grid))) if x == y]
        #print(get_indexes(2,grid))
        # X O blank
        return grid.count(0), grid.count(1), grid.count(2), get_indexes(2, grid)

    #main
    while(not end):
        #printgrid(grid)
        X_count, O_count, blank_count, blank_position_index = count(grid);
        if (X_count <= O_count):
            # X play
            #print("X play")
            end, who = next_move(blank_position_index, 0)
        else:
            # O play
            #print("O play")
            end, who = next_move(blank_position_index, 1)

    if(who == 0):
        data.loc[y, 'Decision'] = 1
        print("1, player")
    elif(who == 1):
        data.loc[y, 'Decision'] = 0
        print("0, computer")
    elif(who == 2):
        data.loc[y, 'Decision'] = 2
        print("tie")

data = pd.read_csv(r"\Solution.csv")
for y in range (0, 4495):
    symbol1 = data.loc[y, 'POS_1']
    symbol2 = data.loc[y, 'POS_2']
    symbol3 = data.loc[y, 'POS_3']
    symbol4 = data.loc[y, 'POS_4']
    symbol5 = data.loc[y, 'POS_5']
    symbol6 = data.loc[y, 'POS_6']
    symbol7 = data.loc[y, 'POS_7']
    symbol8 = data.loc[y, 'POS_8']
    symbol9 = data.loc[y, 'POS_9']
    grid = [symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, symbol8, symbol9]
    pridict(grid, y)
    print(y)

data.to_csv("SolutionFinal.csv", index=False)
