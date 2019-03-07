'''
Given rows:int cols:int mines:List[Tuple[int,int]]
'''
from typing import List, Tuple
import numpy

class QuitGameException(Exception):
    pass

class InvalidMoveException(Exception):
    pass


class MineSweeperGame:
    '''
    Initialize in __init__ with specs
    Export function play()
    The wat t use this is to create an object of this class and then call play().
    Internal functions:
    '''

    def __init__(self, rows: int, cols: int, mines:List[Tuple[int, int]]) -> None:
        # Store spec-variables
        self.rows = rows
        self.cols = cols
        self.mines = mines

        # Create internal variables
        self.game_finished = False
        if self.rows <= 0:
            self.game_finished = True
            return
        if self.cols <= 0:
            self.game_finished = True
            return

        # The nm_squares_left variable is used to see if the game was won.
        # This will be reduced for number of mines first.
        # Then on every play this will be reduced based on hw many squares we uncover.
        self.nm_squares_left = (rows * cols) - len(mines)  
        # After the following step, self.squares and self.open will be valid
        self._build_game_board()
    
    def play(self)-> None:
        '''
        Runs the game and exits when the game is finished
        '''
        self._print_welcome()
        while ( not self.game_finished ):
            self._print_game_board()
            try:
                i, j = self._ask_for_next_move()
            except QuitGameException:
                print ('Ending Game')
                break
            except InvalidMoveException as ustr:
                print ('Invalid move {}. Try writing something like "1 2"'.format(str(ustr)))
            else:
                retval = self._check_outcome_of_move(i, j)
                if retval == 0:
                    if (self.nm_squares_left == 0):
                        self._print_success_string()
                        self._open_mines()
                        self._print_game_board()
                        self.game_finished = True
                elif ( retval == 1 ):
                    self._print_already_open(i, j)
                elif ( retval == 2 ):
                    self._print_invalid_coordinates(i, j)
                elif ( retval == 3 ):
                    self._print_failure_string()
                    self._open_mines()
                    self._print_game_board()
                    self.game_finished = True
 
    def _print_welcome(self)->None:
        print('Starting game')
        print('Please enter the coordinate of what square you want to open. Like "1 1" for top left and "{} {}" for bottom right'.format(self.rows, self.cols))

    def _open_mines(self)->None:
        # For all mines, set the value to -1
        for mine_coords in self.mines:
            if self._is_valid_coord(mine_coords[0], mine_coords[1], True):
                self.squares[mine_coords[0]-1, mine_coords[1]-1] = -1

    def _ask_for_next_move(self) -> Tuple[int, int]:
        '''
        If the given string is 'quit' then raise QuitGameException
        If the string is valid then parse and return a tuple of ints corresponding to the indexes.
        So 1 1 is returned as [0,0]
        '''
        user_str = input('Enter move: ')
        if user_str == 'quit':
            raise QuitGameException
        uwords = user_str.split()
        try:
            # -1 is done to make it an index for arrays
            return(int(uwords[0])-1, int(uwords[1])-1)
        except ValueError:
            raise InvalidMoveException(user_str)
        return (-1, -1)  # invalid 
    
    def _check_outcome_of_move(self, rowidx:int, colidx:int) -> int:
        '''
        Note that it takes index values and not row and column numbers as inputs. 
        So 0, 0 is top left
        retval: 0 means valid move
        1 means already open, try again
        2 means invalid coordinates, try again
        3 means mine found and game has to be finished
        '''
        if self.open[rowidx, colidx] == 1:
            return 1
        if (rowidx < 0 or rowidx>= self.rows):
            return 2
        if (colidx < 0 or colidx>= self.cols):
            return 2
        self.open[rowidx, colidx] = 1
        # decrement nm_squares_left everytime we set a self.open value to 1
        self.nm_squares_left = self.nm_squares_left - 1
        if self.squares[rowidx, colidx] == 0:
            # We are calling the following for an open square with value 0
            self._recurse_open(rowidx, colidx)
        if self.squares[rowidx, colidx] == -1:
            return 3        
        return 0

    def _recurse_open(self, rowidx:int, colidx:int) -> None:
        '''Assumes that indices are valid and point to an open square with value 0
        '''
        for (delr, delc) in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            if self._is_valid_coord(rowidx + 1 + delr, colidx + 1 + delc):
                # if cell was open then nothing to do
                if self.open[rowidx + delr, colidx + delc] == 0:
                    # if it was not open then open it if it is not a mine and ...
                    if self.squares[rowidx + delr, colidx + delc] != -1:
                        self.open[rowidx + delr, colidx + delc] = 1
                        self.nm_squares_left = self.nm_squares_left - 1
                    # ... if it was 0 then recurse open
                    if self.squares[rowidx + delr, colidx + delc] == 0:
                        self._recurse_open(rowidx + delr, colidx + delc)
                    # if -1 then error since it should not 0

    def _print_success_string(self) -> None:
        print ('You won :)')

    def _print_failure_string(self) -> None:
        print ('You lost :(')

    def _print_game_board(self) -> None:
        '''Prints the game board
        '''
        for r in range(self.rows):
            line_str = ""
            for c in range(self.cols):
                # If it is a mine then there is nothing to be done
                if (self.open[r, c] == 0):
                    line_str = line_str + '-' + ' '
                else:
                    if self.squares[r, c] == -1:
                        line_str = line_str + 'M' + ' '
                    else:
                        line_str = line_str + str(int(self.squares[r, c])) + ' '
            print(line_str)


    def _print_already_open(self, row:int, col:int) -> None:
        print ('The cell you tried to open ({}:{}) is already open'.format(row, col))

    def _print_invalid_coordinates(self, row:int, col:int) -> None:
        print ('The cell you tried to open ({}:{}) is invalid'.format(row, col))
        print ('Row should be between 1 and {}'.format(self.rows))
        print ('Col should be between 1 and {}'.format(self.cols))

    def _is_valid_coord(self, row:int, col:int, complain:bool=False)-> bool:
        if (row >= 1 and row <= self.rows) and (col >= 1 and col <= self.cols):
            return True
        else:
            if complain:
                print ('Complain {} {}'.format(row, col))
            return False
    
    def _build_game_board(self) -> None:
        '''
        This function is called once in the beginning
        Assume rows >= 1 and cols >= 1
        '''
        # self.squares[i,j] = -1 if it is a mine, and >= 0 otherwise deending on the number of mines in the neighborhood
        self.squares = numpy.zeros(shape=(self.rows, self.cols))
        # self.open[i,j] = 0 if it is not open and 1 otherwise
        self.open = numpy.zeros(shape=(self.rows, self.cols))
        # For all mines, set the value to -1
        for mine_coords in self.mines:
            if self._is_valid_coord(mine_coords[0], mine_coords[1], True):
                self.squares[mine_coords[0]-1, mine_coords[1]-1] = -1
        # Then build positive numbers in the squares
        for r in range(self.rows):
            for c in range(self.cols):
                # If it is a mine then there is nothing to be done
                if (self.squares[r, c] != -1):
                    num_mines_in_hood = 0
                    for x in [(r-1, c-1), (r-1, c), (r-1, c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)]:
                        # If this is a valid coordinate ...
                        if self._is_valid_coord(x[0]+1, x[1]+1, False):
                            # ... and if this is a mine then increment num_mines_in_hood
                            if (self.squares[x[0], x[1]] == -1):
                                num_mines_in_hood = num_mines_in_hood + 1
                    self.squares[r, c] = num_mines_in_hood

if __name__ == "__main__":
    msgame = MineSweeperGame(5, 5, [(2,2),(3,3),(4,4)])
    msgame.play()