import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

# define varibles
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

# define colors:
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# define font:
font = pygame.font.SysFont(None, 40)

# create rectangle:
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

def draw_grid():
    bg_color = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)
def create_markers(markers):
    for x in range(3):
        row = [0] * 3
        markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                # draw the crosses
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            elif y == -1:
                pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 40, line_width)
            y_pos += 1
        x_pos += 1

def check_winner():

    global winner
    global game_over

    y_pos = 0
    occupied_counter = 0
    for x in markers:
        # check rows:
        if sum(x) == 3:
            winner = 1
            game_over = True
        elif sum(x) == -3:
            winner = 2
            game_over = True
        # check columns:
        elif markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        elif markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    # check diagonals:
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
    else:
        for x in markers:
            if 0 not in x:
                occupied_counter += 1
        if occupied_counter == 3:
            winner = 3
            game_over = True


def draw_winner(winner):
    if winner == 1 or winner == 2:
        win_text = "Player " + str(winner) + " wins!"
        win_image = font.render(win_text, 1, blue)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
        screen.blit(win_image, (screen_width // 2 - 100, screen_height // 2 - 50))
    else:
        tie_text = "Tie!"
        tie_image = font.render(tie_text, 1, blue)
        pygame.draw.rect(screen, green, (screen_width // 2 - 20, screen_height // 2 - 60, 50, 50))
        screen.blit(tie_image, (screen_width // 2 - 20, screen_height // 2 - 50))

    again_text = "Play again?"
    again_image = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_image, (screen_width // 2 - 80, screen_height // 2 + 10))

run = True
create_markers(markers)
while run:
    draw_grid()
    draw_markers()
    # add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        draw_winner(winner)
        
        # check for mouse click to see if user has decided to play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                markers = []
                create_markers(markers)
                pos = []
                player = 1
                winner = 0
                game_over = False

    pygame.display.update()

pygame.quit()