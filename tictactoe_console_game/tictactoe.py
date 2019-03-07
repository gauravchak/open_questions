'''
Tictactoe with simple AI
'''
from typing import Tuple, List

class TTTGameBoard:
    ''' This is the game board class not the AI class '''
    def __init__(self)-> None:
        self.tokens = [['-','-','-'] for x in range(3)]
        self.winner = '-'

    def add(self, i:int, j:int, token:str) -> None:
        if (i< 1 or i >= 4):
            return
        if (j< 1 or j >= 4):
            return
        if self.tokens[i-1][j-1] == '-':
            self.tokens[i-1][j-1] = token
        else:
            # complain
            print ('Error')

    def print(self) -> None:
        for i in range(3):
            print ("{}|{}|{}".format(self.tokens[i][0], self.tokens[i][1], self.tokens[i][2]))

    def is_board_full(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.tokens[i][j] == '-':
                    return False
        return True

    def get_list_of_empty_squares(self) -> List[Tuple[int, int]]:
        list_of_empty_squares = []
        for i in range(3):
            for j in range(3):
                if self.tokens[i][j] == '-':
                    # empty
                    list_of_empty_squares.append((i,j))
        return list_of_empty_squares

    def is_game_over(self) -> bool:
        '''Checks who won. Sets the winner and returns true. If no winner, returns false'''
        for winchar in ['X', 'O']:
            if (self.tokens[0][0] == winchar and self.tokens[0][1] == winchar and self.tokens[0][2] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[1][0] == winchar and self.tokens[1][1] == winchar and self.tokens[1][2] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[2][0] == winchar and self.tokens[2][1] == winchar and self.tokens[2][2] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[0][0] == winchar and self.tokens[1][0] == winchar and self.tokens[2][0] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[0][1] == winchar and self.tokens[1][1] == winchar and self.tokens[2][1] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[0][2] == winchar and self.tokens[1][2] == winchar and self.tokens[2][2] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[0][0] == winchar and self.tokens[1][1] == winchar and self.tokens[2][2] == winchar):
                self.winner = winchar
                return True
            if (self.tokens[0][2] == winchar and self.tokens[1][1] == winchar and self.tokens[2][0] == winchar):
                self.winner = winchar
                return True
        return False

class TTTPlayer:
    ''' This is the AI player of a TicTacToe game '''

    def __init__(self, tttgb :TTTGameBoard)-> None:
        self.tttgb = tttgb
    
    def _rank_possible_moves(self, given_next_moves: List[Tuple[int, int]]) -> List[Tuple[Tuple[int,int], float]]:
        '''Returns a list of tuples of possible moves and scores'''
        ranked_list = []
        for idx, x in enumerate(given_next_moves):
            ranked_list.append((x, 100 - idx))
        return ranked_list

    def play_next_move(self) -> Tuple[int, int]:
        '''
        Make a list of non full squares, return the first one.
        Assumes list 
        '''
        list_of_empty_squares = self.tttgb.get_list_of_empty_squares()
        if not list_of_empty_squares:
            raise ValueError('No legal move exists. Why did you ask me to play!')
        ranked_list = self._rank_possible_moves(list_of_empty_squares)
        x = ranked_list[0][0]
        # Play the chosen move
        self.tttgb.add(x[0]+1, x[1]+ 1, 'O')
        return (x)

class TTTGame:
    '''
    This is a class that enacts one game of TicTacToe where the human player plays first and then
    the AI player and the Human alternate
    while the game board is not full
        if the next_move is user then
        Ask user for a move
        If user won then print "Yay you won!" and exit
        else:
        Ask AI Player to play a move
        If AI won then print ":( AI won" and exit
    If game board full and no one won then print "draw" and return
    '''
    def __init__(self, tttgb:TTTGameBoard, tttpl:TTTPlayer) -> None:
        self.tttgb = tttgb
        self.tttpl = tttpl
        self.next_move_is_user = True

    def play(self) -> None:
        '''
        while the game board is not full
          if the next_move is user then
            Ask user for a move
            If user won then print "Yay you won!" and exit
          else:
            Ask AI Player to play a move
            If AI won then print ":( AI won" and exit
        If game board full and no one won then print "draw" and return
        '''
        self.tttgb.print()
        while not (self.tttgb.is_board_full() or self.tttgb.is_game_over()):
            if self.next_move_is_user:
                print ('Enter next move please as two index numbers like "2 3"')
                user_move = input()
                ulist = user_move.split( )
                if len(ulist) == 2:
                    self.tttgb.add(int(ulist[0]), int(ulist[1]), 'X')
                else:
                    raise ValueError('Error in parsing {}'.format(user_move))
                self.next_move_is_user = False
            else:
                self.tttpl.play_next_move()
                self.tttgb.print()
                self.next_move_is_user = True
        if self.tttgb.is_game_over():
            if self.tttgb.winner == 'X':
                self.tttgb.print()
                print ('You won!')
            elif self.tttgb.winner == 'O':
                self.tttgb.print()
                print ('Computer won!')
            else:
                print ('Weird')
        else:
            self.tttgb.print()
            print ('Draw!')


def __main__():
    # Initialize a gameboard
    tttgb = TTTGameBoard()
    # Initialize an AI TTT player
    tttpl = TTTPlayer(tttgb)
    # Initialize the game 
    tttgame = TTTGame(tttgb, tttpl)
    tttgame.play()

__main__()