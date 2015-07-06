import pygame,sys,random    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up

BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)

list1=[]
keys={"player_up":False,"welcome":False,"playerdash":False,"continue":False}




pygame.init()
#set clock screen and its caption
clock = pygame.time.Clock()
screen=pygame.display.set_mode([1366,768])
pygame.display.set_caption('swat kat')
back=pygame.image.load("heli1_a.png")
player=pygame.image.load("Fighter.png")
playerrect=player.get_rect()
backrect=back.get_rect()

player_x=224
score_ref=player_x
player_y=700

change_up=6
change_down=3

back_x=0
back_width=back.get_width()
back_x1=back_width
back_x2=back_width*2
back_y=-50
change_back=4

while(True):
    screen.fill(WHITE)
    screen.blit(back,(back_x,back_y))
    screen.blit(back,(back_x1,back_y))
    screen.blit(back,(back_x2,back_y))
    back_x-=change_back
    back_x1-=change_back
    back_x2-=change_back
    
    if back_x1==0:
	back_x=2*back_width
    elif back_x2==0:
	back_x1=2*back_width
    elif back_x==0:
	back_x2=2*back_width

	
	#screen.fill(YELLOW)
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
	    
    if playerrect.colliderect(backrect):
	break
    
#    player.topleft=(player_x,player_y)
    screen.blit(player,playerrect)
    pygame.display.update()
    
    clock.tick(50)
	
pygame.quit()