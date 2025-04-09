import pygame
pygame.mixer.init()
pygame.mixer.music.load("project/music/sunny.mp3")
pygame.mixer.music.play()
input("Press Enter to stop")
pygame.mixer.music.stop()