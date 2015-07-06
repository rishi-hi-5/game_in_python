import pygame,sys,random    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up

BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=50

keys={"player_up":False,"welcome":False,"playerdash":False,"continue":False}


player_x=224
score_ref=player_x
player_y=500

change_up=10
change_down=5

def playerHasHitPipe(playerRect, pipe):
	for p in pipe:
		if playerRect.colliderect(p):
			return True
		#if playerRect.colliderect(p['rect2']):
			#return True 
	return False




pygame.init()
#set clock screen and its caption
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1366,768))
pygame.display.set_caption('swat kat')
rect_image=pygame.image.load('blackbar.png')

player=pygame.image.load("Fighter.png")
playerrect=player.get_rect()
playerrect.width=playerrect.width-50
playerrect.height=playerrect.height-10

rect_list=[]
rect_list1=[]

rect1=[]
rect2=[]


#screen.fill((0,255,255))
start=500
max=60


#For Upward
k=0
x=0
while k<100:
	x1=random.randrange(300,600)
	height=random.randrange(200,250)
	rect_list.append([(x,100),(x+x1,100),(x+(x1)/2,height,)])
	x=x+x1
	k+=1



##DOWN
##For Upward
k=0
x=0
while k<100:
	x1=random.randrange(300,600)
	height=random.randrange(768-325,768-250)
	rect_list1.append([(x+(x1)/2,height),(x,768-100),(x+x1,768-100)])
	x=x+x1
	k+=1

#i=0
#j=700
#k=0
##screen.fill((0,255,255))
#start=500
#max=60
#while k<500:	
	#if(i<max/2):
		#j=j+4
		#i+=1
		#start+=5
		#rect_list.append([start,0,10,j])
		
	#elif (i<max):
		#j=j-4
		#i+=1
		#start+=5
		#rect_list.append([start,0,10,j])
		
	#if(i==max):
		#max=random.randrange(20,150)
		#i=0
		#j=75
		
	#k=k+1




#for Downward 
#i=0
#j=700
#k=0
##screen.fill((0,255,255))
#start=500
#max=60


#while k<500:	
	#if(i<max/2):
		#j=j-4
		#i+=1
		#start+=5
		#rect_list1.append([start,j,10,768])
		
	#elif (i<max):
		#j=j+4
		#i+=1
		#start+=5
		#rect_list1.append([start,j,10,768])
		
	#if(i==max):
		#max=random.randrange(20,150)
		#i=0
		#j=700
		
	#k=k+1










while True:
	screen.fill(WHITE)
	pygame.draw.rect(screen,BLACK,(0,0,1366,100))
	pygame.draw.rect(screen,BLACK,(0,768-100,1366,100))
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
		if(event.type==pygame.KEYDOWN):
			if event.key==K_ESCAPE:
			    pygame.quit()
			    sys.exit()
			    
			elif event.key==K_UP:
			    keys["player_up"]=True
			    
			elif event.key==K_SPACE:
			    keys["playerdash"]=True
	    
			
			    
		elif(event.type==pygame.KEYUP):
			    
			if event.key==K_UP:
			    keys["player_up"]=False 
			    
			elif event.key==K_SPACE:
			    keys["playerdash"]=False            
				
			
			
	    
	if keys["player_up"]:
		player_y-=change_up
	else:
		player_y+=change_down    
		
		
		
#show list


	for r in rect_list:
		rect=pygame.draw.polygon(screen,BLACK,r)
		rect1.append(rect)
		
	for r in rect_list1:
		rect=pygame.draw.polygon(screen,BLACK,r)
		rect2.append(rect)
		
	for r in rect1:
		r.move_ip(-1*10,0)
		
	#for r in rect[:]:
		#if r.left<0:
			#rect_list.remove(r)

	#for r in rect_list:
			#y=pygame.transform.scale(rect_image,(r.width,r.height))
			#screen.blit(y,r)
			

#show list1			
	for r in rect2:
			r.move_ip(-1*10,0)
		
	#for r in rect_list1[:]:
			#if r.left<0:
				#rect_list1.remove(r)

	#for r in rect_list1:
			#y=pygame.transform.scale(rect_image,(r.width,r.height))
			#screen.blit(y,r)
			
			
			
			
			
			
			
			
			
	playerrect.topleft=(player_x,player_y)
	screen.blit(player,playerrect)
	#if playerHasHitPipe(playerrect,rect_list) or playerHasHitPipe(playerrect,rect_list1):
	#	break
	
	pygame.display.flip()
	clock.tick(FPS)
	
