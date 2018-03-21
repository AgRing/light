

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
	source.append(light.source(40,140,90,(0,0,200),screen))
	source.append(light.source(360,140,0,(0,0,200),screen))
	source.append(light.source(360,360,0,(0,0,200),screen))
	
	ins.append(inst.blocker(200,250,(100,100,200),10,screen))
	ins.append(inst.blocker(420,140,(100,100,200),10,screen))
	ins.append(inst.blocker(420,360,(100,100,200),10,screen))
	ins.append(inst.blocker(390,370,(100,100,200),10,screen))
	ins.append(inst.reflector(40,320,342,(30,150,255),25,screen))
	ins.append(inst.reflector(70,360,297,(30,150,255),25,screen))
	ins.append(inst.reflector(180,320,-342,(30,150,255),25,screen))
	ins.append(inst.reflector(150,360,-297,(30,150,255),25,screen))
	ins.append(inst.reflector(180,140,45,(30,150,255),25,screen))
	ins.append(inst.spliter(210,140,135,(0,100,100),25,screen))
	ins.append(inst.reflector(290,140,290,(30,150,255),25,screen))
	ins.append(inst.reflector(330,170,155,(30,150,255),25,screen))
	ins.append(inst.reflector(330,210,-155,(30,150,255),25,screen))
	ins.append(inst.reflector(280,250,-290,(30,150,255),25,screen))
	ins.append(inst.reflector(280,360,-290,(30,150,255),25,screen))
	ins.append(inst.reflector(330,320,-155,(30,150,255),25,screen))
	ins.append(inst.reflector(330,270,155,(30,150,255),25,screen))
	ins.append(inst.reflector(210,360,135,(30,150,255),25,screen))	
	ins.append(inst.spliter(390,140,-45,(0,100,100),25,screen))
	

#	ins.append(inst.convex(350,100,0,(0,0,225),50,50,screen))	
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
