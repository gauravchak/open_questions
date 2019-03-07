'''
Tictactoe with simple AI
'''
from typing import Tuple, List
import copy

class TTTGameBoard:
    ''' This is the game board class not the AI class '''
    def __init__(self)-> None:
        self.tokens = [['-']*3 for x in range(3)]
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
            print ('Error i = {} j = {}'.format(i, j))

    def print(self) -> None:
        for i in range(3):
            print ("{}".format('|'.join(self.tokens[i])))

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

    def get_num_paths_to_lose(self) -> int:
        '''Returns the number of ways in which X can win by one move'''
        num_paths_to_lose = 0
        for empty_x in self.get_list_of_empty_squares():
            hyp_tttgb = copy.deepcopy(self)
            hyp_tttgb.add(empty_x[0]+1, empty_x[1]+1, 'X')
            if (hyp_tttgb.is_game_over() and hyp_tttgb.winner == 'X'):
                num_paths_to_lose = num_paths_to_lose + 1
        return num_paths_to_lose

    def is_game_over(self) -> bool:
        '''Checks who won. Sets the winner and returns true. If no winner, returns false'''
        for winchar in ['X', 'O']:
            for i in range(3):
                # check ith row
                line_won = True
                for j in range(3):
                    if (self.tokens[i][j] != winchar):
                        line_won = False
                        break
                if line_won:
                    self.winner = winchar
                    return True
            for j in range(3):
                # check jth column
                col_won = True
                for i in range(3):
                    if (self.tokens[i][j] != winchar):
                        col_won = False
                        break
                if col_won:
                    self.winner = winchar
                    return True
            # Check diagonal
            diag_won = True
            for i in range(3):
                if (self.tokens[i][i] != winchar):
                    diag_won = False
                    break
            if diag_won:
                self.winner = winchar
                return True
            diag_won = True
            for i in range(3):
                if (self.tokens[i][2 - i] != winchar):
                    diag_won = False
                    break
            if diag_won:
                self.winner = winchar
                return True
        return False

class TTTPlayer:
    ''' This is the AI player of a TicTacToe game '''

    def __init__(self, tttgb :TTTGameBoard)-> None:
        self.tttgb = tttgb
    
    def _rank_possible_moves(self, given_next_moves: List[Tuple[int, int]]) -> List[Tuple[Tuple[int,int], float]]:
        '''Given a list of possible moves, it returns a list of tuples of possible moves and scores'''
        ranked_list = []
        for idx, x in enumerate(given_next_moves):
            hyp_tttgb = copy.deepcopy(self.tttgb)
            hyp_tttgb.add(x[0]+1, x[1]+1, 'O')
            if (hyp_tttgb.is_game_over() and hyp_tttgb.winner == 'O'):
                score = 100  # good move so high score
            else:
                # The term 1 of the score will just make us choose the first possible move
                score = (100 - idx)/100 - hyp_tttgb.get_num_paths_to_lose()
            print ('Score allowed move {} {} = {}'.format(x[0], x[1], score))
            ranked_list.append((x, score))
        ranked_list.sort(key=lambda x:x[1], reverse=True)
        # print ('DEBUG list = {}'.format(ranked_list))
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