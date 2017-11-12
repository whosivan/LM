# LM

![alt text](https://github.com/whosivan/LM/blob/master/img/laser_maze.jpg?raw=true "Laser Maze")</p>
**LM_v1.0**

------------------------
Background and Objective
------------------------
Laser maze is a grid of squares, with a single solution. The player has a strating position from which he fires a laser in a specific direction (north, south, east, or west). The laser beam travesl through the grid one square at a time. "Solving" the maze means letting the laser beam travel through the grid until it hits a wall, or gets stuck in a loop. The "solution" is two parts. The first part is the number of squares traversed.

---------
License
---------
This work is under GNU GPLv3 licence, such that it requires anyone who distributes this code or a derivative work to make the source available under the same terms, and also provides an express grant of patent rights from contributors to users.

-----------------------
Software Dependencies
-----------------------
**Package is written in Python 3.x version**</p>
**All the required software is open source.**

Numpy:  [http://www.numpy.org/](http://www.numpy.org/)</p>
Pandas:  [http://pandas.pydata.org/](http://pandas.pydata.org/)</p>
Click:  [http://click.pocoo.org/5/](http://click.pocoo.org/5/)</p>

**Operating system information**

Both Mac OS X and Windows operating system should be able to execute the package in default Python environment.
MAC OS X provides the best user experience*

----------------------
Unittest Results
----------------------
<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/unittest_result.png" alt="...">

----------------------
Package Installation
----------------------
**For Mac:**</p>
Step 1: Open the terminal, type </p>
    `$ python --version`</p>
If your Python version is `Python 3.x` or earlier, please update your Python version.</p>
Step 2: Install dependencies, type</p>
    `$ conda install numpy`</p>
    `$ conda install pandas`</p>
    `$ conda install click`</p>
Step 3: Get the package, type</p>
    `$ git clone https://github.com/whosivan/LM.git`</p>
Step 4: Change directory, type</p>
    `$ cd LM/`</p>
Step 5: Install the package (requires Password), type</p>
    `$ sudo python setup.py install`</p>
Enjoy!

-------------
Command Line Application Example
------------
Step 1: Create input file: </p>
![alt text](https://github.com/whosivan/LM/blob/master/img/inputfileformat.png "inputfile")</p>
Step 2: Enjoy the game, type </p>
        `maze ./path/to/inputfile ./path/to/outputfile`</p>

---------
Folders
---------
**img** - Contains the img used in the ReadME.md.

**Test** - The folder contains unittest codes.

**README.md** - descrption of background, Unittest, Software Installation and dependencies, Folder Descriptions and 
