import click
import numpy as np
import pandas as pd

@click.command()
@click.argument('inputpath', type=click.Path(exists=True))
@click.argument('outputpath', type=click.Path())

class LaserMaze():
    def __init__(self, inputpath, outputpath):
        self.inputpath = inputpath
        self.outputpath = outputpath
        self.readfile()
        self.result = self.move()
        self.writefile()
    
    def readfile(self):
        with open(self.inputpath, 'r') as f:
            inputf = f.read().split("\\n")
        for i in range(len(inputf)):
            inputf[i] = inputf[i].split(' ')
        self.gridsize = list(map(np.int, inputf[0]))
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

            else:
                f.write("{:d}\n{:d} {:d}".format(self.result[0], self.result[1], self.result[2]))
