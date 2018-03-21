import pygame
import math
import light

class test_sp():
	def __init__(self,x,y):
		self.rect=pygame.Rect(0,0,1,1)
		self.rect.centerx=x
		self.rect.centery=y

def draw_background(screen):
	screen.fill((225,225,225))
	for i in range(0,500,10):
		for j in range(0,500,10):
			pygame.draw.line(screen,(100,100,100),[i,0],[i,500])
			pygame.draw.line(screen,(100,100,100),[0,j],[500,j])
			
def ins_coll(test,ins):	
	for i in ins:
		coll=test.rect.collidelist(i.rect_list)	
		if coll > -1:	
			if i.blka == i.rect_list[coll] or i.blkb == i.rect_list[coll]:
				test.stop=1
			return [i]
	return []

def inter(test,ins):
	n=0
	while test.screen.get_rect().colliderect(test.rect):
		test.update(2)
		coll=ins_coll(test,ins)
		if test.stop==1:
			test.update(-2)
			pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
			return
		if len(coll) > 0:
			new_test=coll[0].inter(test)
			if len(new_test) > 0:
				for i in new_test:
					inter(i,ins)
	pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
									
def draw_ray(source,ins):
	for s in source:
		test=light.light(s.rect.centerx,s.rect.centery,s,s.screen)
		inter(test,ins)

def check_event(event,source,ins):
	if event.type==pygame.MOUSEBUTTONDOWN:
		pos=pygame.mouse.get_pos()
		press=pygame.mouse.get_pressed()
		if press ==(1,0,0):
			for i in source:
				test=i.rect.collidepoint(pos)
				if test ==1:
					i.move=1
					return
			for i in ins:
				test=i.rect.collidepoint(pos)
				if test ==1:
					i.move=1
					return
			
		elif press==(0,0,1):		
			for i in source:
				test=i.rect.inflate(70,70).collidepoint(pos)
				if test ==1:
					i.rotate=1
					return
			for i in ins:
				test=i.rect.inflate(70,70).collidepoint(pos)
				if test ==1:
					i.rotate=1
					return	
			
	elif event.type==pygame.MOUSEBUTTONUP:
		for s in source:
			s.move=0
			s.rotate=0
		for s in ins:
			s.move=0
			s.rotate=0

def state_update(source,ins,screen):
	for s in source:
		s.update()
	for s in ins:
		s.update()

def screen_update(source,ins,screen):
	draw_background(screen)
	for s in source:
		s.blitme()
	for s in ins:
		s.blitme()
	draw_ray(source,ins)

