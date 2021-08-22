import pygame, sys, time, random
import data.engine as e
from pygame.locals import *


SIZE = 32
WINDOW_SIZE = (640,480)

class Apple:
	def __init__(self,screen):
		self.screen = screen
		self.apple = pygame.image.load('data/images/apple.png').convert()
		self.apple = pygame.transform.scale(self.apple, (32,32))
		self.x = random.randint(0,20)*SIZE
		self.y = random.randint(0,15)*SIZE

	def draw(self):
		self.screen.blit(self.apple, (self.x, self.y))
		pygame.display.update()

class Box:
	def __init__(self, screen, length):
		self.length = length
		self.screen = screen
		self.box = pygame.image.load('data/images/block.png').convert()
		self.box = pygame.transform.scale(self.box, (32,32))

		self.x = [SIZE]*self.length
		self.y = [SIZE]*self.length

		self.direction = 'none'

	def draw(self):
		self.screen.fill((143, 163, 54))
		for i in range(self.length):
			self.screen.blit(self.box, (self.x[i], self.y[i]))
		pygame.display.update()

	def move_up(self):
		self.direction = 'up'		

	def move_down(self):
		self.direction = 'down'

	def move_left(self):
		self.direction = 'left'
	
	def move_right(self):
		self.direction = 'right'	

	def increase_length(self):
		self.length += 1
		self.x.append(-1)
		self.y.append(-1)

	def run(self):
		for i in range(self.length-1,0,-1):
			self.x[i] = self.x[i-1]
			self.y[i] = self.y[i-1]

		if self.direction == 'up':
			self.y[0] -= SIZE
			self.draw()
		
		if self.direction == 'down':
			self.y[0] += SIZE
			self.draw()
		
		if self.direction == 'left':
			self.x[0] -= SIZE
			self.draw()

		if self.direction == 'right':
			self.x[0] += SIZE
			self.draw()

class Game:
	def __init__(self):
		pygame.init()

		self.window = pygame.display.set_mode(WINDOW_SIZE)
		self.box = Box(self.window, 2)
		self.box.draw()
		self.apple = Apple(self.window)
		self.apple.draw()
		self.points = 0
	
	def display_score(self):
		font = pygame.font.Font('data/font/Roboto-Light.ttf', 50)
		score = font.render(str(self.points), True, (255, 250, 255))
		self.window.blit(score, (300,15))
		pygame.display.flip()

	def play(self):
		self.box.run()
		self.apple.draw()
		self.display_score()
				
		if e.apple_collision(self):
			self.apple.x = random.randint(0,18)*SIZE
			self.apple.y = random.randint(0,12)*SIZE
			self.box.increase_length()
			self.points += 1


		if e.wall_collision(self,WINDOW_SIZE):
			sys.exit()

	def run(self):
		run = True

		while run:
			for event in pygame.event.get():
				self.box.draw()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						run = False
					if event.key == K_UP:
						self.box.move_up()
						
					if event.key == K_DOWN:
						self.box.move_down()
						
					if event.key == K_LEFT:
						self.box.move_left()
						
					if event.key == K_RIGHT:
						self.box.move_right()
						
				elif event.type == QUIT:
					run = False

			self.play()
			time.sleep(0.15)
			


if __name__ == "__main__":

	game = Game()

	game.run()
	
	