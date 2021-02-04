import pygame, sys
from math import inf

def draw_grid():
    pygame.draw.line(screen, (23,145,135), (0,200-line_width), (screen_width,200-line_width),line_width)
    pygame.draw.line(screen, (23,145,135), (0,400-line_width), (screen_width,400-line_width),line_width)
    pygame.draw.line(screen, (23,145,135), (200-line_width,0), (200-line_width, screen_height),line_width)
    pygame.draw.line(screen, (23,145,135), (400-line_width,0), (400-line_width, screen_height),line_width)

def draw_board(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                ai_text = font.render('x', True, (66,66,66))
                screen.blit(ai_text, (col*200 + 55,row*200 + 55))
            elif board[row][col] == 'O':
                human_text = font.render('o', True, (66,66,66))
                screen.blit(human_text, (col*200 + 55,row*200 + 55))

def check_winner(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-":
            return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "-":
            return board[2][0]
    for row in board:
        for cell in row:
            if cell == "-":
                return None
    return "tie"

def minimax(board, max_turn):
    winner = check_winner(board)
    if winner != None:
        return points[winner]
    if max_turn:
        score = -inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    curr_score = minimax(board,False)
                    board[i][j] = "-"
                    score = max(score, curr_score)
        return score
    else:
        score =  inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    curr_score = minimax(board,True)
                    board[i][j] = "-"
                    score = min(score, curr_score)
        return score

def computer_move(board):
    score = -inf
    x = -1
    y = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                board[i][j] = "X"
                curr_score = minimax(board,False)
                board[i][j] = "-"
                if curr_score > score:
                    score = curr_score
                    x = i
                    y = j
    board[x][y] = "X"


pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption(('Tic Tac Toe'))

line_width = 15
font = pygame.font.SysFont("monospace",90)
board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]]
points = {
    "X": 1,
    "tie": 0,
    "O": -1
}

computer_move(board)
while (True):
    screen.fill((28,170,156))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and check_winner(board)==None:
            mouseX = event.pos[1]
            mouseY = event.pos[0]
            clicked_row = int(mouseX // 200)
            clicked_col = int(mouseY // 200)
            if board[clicked_row][clicked_col] == '-':
                board[clicked_row][clicked_col] = 'O'
                computer_move(board)
    draw_grid()
    draw_board(board)
    pygame.display.flip()
    clock.tick(60)
