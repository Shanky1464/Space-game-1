import pygame as pg
import time as t
import math as m
from pygame import mixer


pg.init()
#screen
screen=pg.display.set_mode((1600,820))
bgimg=pg.image.load('space-bg.jpg')
loopv2=True
#clock
clock=pg.time.Clock()

#images
img1,img2=pg.image.load('r1.png'),pg.image.load('r2.png')
img1,img2=pg.transform.rotate(img1,-90),pg.transform.rotate(img2,90)
bullet1img=bullet2img=pg.image.load('horizontal bullet.png')
bullet2img=pg.transform.rotate(bullet1img,180)

#spaceships
s1_xchange= s1_ychange=s2_xchange=s2_ychange=0
s1_x=100
s2_x=1400
s1_y=s2_y=460
def s1move(x,y):
         screen.blit(img1,(x,y))
def s2move(x,y):
         screen.blit(img2,(x,y))



#bulletstate and coordinates
bullet11_state=bullet12_state=bullet21_state=bullet22_state='stop'
bullet11_x=bullet12_x=s1_x
bullet11_y,bullet12_y=s1_y-15,s1_y+40
bullet22_x,bullet22_y=bullet21_x,bullet21_y=s2_x,s2_y+40
bullet11_xchange=bullet12_xchange=bullet11_ychange=bullet12_ychange=bullet21_xchange=bullet22_xchange=bullet21_ychange=bullet22_ychange=0

#sounds
laser=mixer.Sound('LASER.wav')
GO=mixer.Sound('game-over.wav')
m_sound=mixer.Sound('Mario.mpeg')

#constants
health1=health2=5
s=0

#fonts
font1=pg.font.SysFont('Blackadder ITC',32)
font_al=pg.freetype.Font('SwipeRace.ttf',55)
showfont1=font1.render("Player 1",True,(0,0,0))
showfont2=font1.render("Player 2",True,(0,0,0))
showfont_go=font_al.render("GAME OVER",True,(0,0,0))



#defintions
def fire11(x,y):
         global bullet11_state
         bullet11_state='go'
         screen.blit(bullet1img,(x,y))

def fire12(x,y):
         global bullet12_state
         bullet12_state='go'
         screen.blit(bullet1img,(x,y))

def fire21(x,y):
         global bullet21_state
         bullet21_state='go'
         screen.blit(bullet2img,(x,y))

def fire22(x,y):
         global bullet22_state
         bullet22_state='go'
         screen.blit(bullet2img,(x,y))
def dist1(x1,x2,y1,y2):
         dist=m.sqrt((x2-x1)**2+(y2-y1)**2)
         if dist<=25:
                  return True
         else:
                  return False
         






