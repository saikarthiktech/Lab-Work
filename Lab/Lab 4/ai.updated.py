import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        # Get all legal columns
        legal = [
            c for c in range(7)
            if board.grid[0][c] == "."
        ]

        # No moves available
        if not legal:
            return None

        # -------------------------------------------------
        # 1. Check if AI can win immediately
        # -------------------------------------------------
        for col in legal:
            test_board = self.copy_board(board)

            if test_board.drop(col, me) is not None:
                if test_board.winner(me):
                    return col

        # -------------------------------------------------
        # 2. Check if opponent can win next move
        #    If yes, block that column
        # -------------------------------------------------
        for col in legal:
            test_board = self.copy_board(board)

            if test_board.drop(col, opponent) is not None:
                if test_board.winner(opponent):
                    return col

        # -------------------------------------------------
        # 3. Prefer the center column
        # -------------------------------------------------
        preferred_columns = [3, 2, 4, 1, 5, 0, 6]

        for col in preferred_columns:
            if col in legal:
                return col

        # -------------------------------------------------
        # 4. Fallback: choose a random legal column
        # -------------------------------------------------
        return random.choice(legal)

    def copy_board(self, board):
        """
        Create a copy of the current board.
        This allows the AI to test moves without
        changing the real game board.
        """

        new_board = type(board)()

        new_board.grid = [
            row.copy()
            for row in board.grid
        ]

        return new_board