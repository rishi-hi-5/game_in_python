import pygame,sys,random,time    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
BROWN=(150,50,0)
FPS=60



class func:
	rect_x=0
	rect_x1=400+150
	rect_x2=rect_x1+400+150
	rect_x3=rect_x2+400+150
	rect_x4=rect_x3+400+150


	rect1_x=0
	rect1_x1=400+150
	rect1_x2=rect_x1+400+150
	rect1_x3=rect_x2+400+150
	rect1_x4=rect_x3+400+150

	rect_wid=400
	rect_wid1=400
	rect_wid2=400
	rect_wid3=400
	rect_wid4=400

	rect1_wid=400
	rect1_wid1=400
	rect1_wid2=400
	rect1_wid3=400
	rect1_wid4=400
	def fun(x):

		pygame.draw.rect(screen,BLACK,[func.rect_x,func.rect_y,func.rect_wid,30])

		pygame.draw.rect(screen,BLACK,[func.rect_x1,func.rect_y,func.rect_wid1,30])

		pygame.draw.rect(screen,BLACK,[func.rect_x2,func.rect_y,func.rect_wid2,30])

		pygame.draw.rect(screen,BLACK,[func.rect_x3,func.rect_y,func.rect_wid3,30])

		pygame.draw.rect(screen,BLACK,[func.rect_x4,func.rect_y,func.rect_wid4,30])

		func.rect_x-=5
		func.rect_x1-=5
		func.rect_x2-=5
		func.rect_x3-=5
		func.rect_x4-=5

		if func.rect_x1<=-400:
			func.rect_x=func.rect_x4+func.rect_wid4+150
			func.rect_wid=random.randrange(300,400)

		if func.rect_x2<=-400:
			func.rect_x1=func.rect_x+func.rect_wid+150
			func.rect_wid1=random.randrange(300,400)

		if func.rect_x3<=-400:
			func.rect_x2=func.rect_x1+func.rect_wid1+150
			func.rect_wid2=random.randrange(300,400)

		if func.rect_x4<=-400:
			func.rect_x3=func.rect_x2+func.rect_wid2+150
			func.rect_wid3=random.randrange(300,400)

		if func.rect_x<=-400:
			func.rect_x4=func.rect_x3+func.rect_wid3+150
			func.rect_wid4=random.randrange(300,400)



		#level2
		pygame.draw.rect(screen,BLACK,[func.rect1_x,func.rect_y1,func.rect1_wid,30])

		pygame.draw.rect(screen,BLACK,[func.rect1_x1,func.rect_y1,func.rect1_wid1,30])

		pygame.draw.rect(screen,BLACK,[func.rect1_x2,func.rect_y1,func.rect1_wid2,30])

		pygame.draw.rect(screen,BLACK,[func.rect1_x3,func.rect_y1,func.rect1_wid3,30])

		pygame.draw.rect(screen,BLACK,[func.rect1_x4,func.rect_y1,func.rect1_wid4,30])


		func.rect1_x-=6
		func.rect1_x1-=6
		func.rect1_x2-=6
		func.rect1_x3-=6
		func.rect1_x4-=6

		if func.rect1_x1<=-400:
			func.rect1_x=func.rect1_x4+func.rect1_wid4+150
			func.rect1_wid=random.randrange(300,400)

		if func.rect1_x2<=-400:
			func.rect1_x1=func.rect1_x+func.rect1_wid+150
			func.rect1_wid1=random.randrange(300,400)

		if func.rect1_x3<=-400:
			func.rect1_x2=func.rect1_x1+func.rect1_wid1+150
			func.rect1_wid2=random.randrange(300,400)

		if func.rect1_x4<=-400:
			func.rect1_x3=func.rect1_x2+func.rect1_wid2+150
			func.rect1_wid3=random.randrange(300,400)

		if func.rect1_x<=-400:
			func.rect1_x4=func.rect1_x3+func.rect1_wid3+150
			func.rect1_wid4=random.randrange(300,400)





pygame.init()
#set clock screen and its caption
func.rect_size=100
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1366,768))

func.rect_y=150
func.rect_y1=400

func.rect_x=0
func.rect_x1=400+150
func.rect_x2=func.rect_x1+400+150
func.rect_x3=func.rect_x2+400+150
func.rect_x4=func.rect_x3+400+150


func.rect1_x=0
func.rect1_x1=400+150
func.rect1_x2=func.rect_x1+400+150
func.rect1_x3=func.rect_x2+400+150
func.rect1_x4=func.rect_x3+400+150

func.rect_wid=400
func.rect_wid1=400
func.rect_wid2=400
func.rect_wid3=400
func.rect_wid4=400

func.rect1_wid=400
func.rect1_wid1=400
func.rect1_wid2=400
func.rect1_wid3=400
func.rect1_wid4=400









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
player_up=player_down=player_left=False
player_right=True
i=0
k=0
f=func()





const=1366
while(True):

	screen.fill(WHITE)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

	if event.type==KEYDOWN:
		#if event.key==K_RIGHT:
			#player_right=True
		if event.key==K_UP:
			player_up=True
			#i=5
			
	if event.type==KEYUP:
		#if event.key==K_RIGHT:
			#player_right=False
			#i=0
		if event.key==K_UP:
			player_up=False
			#i=0
	
		if event.key==K_ESCAPE:
			pygame.quit()
			sys.exit()



#level1
#









	f.fun()



	#player_right== True: #and i<=3:
	#player.move_ip(1*8,0)
		
	if player_up==True:
		for j in range(4,6):
			player.move_ip(0,-1*70)
			screen.fill(WHITE)
			f.fun()
			screen.blit(swat[j],player)
			pygame.display.update()
			clock.tick(15)
	
		for j in range(6,8):
			player.move_ip(0,22)
			print j
			screen.fill(WHITE)
			f.fun()
			screen.blit(swat[j],player)
			pygame.display.update()
			clock.tick(15)
		#i=0
		
	
	#screen.fill(BLACK)
	if(k==1):
		screen.blit(swat[i], player)
		i+=1
		k=0
		pygame.display.update()
	else:
		k+=1
		screen.blit(swat[i], player)

	if i==3:
		#player.move_ip(-1*2,0)
		i=0
		print i
	

	pygame.display.update()
	clock.tick(40)
