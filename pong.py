import random
import pygame
import sys

# Main menu
# Options will include play (where you can pick difficulty) and quit
def main_menu():
    x = 5
# pong game animation
def ball_animated():
    global ball_speed_x,ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    # Ball will bounce off wall
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        score_tracker()
    # Handles collisions
    if ball.colliderect(player) or ball.colliderect(opp):
        ball_speed_x *= -1
        
# Player movement
def player_animated():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        
# Opponent movement
def opp_animated():
	if opp.top < ball.y:
		opp.y += opp_speed
	if opp.bottom > ball.y:
		opp.y -= opp_speed

	if opp.top <= 0:
		opp.top = 0
	if opp.bottom >= HEIGHT:
		opp.bottom = HEIGHT

def ball_restart():
	global ball_speed_x, ball_speed_y
	ball.center = (WIDTH/2, HEIGHT/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

def score_tracker():
    global opp_score,player_score
  
        
    if ball.left <= 0:
        ball_restart()
        opp_score += 1
    if ball.right >= WIDTH:
        ball_restart()
        player_score += 1
    

    
# general set up
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window with screen width and height
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('Pong Game')

# Game pieces
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 -15, 30,30)
player = pygame.Rect(WIDTH - 20,HEIGHT/2 - 70,10,70)
opp = pygame.Rect(10,HEIGHT/2 - 70,10,70)

# Score
player_score = 0
opp_score = 0
font = pygame.font.Font('freesansbold.ttf',32)
msgFont =  pygame.font.Font('freesansbold.ttf',16)

bg_color = pygame.Color('grey12')
black = pygame.Color('black')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opp_speed = 7

while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Key has been pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed -=7
        # Key has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed +=7    
   
    if player_score == 11 or opp_score == 11: # First to 11 wins
        ball_speed_x=0
        ball_speed_y = 0
        screen.blit(msg, (WIDTH/2 - 33,0))
        
        
    ball_animated()
    player_animated()
    opp_animated()
    score = font.render(str(opp_score) + " : " + str(player_score), True, (225,225,225))
    msg = msgFont.render("Congratulations, you win!", True, (255,255,255))
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opp)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (WIDTH/2,0), (WIDTH/2,HEIGHT))         
    
    screen.blit(score,(WIDTH/2 - 33,0))
    # Updating window
    pygame.display.flip()
    clock.tick(60)
    



# To do:
# display game message when game is over
# ask user to play again at end
# menu to ask difficulty
# ball speed when it returns
