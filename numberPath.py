class Problem(object):
    def __init__(self, gd, st_row, st_col, s, path):
        self.grid = self.convert(gd)
        self.path = path
        self.row_start = st_row
        self.col_start = st_col
        self.sum = s

        #Updates the path
        self.path.append(self.grid[st_row][st_col])
        print("Next Value: " +str(self.getCurrVal()))

    def __str__(self):
        line = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                line += str(self.grid[i][j]).ljust(5)
            if(i != len(self.grid)-1):
                line += "\n"
        return line

    def convert(self, gd):
        res = []
        for i in range(len(gd)):
            temp = []
            for j in range(len(gd[i])):
                if(gd[i][j] != None):
                    temp.append((int)(gd[i][j]))
                else:
                    temp.append(None)
            res.append(temp)
        return res

    def getGrid(self):
        res = []
        for i in range(len(self.grid)):
            temp = []
            for j in range(len(self.grid[i])):
                temp.append(self.grid[i][j])
            res.append(temp)
        return res

    def getPath(self):
        res = []
        for i in range(len(self.path)):
            res.append(self.path[i])
        return res

    def getCurrVal(self):
        return self.grid[self.row_start][self.col_start]

def solve(pb):
    print("\nSolving...")
    if((pb.row_start == end_row) & (pb.col_start == end_col) & (pb.sum <= targetValue)):
        print("We reached the target value")
        return pb.path
    elif(pb.sum > targetValue):
        print("We went over the target value. Backing up a step...")
        return None
    else:
        #Current position information
        currVal = pb.getCurrVal()

        #New Problem in case of movement
        newGrid = pb.getGrid()
        newGrid[pb.row_start][pb.col_start] = None
        newSum = pb.sum + currVal
        newPath = pb.getPath()

        #Moving right
        if(pb.col_start < grid_cols - 1):
            if(pb.grid[pb.row_start][pb.col_start + 1] != None):
                showCurrInfo(pb)
                print("Going right")
                print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))

                new_pb = Problem(newGrid, pb.row_start, pb.col_start + 1, newSum, newPath)
                #Shows and solves the new Problem
                print(new_pb)
                solve(new_pb)
        else:
            print("Cannot go right")

        #Moving up
        if(pb.row_start - 1 >= 0):
            if(pb.grid[pb.row_start - 1][pb.col_start] != None):
                showCurrInfo(pb)
                print("Going up")
                print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
                new_pb = Problem(newGrid, pb.row_start - 1, pb.col_start, newSum, newPath)
                #Shows and solves the new Problem
                print(new_pb)
                solve(new_pb)
        else:
            print("Cannot go up")

        #Moving down
        if(pb.row_start < grid_rows - 1):
            if(pb.grid[pb.row_start + 1][pb.col_start] != None):
                showCurrInfo(pb)
                print("Going down")
                print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
                new_pb = Problem(newGrid, pb.row_start + 1, pb.col_start, newSum, newPath)
                #Shows and solves the new Problem
                print(new_pb)
                solve(new_pb)
        else:
            print("Cannot go down")

        #Moving left
        if(pb.col_start - 1 >= 0):
            if(pb.grid[pb.row_start][pb.col_start - 1] != None):
                showCurrInfo(pb)
                print("Going left")
                print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
                new_pb = Problem(newGrid, pb.row_start, pb.col_start - 1, newSum, newPath)
                #Shows and solves the new Problem
                print(new_pb)
                solve(new_pb)
        else:
            print("Cannot go left")

        print("No direction possible. Backing up a step... " +str(pb.path))
        return None

def showCurrInfo(pb):
    #Current position information
    currVal = pb.getCurrVal()
    print("Current coordinates: [" + str(pb.row_start) + "," + str(pb.col_start) + "]")
    print("Current Value: " +str(currVal))
    print("Current Path: " +str(pb.path))

def isValid():
    print("Checking if next move is valid")

def main():
    print("______Program Number Path______")

    #Opening pathdata.txt file
    src = open('./pathdata1.txt', 'r')
    line_count = 1
    grid = []
    for line in src:
        #First line analysis
        if line_count == 1:
            fl_list = line.split()

            global targetValue
            global grid_rows
            global grid_cols
            global end_row
            global end_col
            targetValue = (int)(fl_list[0])
            grid_rows = (int)(fl_list[1])
            grid_cols = (int)(fl_list[2])
            start_row = (int)(fl_list[3])
            start_col = (int)(fl_list[4])
            end_row = (int)(fl_list[5])
            end_col = (int)(fl_list[6])
        #Saving other lines in the grid
        else:
            grid.append(line.split())
        line_count += 1

    pb = Problem(grid, start_row, start_col, 0, [])

    print("Original Matrix")
    print(pb)
    solve(pb)


main()
