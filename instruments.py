import pygame
import math
import light

class block():
	def __init__(self,x,y,size,clr):
		self.x=x
		self.y=y
		self.clr=clr
		self.rect=pygame.Rect(0,0,size,size)
		self.rect.centerx=x
		self.rect.centery=y

class blocker():
	def __init__(self,x,y,clr,size,screen):
		self.screen=screen
		self.clr=clr
		self.size=size
		self.rect=pygame.Rect(0,0,self.size,self.size)
		self.rect.centerx=x
		self.rect.centery=y
		self.move=0		
		self.ratate=0
		self.fix=0
		self.rect_list=[]
		self.blka=block(self.rect.centerx,self.rect.centery,self.size,self.clr)
		self.rect_list.append(self.blka)
		self.blkb=self.blka
		self.rect_list.append(self.blka)
		
	def update(self):
		if self.move==1 and self.fix==0:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)		
			self.rect_list=[]
			self.blka=block(self.rect.centerx,self.rect.centery,self.size,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=self.blka
			self.rect_list.append(self.blka)
	
	def inter(self,test):
		pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
		test.stop=1
		return []
	
	def blitme(self):
		pygame.draw.rect(self.screen,self.clr,self.rect)
	
class reflector():
	def __init__(self,x,y,angle,clr,size,screen):
		self.screen=screen
		self.clr=clr
		self.size=size
		self.rect=pygame.Rect(0,0,self.size,self.size)
		self.rect.centerx=x
		self.rect.centery=y
		self.move=0
		self.rotate=0		
		self.angle=angle*math.pi/180.
		self.vector=pygame.math.Vector2(math.cos(self.angle),math.sin(self.angle))
		self.vectorl=self.vector.rotate(90.)
		self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
		self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
		self.rect_list=[]
		point=self.pointa[:]
		for i in range(0,self.size):
			self.rect_list.append(block(point[0],point[1],2,self.clr))
			point[0]+=self.vectorl[0]
			point[1]+=self.vectorl[1]
		self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
		self.rect_list.append(self.blka)
		self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
		self.rect_list.append(self.blkb)
			
	def blitme(self):			
		pygame.draw.line(self.screen,self.clr,self.pointa,self.pointb,3)
		pygame.draw.rect(self.screen,self.clr,self.blka)
		pygame.draw.rect(self.screen,self.clr,self.blkb)
		
	def update(self):
		if self.move==1:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
		elif self.rotate==1:
			pos=pygame.mouse.get_pos()
			self.vector[0]=pos[0]-self.rect.centerx
			self.vector[1]=pos[1]-self.rect.centery
			self.vector=self.vector.normalize()
			self.vectorl=self.vector.rotate(90.)
			self.angle=math.acos(self.vector[0])
			if self.vector[1]<0:
				self.angle=2.*math.pi-self.angle
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
#		print(self.rect.center,self.angle*180./math.pi)
	
	def inter(self,test):
		pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
		angle=test.vector.angle_to(self.vector)
		if abs(angle) < 0.5 or abs(angle -180) < 0.5:
			test.stop=1
			return []
		test.sourcex=test.x
		test.sourcey=test.y
		test.vector=test.vector.reflect(self.vector)
		test.update(15)
		return []
		
class spliter():
	def __init__(self,x,y,angle,clr,size,screen):
		self.screen=screen
		self.clr=clr
		self.size=size
		self.rect=pygame.Rect(0,0,self.size,self.size)
		self.rect.centerx=x
		self.rect.centery=y
		self.move=0
		self.rotate=0		
		self.angle=angle*math.pi/180.
		self.vector=pygame.math.Vector2(math.cos(self.angle),math.sin(self.angle))
		self.vectorl=self.vector.rotate(90.)
		self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
		self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
		self.rect_list=[]
		point=self.pointa[:]
		for i in range(0,self.size):
			self.rect_list.append(block(point[0],point[1],2,self.clr))
			point[0]+=self.vectorl[0]
			point[1]+=self.vectorl[1]
		self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
		self.rect_list.append(self.blka)
		self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
		self.rect_list.append(self.blkb)
			
	def blitme(self):			
		pygame.draw.line(self.screen,self.clr,self.pointa,self.pointb,3)
		pygame.draw.rect(self.screen,self.clr,self.blka)
		pygame.draw.rect(self.screen,self.clr,self.blkb)
		
	def update(self):
		if self.move==1:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
		elif self.rotate==1:
			pos=pygame.mouse.get_pos()
			self.vector[0]=pos[0]-self.rect.centerx
			self.vector[1]=pos[1]-self.rect.centery
			self.vector=self.vector.normalize()
			self.vectorl=self.vector.rotate(90.)
			self.angle=math.acos(self.vector[0])
			if self.vector[1]<0:
				self.angle=2.*math.pi-self.angle
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
		
	def inter(self,test):
		new_test=light.light(test.rect.centerx,test.rect.centery,test.source,test.screen)
		new_test.vector=test.vector
		new_test.sourcex=test.x
		new_test.sourcey=test.y
		new_test.update(15)
		pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
		angle=test.vector.angle_to(self.vector)
		if abs(angle) < 0.5 or abs(angle -180) < 0.5:
			test.stop=1
			return [new_test]
		test.sourcex=test.x
		test.sourcey=test.y
		test.vector=test.vector.reflect(self.vector)
		test.update(15)
		return 	[new_test]

class deflector():
	def __init__(self,x,y,angle,clr,size,n,screen):
		self.n=n
		self.screen=screen
		self.clr=clr
		self.size=size
		self.rect=pygame.Rect(0,0,100,100)
		self.rect.centerx=x
		self.rect.centery=y
		self.move=0
		self.rotate=0
		self.fix=0		
		self.angle=angle*math.pi/180.
		self.vector=pygame.math.Vector2(math.cos(self.angle),math.sin(self.angle))
		self.vectorl=self.vector.rotate(90.)
		self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
		self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
		self.rect_list=[]
		point=self.pointa[:]
		for i in range(0,self.size):
			self.rect_list.append(block(point[0],point[1],2,self.clr))
			point[0]+=self.vectorl[0]
			point[1]+=self.vectorl[1]
		self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
		self.rect_list.append(self.blka)
		self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
		self.rect_list.append(self.blkb)
		print(len(self.rect_list))
			
	def blitme(self):			
		pygame.draw.line(self.screen,self.clr,self.pointa,self.pointb,3)
		pygame.draw.rect(self.screen,self.clr,self.blka)
		pygame.draw.rect(self.screen,self.clr,self.blkb)
		
	def update(self):
		if self.move==1 and self.fix==0:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
		elif self.rotate==1:
			pos=pygame.mouse.get_pos()
			self.vector[0]=pos[0]-self.rect.centerx
			self.vector[1]=pos[1]-self.rect.centery
			self.vector=self.vector.normalize()
			self.vectorl=self.vector.rotate(90.)
			self.angle=math.acos(self.vector[0])
			if self.vector[1]<0:
				self.angle=2.*math.pi-self.angle
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
		
	def inter(self,test):
		new_test=light.light(test.rect.centerx,test.rect.centery,test.source,test.screen)
		new_test.vector=test.vector
		new_test.sourcex=test.x
		new_test.sourcey=test.y
		angle1=abs(new_test.vector.angle_to(self.vector))
		if angle1 > 90:
			angle1=180.-angle1
		angle2=math.asin(math.sin(angle1*math.pi/180.)/self.n)*180./math.pi
		new_test.vector=new_test.vector.rotate(angle1-angle2)		
		new_test.update(15)
		pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
		angle=test.vector.angle_to(self.vector)
		if abs(angle) < 0.5 or abs(angle -180) < 0.5:
			test.stop=1
			return [new_test]
		test.sourcex=test.x
		test.sourcey=test.y
		test.vector=test.vector.reflect(self.vector)
		test.update(15)
		return 	[new_test]

class convex(pygame.sprite.Sprite):
	def __init__(self,x,y,angle,clr,size,f,screen):
		self.screen=screen
		self.clr=clr
		self.size=size
		self.rect=pygame.Rect(0,0,self.size,self.size)
		self.rect.centerx=x
		self.rect.centery=y
		self.move=0
		self.rotate=0		
		self.angle=angle*math.pi/180.
		self.vector=pygame.math.Vector2(math.cos(self.angle),math.sin(self.angle))
		self.vectorl=self.vector.rotate(90.)
		self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
		self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
		self.rect_list=[]
		point=self.pointa[:]
		for i in range(0,self.size):
			self.rect_list.append(block(point[0],point[1],2,self.clr))
			point[0]+=self.vectorl[0]
			point[1]+=self.vectorl[1]
		self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
		self.rect_list.append(self.blka)
		self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
		self.rect_list.append(self.blkb)
		self.f=f
			
	def blitme(self):			
		pygame.draw.line(self.screen,self.clr,self.pointa,self.pointb,3)
		pygame.draw.rect(self.screen,self.clr,self.blka)
		pygame.draw.rect(self.screen,self.clr,self.blkb)
		
	def update(self):
		if self.move==1:
			pos=pygame.mouse.get_pos()
			self.rect.centerx=10*round(pos[0]/10.)
			self.rect.centery=10*round(pos[1]/10.)
			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
			self.rect_list=[]
			point=self.pointa[:]
			for i in range(0,self.size):
				self.rect_list.append(block(point[0],point[1],2,self.clr))
				point[0]+=self.vectorl[0]
				point[1]+=self.vectorl[1]
			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
			self.rect_list.append(self.blka)
			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
			self.rect_list.append(self.blkb)
#		elif self.rotate==1:
#			pos=pygame.mouse.get_pos()
#			self.vector[0]=pos[0]-self.rect.centerx
#			self.vector[1]=pos[1]-self.rect.centery
#			self.vector=self.vector.normalize()
#			self.vectorl=self.vector.rotate(90.)
#			self.angle=math.acos(self.vector[0])
#			if self.vector[1]<0:
#				self.angle=2.*math.pi-self.angle
#			self.pointa=[round(self.rect.centerx-0.5*self.size*self.vectorl[0]),round(self.rect.centery-0.5*self.size*self.vectorl[1])]
#			self.pointb=[round(self.rect.centerx+0.5*self.size*self.vectorl[0]),round(self.rect.centery+0.5*self.size*self.vectorl[1])]		
#			self.rect_list=[]
#			point=self.pointa[:]
#			for i in range(0,self.size):
#				self.rect_list.append(block(point[0],point[1],2,self.clr))
#				point[0]+=self.vectorl[0]
#				point[1]+=self.vectorl[1]
#			self.blka=block(self.pointa[0],self.pointa[1],5,self.clr)
#			self.rect_list.append(self.blka)
#			self.blkb=block(self.pointb[0],self.pointb[1],5,self.clr)
#			self.rect_list.append(self.blkb)
#		print(self.rect.center,self.angle*180./math.pi)
	
	def inter(self,test):
		pygame.draw.line(test.screen,test.clr,[test.sourcex,test.sourcey],[test.x,test.y],3)
		angle=test.vector.angle_to(self.vector)
		if abs(angle) < 0.5 or abs(angle -180) < 0.5:
			f=[self.rect.centerx+self.vector[0]*self.f,self.rect.centery]
			test.vector=pygame.math.Vector2(f[0]-test.x,f[1]-test.y)
			test.vector=test.vector.normalize()
			if self.f < 0:
				test.vector=-test.vector
		elif abs(test.x-self.rect.centerx) < 2 and abs(test.y-self.rect.centery) < 2:
			pass
		else:
			f=self.f
			a=test.vector[0]
			b=test.vector[1]
			c=test.y-self.rect.centery
			test.vector=pygame.math.Vector2(f*a,f*b-a*c)
			test.vector=test.vector.normalize()
			if self.f < 0:
				test.vector=-test.vector
			
		test.sourcex=test.x
		test.sourcey=test.y
#		test.vector=test.vector.reflect(self.vector)
		test.update(15)
		return []
