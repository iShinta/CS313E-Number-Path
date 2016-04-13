class Problem(object):
    def __init__(self, gd, st_row, st_col, s, path):
        self.grid = self.convert(gd)
        self.path = []
        self.row_start = st_row
        self.col_start = st_col
        self.sum = s

        #Inits the first value of path
        self.path.append(self.grid[self.row_start][self.col_start])

    def __str__(self):
        line = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                line += str(self.grid[i][j]).ljust(5)
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

    def copy(self):
        res = []
        for i in range(len(self.grid)):
            temp = []
            for j in range(len(self.grid[i])):
                temp.append(self.grid[i][j])
            res.append(temp)
        return res

def solve(pb):
    print("\nSolving...")
    print(pb)
    if(pb.sum == targetValue):
        print("We reached the target value")
        return pb.path
    elif(pb.sum > targetValue):
        print("We went over the target value")
        return None
    else:
        #Current position information
        print("Current coordinates: [" + str(pb.row_start) + "," + str(pb.col_start) + "]")
        currVal = pb.grid[pb.row_start][pb.col_start]
        print("Current Value: " +str(currVal))

        #New Problem in case of movement
        newGrid = pb.copy()
        newGrid[pb.row_start][pb.col_start] = None
        newSum = pb.sum + currVal

        #Moving right
        if((pb.col_start < grid_cols - 1)):
            print("Going right")
            print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
            new_pb = Problem(newGrid, pb.row_start, pb.col_start + 1, newSum, pb.path.append(currVal))
            #Solve the new Problem
            solve(new_pb)
        #Moving up
        elif(pb.row_start - 1 >= 0 & pb.grid[pb.row_start - 1][pb.col_start] != None):
            print("Going up")
            print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
            new_pb = Problem(newGrid, pb.row_start - 1, pb.col_start, newSum, pb.path.append(currVal))
            #Solve the new Problem
            solve(new_pb)
        #Moving down
        elif(pb.row_start + 1 <= grid_rows):
            print("Going down")
            print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
            new_pb = Problem(newGrid, pb.row_start + 1, pb.col_start, newSum, pb.path.append(currVal))
            #Solve the new Problem
            solve(new_pb)
        #Moving left
        elif((pb.col_start - 1 >= 0) & (pb.grid[pb.row_start][pb.col_start - 1] != None)):
            print("Going left")
            print("Sum was " +str(pb.sum) + ", is now " +str(newSum) +". Target is " +str(targetValue))
            new_pb = Problem(newGrid, pb.row_start, pb.col_start - 1, newSum)
            #Solve the new Problem
            solve(new_pb)
        else:
            print("No direction possible")
            return None

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

    solve(pb)


main()
