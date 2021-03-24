import pygame
import random

#https://docs.repl.it/tutorials/07-building-a-game-with-pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

class Ball:
  def __init__(self):
    #add self.rect = CLEAR
    self.image = pygame.image.load("small_tennis.png")
    self.speed = [random.uniform(-4,4), 2]
    self.rect = self.image.get_rect()
    self.alive = True

  def update(self):
    if self.rect.top < 0:
      self.speed[1] = -self.speed[1]
      self.speed[0] = random.uniform(-4, 4)
      if self.alive == True:
        self.image = pygame.image.load("small_tennis.png")
    elif self.rect.left < 0 or self.rect.right > 800:
      self.speed[0] = -self.speed[0]
      if self.alive == True:
        self.image = pygame.image.load("small_tennis.png")
    elif self.rect.bottom > HEIGHT:
      self.speed[1] = -2
      self.speed[0] = random.uniform(-4, 4)
      self.image = pygame.image.load("small_tennis_red.png")
      self.alive = False
    self.move()
  
  def move(self):
    self.rect = self.rect.move(self.speed)


def main():
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  #Initialize a window or screen for display
  clock = pygame.time.Clock()
  #create an object to help track time

  ball1 = Ball()
  ball2 = Ball()
  ball3 = Ball()

  balls = [ball1, ball2, ball3]
  num_successful_throws = 0
  numberOfBall = 3
  numberOfBallNotAlive = 0

  while True:

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        for ball in balls:
          if ball.rect.collidepoint(pygame.mouse.get_pos()) and ball.alive:
                                  #get the mouse cursor position
            ball.speed[0] = random.uniform(-4, 4)
            ball.speed[1] = -2
            num_successful_throws += 1
            ball.image = pygame.image.load("small_tennis_green.png")
            break

    # for i, ball in enumerate(balls):
    #   if ball.rect.bottom > 600:
    #     numberOfBallNotAlive += 1
    #     break

    if num_successful_throws >= 3:
        ball = Ball()
        balls.append(ball)
        num_successful_throws = 0
        numberOfBall += 1
    
    screen.fill(BACKGROUND)

    for i, ball in enumerate(balls):
          screen.blit(ball.image, ball.rect)
          ball.update()

    # while numberOfBall == numberOfBallNotAlive:
    #   ball.clear = 1

    pygame.display.flip()
    #Update the full display Surface to the screen
    clock.tick(60)
    #framerate definition

if __name__ == "__main__":
  main()