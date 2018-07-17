from pygame import *
from random import randint as r
size=(800,600)
screen = display.set_mode(size) 
score = 0                
running = True
rect = Rect(400,300,25,25)
key.set_repeat(10,10)
enemies = []
font.init()
timesNewRomanFont = font.SysFont("Times New Roman", 24)
myClock = time.Clock()
def create_enemies(amount):
	global enemies
	enemies = []
	for i in range(amount):
		enemies.append(Rect(r(0, 800 - 25), r(0, 10), 25, 25))
def checkOutOfBounds(enemies):
	counter = 0
	for i in enemies:
		if i.y > 600:
			counter += 1
	return counter
def checkHit(rect, enemies):
	for i in enemies:
		if rect.colliderect(i):
			return True
	return False
create_enemies(10)			
xdiff = []
speed = 3
while running:
	for evt in event.get():  
		if evt.type == QUIT: 
			running = False
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:
				running = False
	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
	kp = key.get_pressed()
	if speed != 5.090909090909091:
		speed = 3 + (score + 1) / 11	 
	if kp[K_UP] and rect.y >= 0:
		rect.y -= speed
	if kp[K_DOWN] and rect.y <= 575:
		rect.y += speed
	if kp[K_LEFT] and rect.x >= 0:
		rect.x -= speed
	if kp[K_RIGHT] and rect.x <= 775:
		rect.x += speed		
	screen.fill(0)
	for i in enemies:
		draw.rect(screen, (255,0,0), i)
	for i in range(len(enemies)):
		if score < 19:
			x = (score + 1) / 10
		enemies[i].y += r(1,2) + x
		try:
			enemies[i].x += xdiff[i]
		except: pass	
	for i in range(len(enemies)):
		if enemies[i].x > 775 or enemies[i].x < 0:
			xdiff[i] = -1 * xdiff[i]
	if checkHit(rect, enemies):
		screen.fill(0)
		screen.blit(timesNewRomanFont.render("Your final score is " + str(score), True, (0,255,0)), (0,0))
		display.flip()
		time.wait(2000)
		running = False		
	if checkOutOfBounds(enemies) == len(enemies):
		create_enemies(int(10 + (score + 1) / 25))
		xdiff = []
		for i in range(len(enemies)):
			xdiff.append(r(-1,1))
		score += 1
	draw.rect(screen, (0,255,0), rect)    
	scoreText = timesNewRomanFont.render("Score: " + str(score), True, (0,255,0))
	screen.blit(scoreText, (0,0))
	myClock.tick(450)
	display.flip() 
quit()