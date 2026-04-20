class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Board:
    valid_moves = ["upper left", "upper center", "upper right", 
                   "middle left", "center", "middle right", 
                   "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    # Using provided methods from assignment
    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check for Cat's Game
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
        
        # Check Win Conditions
        win = False
        # (Row/Col/Diag logic provided in prompt)
        for i in range(3): # Rows
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
        if not win:
            for i in range(3): # Cols
                if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
        if not win:
            if self.board_array[1][1] != " ": # Diagonals
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]: win = True
                if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]: win = True

        if win:
            winner = "O" if self.turn == "X" else "X"
            return (True, f"{winner} wins!")
        if cat:
            return (True, "Cat's Game.")
        return (False, f"{self.turn}'s turn.")

# Mainline Implementation
if __name__ == "__main__":
    game_board = Board()
    game_over = False
    
    while not game_over:
        print(game_board)
        status = game_board.whats_next()
        print(status[1])
        
        if status[0]:
            break
            
        move_input = input("Enter move (e.g., 'center', 'upper left'): ").lower().strip()
        try:
            game_board.move(move_input)
        except TictactoeException as e:
            print(f"Error: {e.message}")