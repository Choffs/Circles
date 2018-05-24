import pygame,sys
from Objects import Circle


class EventListener:

    def __init__(self,screen):
        self.screen = screen
        self.circles = []
        print("Event Listener Initialized")

    def CheckEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.circles.append(Circle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
