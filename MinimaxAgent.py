from Agent import Agent
import math

class MinimaxAgent(Agent):
    INF = float('inf')
    
    def __init__(self, grid):
        self.grid = grid.board
        self.n = int(math.sqrt(grid.size))
        self.symbol = ['o', 'x']
        self.dp = {}
        self.player = True

    def checkMove(self, real_board):
        self.grid = real_board.board
        self.bestMove(real_board)
    
    def mark(self, player, x, y):
        self.grid[x * self.n + y] = self.symbol[player]

    def unmark(self, x, y):
        self.grid[x * self.n + y] = ' '

    def game_over(self):
        return all(cell != ' ' for cell in self.grid)

    def valid_point(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def winner(self, player, x, y):
        symbol = self.symbol[player]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            for shift in range(-2, 1):
                if all(self.valid_point(x + dx * (shift + i), y + dy * (shift + i)) and
                       self.grid[(x + dx * (shift + i)) * self.n + (y + dy * (shift + i))] == symbol
                       for i in range(3)):
                    return True
        return False

    def get_state(self):
        return ''.join(self.grid)

    def minimax(self, player, alpha, beta, depth):
        if self.game_over():
            return depth * (-1 if player == self.player else 1)
        
        state = self.get_state()
        if state in self.dp:
            return self.dp[state]
        
        best_score = -self.INF if player == self.player else self.INF
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i * self.n + j] == ' ':
                    self.mark(player, i, j)
                    if self.winner(player, i, j):
                        score = self.n ** 2 + 1 if player == self.player else -(self.n ** 2 + 1)
                    else:
                        score = self.minimax(not player, alpha, beta, depth + 1)
                    self.unmark(i, j)
                    
                    if player == self.player:
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                    else:
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                    
                    if beta <= alpha:
                        self.dp[state] = best_score
                        return best_score
        
        self.dp[state] = best_score
        return best_score

    def bestMove(self, real_board):
        best_score = -self.INF
        best_move = (0, 0)
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i * self.n + j] == ' ':
                    self.mark(self.player, i, j)
                    if self.winner(self.player, i, j):
                        self.unmark(i, j)
                        return (i, j)
                    
                    self.dp.clear()
                    score = self.minimax(not self.player, -self.INF, self.INF, 0)
                    self.unmark(i, j)
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        move_index = best_move[0] * self.n + best_move[1]
        if real_board.board[move_index] == ' ':
            real_board.squares[move_index].clicked(
                real_board.squares[move_index].x, real_board.squares[move_index].y,
                'x', real_board, real_board.x_asset
            )
