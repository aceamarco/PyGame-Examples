#Wee Woo video taken from youtube: https://www.youtube.com/watch?v=0TcTGzgmoR8

import module_manager
module_manager.review()
import pygame
import os

#Set Up Pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 500))

#Set up the audio
pygame.mixer.pre_init()
pygame.init()

#Gets the name of each image files and sorts them because listdir returns in random order
frames = sorted(os.listdir('wee-woo-gif'))
frame_index = 0

playing = True
while playing:
    time = clock.tick(20)

    #Load the current frame and display it
    if frame_index == 0:
        audio = pygame.mixer.Sound(file = 'wee_woo.ogg')
        audio.play()
    img = pygame.image.load(str('wee-woo-gif/' + frames[frame_index])).convert()
    screen.blit(img,(100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #Increases the index and loops again if its done
    frame_index += 1
    if frame_index == len(frames):
        frame_index = 0
        audio.stop()

    pygame.display.flip()

pygame.quit()
