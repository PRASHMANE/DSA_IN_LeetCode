class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [[0] * 3 for _ in range(2)]
        col = [[0] * 3 for _ in range(2)]
        diag1 = [0] * 2  # main diagonal
        diag2 = [0] * 2  # anti-diagonal
        
        for i, (r, c) in enumerate(moves):
            player = i % 2  # 0 -> A, 1 -> B
            row[player][r] += 1
            col[player][c] += 1
            diag1[player] += (r == c)
            diag2[player] += (r + c == 2)
            
            # Check win condition
            if (row[player][r] == 3 or col[player][c] == 3 or
                diag1[player] == 3 or diag2[player] == 3):
                return "A" if player == 0 else "B"

        # If no winner yet...
        return "Draw" if len(moves) == 9 else "Pending"