while loopv2:
         #screen
         screen.fill((0,0,0))
         screen.blit(bgimg,(-100,-100))
         #FONTS_HEALTH
         screen.blit(showfont1,(10,10))
         screen.blit(showfont2,(1500,10))
         
         
         pg.draw.rect(screen,(0,0,0),(10,50,300,30),3)
         pg.draw.rect(screen,(0,0,0),(1290,50,300,30),3)
         for x in range(health1):
                  pg.draw.rect(screen,(255,80,80),((60*x)+10,50,60,30))
         for y in range(health2):
                  pg.draw.rect(screen,(255,80,80),((60*y)+1290,50,60,30))
                  
         pg.draw.line(screen,(0,0,0),(800,100),(800,820),width=5)
         pg.draw.line(screen,(0,0,0),(0,100),(1600,100),width=5)
         for event in pg.event.get():
                  if event.type==pg.QUIT:
                           loopv2=False
                  if event.type==pg.KEYDOWN:
                           if event.key==pg.K_a:
                                   s1_xchange=-2

                           if event.key==pg.K_s:
                                    s1_ychange=2

                           if event.key==pg.K_d:
                                   s1_xchange=2

                           if event.key==pg.K_w:
                                    s1_ychange=-2
                                    
                           if event.key==pg.K_LEFT:
                                   s2_xchange=-2
                                   
                           if event.key==pg.K_DOWN:
                                    s2_ychange=2
                                    
                           if event.key==pg.K_RIGHT:
                                   s2_xchange=2
                                   
                           if event.key==pg.K_UP:
                                    s2_ychange=-2
                                    
                           if event.key==pg.K_CAPSLOCK:
                                    fire11(bullet11_x,bullet11_y)
                                    fire12(bullet12_x,bullet12_y)
                                    mixer.Sound.play(laser)
                                    
                           if event.key==pg.K_0:
                                    fire21(bullet21_x,bullet21_y)
                                    fire22(bullet22_x,bullet22_y)
                                    mixer.Sound.play(laser)
                                    
                  if event.type==pg.KEYUP:
                          if event.key==pg.K_a or event.key==pg.K_s or  event.key==pg.K_w or event.key==pg.K_d or event.key==pg.K_LEFT or event.key==pg.K_RIGHT or  event.key==pg.K_DOWN or event.key==pg.K_UP:
                                   s1_xchange=s2_xchange=s1_ychange=s2_ychange=0
                           
                                   
                                   

         #SPACESHIP MOVEMENTS
         s1_x+=s1_xchange
         s1_y+=s1_ychange
         s2_x+=s2_xchange
         s2_y+=s2_ychange
         s1move(s1_x,s1_y)
         s2move(s2_x,s2_y)
         
         #PLAYER 1 BULLETS
         if bullet11_state=='stop':
                  bullet11_x=s1_x
                  bullet11_y=s1_y-10
         if bullet12_state=='stop':
                  bullet12_x=s1_x
                  bullet12_y=s1_y+45
         
         if bullet11_x>1550:         
                  bullet11_state='stop'
         if bullet12_x>1550:         
                  bullet12_state='stop'

         if bullet11_state=='go':
                  fire11(bullet11_x,bullet11_y)                  
                  bullet11_x+=6
         if bullet12_state=='go':
                  fire12(bullet12_x,bullet12_y)
                  bullet12_x+=6

         #player 2 bullets
         if bullet21_state=='stop':
                  bullet21_x=s2_x
                  bullet21_y=s2_y-10
         if bullet22_state=='stop':
                  bullet22_x=s2_x
                  bullet22_y=s2_y+45
         
         if bullet21_x <0:         
                  bullet21_state='stop'
         if bullet22_x <0:         
                  bullet22_state='stop'

         if bullet21_state=='go':
                  fire21(bullet21_x,bullet21_y)                  
                  bullet21_x-=6
         if bullet22_state=='go':
                  fire22(bullet22_x,bullet22_y)
                  bullet22_x-=6


         #COLLISION
         b11s2=dist1(bullet11_x,s2_x,bullet11_y-10,s2_y)
         b12s2=dist1(bullet12_x,s2_x,bullet12_y-10,s2_y)
         b21s1=dist1(bullet21_x,s1_x,bullet21_y-10,s1_y)
         b22s1=dist1(bullet22_x,s1_x,bullet22_y-10,s1_y)

         while b11s2 or b12s2:
                  if (b11s2 and not b12s2) :
                           bullet11_state='stop'
                           health2-=1
                  if(not b11s2 and  b12s2):
                           bullet12_state='stop'
                           health2-=1
                  elif b11s2 and b12s2:
                           bullet11_state='stop'
                           bullet12_state='stop'
                           health2-=2
                  break
         while b21s1 or b22s1:
                  if (b21s1 and not b22s1) :
                           bullet21_state='stop'
                           health1-=1
                  if(not b21s1 and  b22s1):
                           bullet22_state='stop'
                           health1-=1
                  elif b21s1 and b22s1:
                           bullet21_state='stop'
                           bullet22_state='stop'
                           health1-=2
                  break

        
         
        



         #boundaries
         if s1_x<=0:
                  s1_x=0
         if s2_x>=1542:
                  s2_x=1542
         if s1_y<98:
                  s1_y=98
         if s2_y<100:
                  s2_y=100
         if s1_x>672:
                  s1_x=672
         if s2_x<872:
                  s2_x=872
         if s1_y>750:
                  s1_y=750
         if s2_y>753:
                  s2_y=752
         #gameover

         if health1<=0:
                  screen.fill((0,0,0))
                  screen.blit(bgimg,(-100,-100))

                  if s==0:
                           mixer.Sound.play(m_sound)
                           t.sleep(3)
                  font_al.render_to(screen,(425,330),"Game Over",(0,0,0))
                  font_al.render_to(screen,(425,430),"Player 2 won",(0,0,0))
                  mixer.Sound.play(GO)
                  s+=1         
                  if s==2:
                           break
         if health2<=0:
                  screen.fill((0,0,0))
                  screen.blit(bgimg,(-100,-100))
                  if s==0:
                           mixer.Sound.play(m_sound)
                           t.sleep(3)
                           font_al.render_to(screen,(425,330),"Game Over",(0,0,0))
                           font_al.render_to(screen,(425,430),"Player 1 won",(0,0,0))
                  mixer.Sound.play(GO)
                  s+=1
                  if s==2:
                           break
         
         
                           
         pg.display.update()
t.sleep(2)



