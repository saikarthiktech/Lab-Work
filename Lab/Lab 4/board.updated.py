ROWS, COLS = 6, 7


class Board:
    def __init__(self):
        self.grid = [["."] * COLS for _ in range(ROWS)]

    def drop(self, col, token):
        if not 0 <= col < COLS:
            return None

        for r in range(ROWS - 1, -1, -1):
            if self.grid[r][col] == ".":
                self.grid[r][col] = token
                return r

        return None

    def full(self):
        return all(self.grid[0][c] != "." for c in range(COLS))

    def winner(self, token):
        directions = [
            (0, 1),    # Horizontal
            (1, 0),    # Vertical
            (1, 1),    # Diagonal down-right
            (1, -1)    # Diagonal down-left
        ]

        for r in range(ROWS):
            for c in range(COLS):

                if self.grid[r][c] != token:
                    continue

                for dr, dc in directions:
                    count = 0

                    for i in range(4):
                        nr = r + i * dr
                        nc = c + i * dc

                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            break

                        if self.grid[nr][nc] != token:
                            break

                        count += 1

                    if count == 4:
                        return True

        return False

    def print(self):
        print("\n  " + " ".join(str(i + 1) for i in range(COLS)))

        for row in self.grid:
            print("  " + " ".join(row))

        print()