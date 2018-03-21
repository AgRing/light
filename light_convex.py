

import pygame
import light
import gamefunctions as gf
import instruments as inst

pygame.init()


def run_game():
	screen = pygame.display.set_mode((500,500))
	pygame.display.set_caption("My Game")
	clock = pygame.time.Clock()
	done = False	
	
	source=[]
	ins=[]
	source.append(light.source(20,170,0,(255,0,0),screen))
	source.append(light.source(20,170,15,(225,0,0),screen))
	source.append(light.source(20,170,30,(225,0,0),screen))
	source.append(light.source(20,200,-15,(0,225,0),screen))
	source.append(light.source(20,200,0,(0,255,0),screen))
	source.append(light.source(20,200,15,(0,255,0),screen))
	source.append(light.source(20,230,-30,(0,0,225),screen))
	source.append(light.source(20,230,-15,(0,0,255),screen))
	source.append(light.source(20,230,0,(0,0,255),screen))
	

	ins.append(inst.convex(180,200,0,(0,0,225),150,70,screen))
	ins.append(inst.convex(180,400,0,(0,0,225),150,-70,screen))		
#	ins.append(inst.spliter(290,240,0,(0,100,100),25,screen))		
#	ins.append(inst.deflector(290,260,0,(0,0,200),25,1.7,screen))	
		
	while not done:

		event=pygame.event.wait()
		if event.type == pygame.QUIT:
			done = True
			continue
		
		gf.check_event(event,source,ins)
		gf.state_update(source,ins,screen)
		gf.screen_update(source,ins,screen)
		pygame.display.flip()
		clock.tick(60)
#		print(clock.get_fps())
	
# Close the window and quit.
	pygame.quit()

run_game()
