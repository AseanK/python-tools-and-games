import random
import os
from sys import platform

# Clears command line
def clear():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OS X
        os.system("clear")
    elif platform == "win32":
        # Windows...
        os.system("CLS")
	
# Game grid
GRID = 8
# Number of mines
MINE = 8
# Coulumn values
COL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]


# Intro
def intro():
    clear()
    
    print("""             . . .                         
                                  \|/                          
                                `--+--'                        
                                  /|\                          
        Welcome   to             ' | '                         
                                   |                           
                                   |                           
     THE   Minesweeper!        ,--'#`--.                       
                               |#######|                       
                            _.-'#######`-._                    
                         ,-'###############`-.                 
                       ,'#####################`,               
                      /#########################\              
                     |###########################|             
                    |#############################|            
                    |#############################|            
                    |#############################|            
                    |#############################|            
                     |###########################|             
                      \#########################/              
                       `.#####################,'               
                         `._###############_,'                 
                            `--..#####..--'
	""")
    print("Your goal is to find all the mines in the field and place falgs on all of them!")
    print("\nValid input format:")
    print("ROW SPACE COLUMN   [3 H], [1 F]    : dig")
    print("  Followed by F    [3 H F], [1 F F]: flag\n")


# Grid layout
def layout():

    global display

    st = "   "
    for i in range(GRID):
        st = st + "     " + COL[i]
    print(st)	

    for r in range(GRID):
        st = "     "
        if r == 0:
            for c in range(GRID):
                st = st + "______"	
            print(st)

        st = "     "
        for c in range(GRID):
            st = st + "|     "
        print(st + "|")
        
        st = "  " + str(r + 1) + "  "
        for c in range(GRID):
            st = st + "|  " + str(display[r][c]) + "  "
        print(st + "|")	

        st = "     "
        for c in range(GRID):
            st = st + "|_____"
        print(st + '|')

    print()


# Place -1 value on the random cell -1 = bomb 
def plant_mines():

    global grid_val

    count = 0
    while count < MINE:
        val = random.randint(0, GRID*GRID-1)
        r = val // GRID
        c = val % GRID
        
        if grid_val[r][c] != -1:
            count = count + 1
            grid_val[r][c] = -1


# Get values for each cell
def cell_value():
    global grid_val

    for row in range(GRID):
        for col in range(GRID):

            if grid_val[row][col] == -1:
                continue

            # Check up	
            if row > 0 and grid_val[row-1][col] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check down	
            if row < GRID-1  and grid_val[row+1][col] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check left
            if col > 0 and grid_val[row][col-1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check right
            if col < GRID-1 and grid_val[row][col+1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check top-left	
            if row > 0 and col > 0 and grid_val[row-1][col-1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check top-right
            if row > 0 and col < GRID-1 and grid_val[row-1][col+1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check below-left	
            if row < GRID-1 and col > 0 and grid_val[row+1][col-1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1
            # Check below-right
            if row < GRID-1 and col < GRID-1 and grid_val[row+1][col+1] == -1:
                grid_val[row][col] = grid_val[row][col] + 1


# Display all 0 value neighbours
def neighbours(r, c):
	
    global display
    global grid_val
    global vis

    if [r,c] not in vis:

        vis.append([r,c])

        if grid_val[r][c] == 0:

            display[r][c] = grid_val[r][c]

            if r > 0:
                neighbours(r-1, c)
            if r < GRID-1:
                neighbours(r+1, c)
            if c > 0:
                neighbours(r, c-1)
            if c < GRID-1:
                neighbours(r, c+1)	
            if r > 0 and c > 0:
                neighbours(r-1, c-1)
            if r > 0 and c < GRID-1:
                neighbours(r-1, c+1)
            if r < GRID-1 and c > 0:
                neighbours(r+1, c-1)
            if r < GRID-1 and c < GRID-1:
                neighbours(r+1, c+1)	

        if grid_val[r][c] != 0:
                display[r][c] = grid_val[r][c]


# Check if game over
def check_over():
    global display

    count = 0

    for r in range(GRID):
        for c in range(GRID):

            if display[r][c] != ' ' and display[r][c] != 'F':
                count = count + 1

    if count == GRID * GRID - MINE:
        return True
    else:
        return False
                    

# display all mines
def show_mines():
    global display
    global grid_val

    for r in range(GRID):
        for c in range(GRID):
            if grid_val[r][c] == -1:
                display[r][c] = 'M'


grid_val = [[0 for y in range(GRID)] for x in range(GRID)] 
display = [[' ' for y in range(GRID)] for x in range(GRID)]
flags = []
game_over = False

plant_mines()
cell_value()


# Main
while not game_over:
    intro()

    inp = input("Press enter to start 'q' to quit")
    if inp == "q":
        exit()
    clear()

    layout()

    inp = input("\nEnter row space and column : ").split()

    col = inp[1].lower()
    if col == "a":
        inp[1] = 1
    elif col == "b":
        inp[1] = 2
    elif col == "c":
        inp[1] = 3
    elif col == "d":
        inp[1] = 4
    elif col == "e":
        inp[1] = 5
    elif col == "f":
        inp[1] = 6
    elif col == "g":
        inp[1] = 7
    elif col == "h":
        inp[1] = 8
    elif col == "i":
        inp[1] = 9
    elif col == "j":
        inp[1] = 10
    elif col == "k":
        inp[1] = 11
        

    if len(inp) == 2:
        try: 
            val = list(map(int, inp))
        except ValueError:
            clear()
            print("Wrong input!")
            continue

    elif len(inp) == 3:
        if inp[2] != 'F' and inp[2] != 'f':
            clear()
            print("Wrong Input!")
            continue
        try:
            val = list(map(int, inp[:2]))
        except ValueError:
            clear()
            print("Wrong input!")
            continue

        if val[0] > GRID or val[0] < 1 or val[1] > GRID or val[1] < 1:
            clear()
            print("Wrong input!")
            continue

        r = val[0]-1
        c = val[1]-1	

        if [r, c] in flags:
            clear()
            print("Flag already set")
            continue

        if display[r][c] != ' ':
            clear()
            print("Value already known")
            continue

        if len(flags) < MINE:
            clear()
            print("Flag set")
            flags.append([r, c])
            display[r][c] = 'F'
            continue
        else:
            clear()
            print("Flags finished")
            continue	 

    else: 
        clear()
        print("Wrong input!")	
        continue
        

    # Sanity checks
    if val[0] > GRID or val[0] < 1 or val[1] > GRID or val[1] < 1:
        clear()
        print("Wrong Input!")
        continue
        
    r = val[0]-1
    c = val[1]-1

    if [r, c] in flags:
        flags.remove([r, c])

    if grid_val[r][c] == -1:
        display[r][c] = 'M'
        show_mines()
        layout()
        print("Game Over!")
        game_over = True
        continue

    elif grid_val[r][c] == 0:
        vis = []
        display[r][c] = '0'
        neighbours(r, c)

    else:	
        display[r][c] = grid_val[r][c]

    if(check_over()):
        show_mines()
        layout()
        print("You Win!")
        game_over = True
        continue
    clear()	