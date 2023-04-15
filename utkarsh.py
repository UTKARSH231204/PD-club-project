
'''
import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.list_mode((600, 400))
mixer.music.load("r'C:\Users\AS\Music\song1.mp3")
mixer.music.play()

print("Press 'p' to pause 'r' to resume")
print("Press 'q' to quit")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_r:
                mixer.music.unpause()
            if event.key == pygame.K_q:
                running = False
quit()


'''
import pygame
from pygame import mixer

pygame.init()
mixer.init()

print("saude baazi, kesariyan ")
choice=input("song")
if choice=="saude baazi":
  mixer.music.load ("C:\Users\AS\Music\song1.mp3")
  mixer.music.play()
if choice=="kesariyan":
  mixer.music.load( "C:\Users\AS\Music\song2.mp3")
  mixer.music.play()
  
print("Press 'u' to pause 'v' to resume")
print("Press 'd' to end")

while running:
     for event in pygame.event.get():
       
        if event.type == pygame.END:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_u:
                mixer.music.pause()
            
            if event.key == pygame.K_v:
                mixer.music.unpause()
            
            if event.key == pygame.K_d:
                running = False
end()








