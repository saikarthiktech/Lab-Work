from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("================================")
        print("        CONNECT FOUR")
        print("================================")
        print("You are X.")
        print("AI is O.")
        print("Enter a column number from 1 to 7.")
        print("Enter q to quit.\n")

        while True:

            # Display the current board
            self.board.print()

            # Human player's turn
            if self.turn == "X":

                raw = input("Column (1-7), or q: ").strip().lower()

                # Quit the game
                if raw == "q":
                    print("Game ended.")
                    return

                # Convert input to integer
                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Invalid input. Enter a number from 1 to 7.\n")
                    continue

                # Check column range
                if not 0 <= col < 7:
                    print("Please enter a column from 1 to 7.\n")
                    continue

            # AI player's turn
            else:
                print("AI is thinking...")

                col = self.ai.choose_column(self.board)

                # No valid move available
                if col is None:
                    self.board.print()
                    print("AI has no available moves.")
                    print("Draw.")
                    return

            # Drop the token
            row = self.board.drop(col, self.turn)

            # Column is unavailable
            if row is None:

                if self.turn == "X":
                    print("Column unavailable. Choose another column.\n")
                    continue

                else:
                    print("AI selected an unavailable column.")
                    print("Game ended.")
                    return

            # Check for winner
            if self.board.winner(self.turn):

                self.board.print()

                if self.turn == "X":
                    print("You win!")
                else:
                    print("AI wins!")

                return

            # Check for draw
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            # Change turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"