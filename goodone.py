import pygame,sys,random,time
from pygame.locals import*

	
BLACK=(0,0,0)
WHITE=(255,255,255)
WINDOWWIDTH=1366
WINDOWHEIGHT=768
FPS=15
pygame.init()
window=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption('fight')
mainclock=pygame.time.Clock()
swat=[]
swat_run2=pygame.image.load('swat-run4.png')
swat.append(swat_run2)
swat_run3=pygame.image.load('swat-run5.png')
swat.append(swat_run3)
swat_run4=pygame.image.load('swat-run6.png')
swat.append(swat_run4)
swat_run1=pygame.image.load('swat-run3.png')
swat.append(swat_run1)

swat_jump1=pygame.image.load('swat-jump1.png')
swat.append(swat_jump1)
swat_jump2=pygame.image.load('swat-jump2.png')
swat.append(swat_jump2)
swat_jump3=pygame.image.load('swat-jump3.png')
swat.append(swat_jump3)
swat_jump4=pygame.image.load('swat-jump4.png')
swat.append(swat_jump4)

player = pygame.Rect(450,450, 58, 50)
print swat
player_up=player_down=player_left=player_right=False
i=0

while(True):
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	if event.type==KEYDOWN:
		if event.key==K_RIGHT:
			player_right=True
		if event.key==K_UP:
			player_up=True
			i=5
			
	if event.type==KEYUP:
		if event.key==K_RIGHT:
			player_right=False
			i=0
		if event.key==K_UP:
			player_up=False
			i=0
	
		if event.key==K_ESCAPE:
			pygame.quit()
			sys.exit()
	if player_right== True: #and i<=3:
		player.move_ip(1*8,0)
		i+=1	
	if player_up==True:
		for j in range(4,6):
			player.move_ip(0,-1*45)
			window.fill(BLACK)
			window.blit(swat[j],player)
			pygame.display.update()
			time.sleep(0.2)
		for j in range(6,8):
			player.move_ip(0,15)
			print j
			window.fill(BLACK)
			window.blit(swat[j],player)
			pygame.display.update()
			time.sleep(0.2)
		i=0
		
		
	window.fill(BLACK)
	window.blit(swat[i], player)
	if i==3:
		player.move_ip(-1*2,0)
		i=0
		print i
		
	
	pygame.display.update()	
	mainclock.tick(FPS)
  
  
	
