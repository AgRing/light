import pygame
import math

class source():
	def __init__(self,x,y,angle,clr,screen):
		self.rect=pygame.Rect(0,0,10,10)
		self.rect.centerx=x
		self.rect.centery=y
		self.angle=angle*math.pi/180.
		self.vector=pygame.math.Vector2(math.cos(self.angle),math.sin(self.angle))
		self.clr=clr
		self.screen=screen
		self.move=0
		self.rotate=0
		self.fixed=0
		
	def update(self):
		if self.move==1 and self.fixed==0:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)
		elif self.rotate==1:
			pos=pygame.mouse.get_pos()
			self.vector[0]=pos[0]-self.rect.centerx
			self.vector[1]=pos[1]-self.rect.centery
			self.vector=self.vector.normalize()
			self.angle=math.acos(self.vector[0])
			if self.vector[1]<0:
				self.angle=2.*math.pi-self.angle
	def blitme(self):
		pygame.draw.circle(self.screen,self.clr,[self.rect.centerx,self.rect.centery],5)


class light():
	def __init__(self,x,y,source,screen):
		self.x=x
		self.y=y
		self.source=source
		self.sourcex=source.rect.centerx
		self.sourcey=source.rect.centery
		self.clr=source.clr
		self.vector=source.vector
		self.screen=screen
		self.rect=pygame.Rect(0,0,1,1)
		self.rect.centerx=x
		self.rect.centery=y
		self.stop=0
		
	def update(self,l):
		self.x+=l*self.vector[0]
		self.y+=l*self.vector[1]
		self.rect.centerx=self.x
		self.rect.centery=self.y
		

		
