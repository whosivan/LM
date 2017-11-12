import click
import numpy as np
import pandas as pd

@click.command()
@click.argument('inputpath', type=click.Path(exists=True))
@click.argument('outputpath', type=click.Path())


class LaserMaze():
    """
    Laser maze is a grid of squares, with a single solution. The player has a strating position from which he fires a laser
    in a specific direction (north, south, east, or west). The laser beam travesl through the grid one square at a time. "Solving"
    the maze means letting the laser beam travel through the grid until it hits a wall, or gets stuck in a loop. The "solution" is
    two parts. The first part is the number of squares traversed.
    """
    def __init__(self, inputpath, outputpath):
        self.inputpath = inputpath
        self.outputpath = outputpath
        self.readfile()
        self.result = self.move()
        self.writefile()
    
    def readfile(self):
        with open(self.inputpath, 'r') as f:
            inputf = f.read().split("\\n")
        
        try:
            self.gridsize = list(map(np.int, inputf[0].split(' ')))
        except ValueError:
            raise ValueError("Wrong input file format at grid size '{}'.".format(inputf[0]))
        
        for i in range(1, len(inputf)):
            if len(inputf[i].split(' ')) != 3:
                raise ValueError("Wrong input file format at the {:d}th \\n ({}).".format(i+1, inputf[i]))
            else:
                inputf[i] = inputf[i].split(' ')
        self.location = inputf[1]
        self.location[0] = eval(self.location[0])
        self.location[1] = eval(self.location[1])
        self.inputf = np.array(inputf[2:])
        
        try:
            self.df = pd.DataFrame(self.inputf, columns=['x', 'y', 'mir'])
        except ValueError:
            raise ValueError("Wrong input file format. Please check there is no additional space.")

        self.df.x = self.df.x.astype(np.int)
        self.df.y = self.df.y.astype(np.int)
    
    def move(self):
        maxtraversed = self.gridsize[0] * self.gridsize[1] + int(max(self.gridsize)/2)
        self.traversed = 0
        while True:
            if self.traversed > maxtraversed:
                return -1
            else:
                if self.location[2] == "N":
                    try:
                        mirloc = list(self.df[(self.df.x == self.location[0]) & (self.df.y > self.location[1])].sort_values('y').iloc[0])
                        self.traversed += mirloc[1] - self.location[1]
                        self.location = mirloc
                        if self.location[2] == '\\':
                            self.location[2] = 'W'
                        elif self.location[2] == '/':
                            self.location[2] = 'E'
                        else:
                            raise ValueError("Wrong mark ({}) at x={:d} y={:d}.".format(self.location[2], self.location[0], self.location[1]))
                    except IndexError:
                        self.traversed += self.gridsize[1] - self.location[1]
                        return self.traversed, self.location[0], self.gridsize[1] - 1

                elif self.location[2] == "S":
                    try:
                        mirloc = list(self.df[(self.df.x == self.location[0]) & (self.df.y < self.location[1])].sort_values('y', ascending=False).iloc[0])
                        self.traversed +=  self.location[1] - mirloc[1]
                        self.location = mirloc
                        if self.location[2] == '\\':
                            self.location[2] = 'E'
                        elif self.location[2] == '/':
                            self.location[2] = 'W'
                        else:
                            raise ValueError("Wrong mark ({}) at x={:d} y={:d}.".format(self.location[2], self.location[0], self.location[1]))
                    except IndexError:
                        self.traversed += self.location[1]
                        return self.traversed, self.location[0], 0
            
                elif self.location[2] == "W":
                    try:
                        mirloc = list(self.df[(self.df.y == self.location[1]) & (self.df.x < self.location[0])].sort_values('x', ascending=False).iloc[0])
                        self.traversed +=  self.location[0] - mirloc[0]
                        self.location = mirloc
                        if self.location[2] == '\\':
                            self.location[2] = 'N'
                        elif self.location[2] == '/':
                            self.location[2] = 'S'
                        else:
                            raise ValueError("Wrong mark ({}) at x={:d} y={:d}.".format(self.location[2], self.location[0], self.location[1]))
                    except IndexError:
                        self.traversed += self.location[0]
                        return self.traversed, 0, self.location[1]

                elif self.location[2] == "E":
                    try:
                        mirloc = list(self.df[(self.df.y == self.location[1]) & (self.df.x > self.location[0])].sort_values('x').iloc[0])
                        self.traversed += mirloc[0] - self.location[0]
                        self.location = mirloc
                        if self.location[2] == '\\':
                            self.location[2] = 'S'
                        elif self.location[2] == '/':
                            self.location[2] = 'N'
                        else:
                            raise ValueError("Wrong mark ({}) at x={:d} y={:d}.".format(self.location[2], self.location[0], self.location[1]))
                    except IndexError:
                        self.traversed += self.gridsize[0] - self.location[0]
                        return self.traversed, self.gridsize[0] - 1, self.location[1]

    def writefile(self):
        with open(self.outputpath, 'w') as f:
            if self.result == -1:
                f.write(str(self.result))
            else:
                f.write("{:d}\n{:d} {:d}".format(self.result[0], self.result[1], self.result[2]))
