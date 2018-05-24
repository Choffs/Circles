import pygame
from EventListener import EventListener

class GI:

    def __init__(self):
        print("Pygame Version: {ver}".format(ver=pygame.ver))
        pygame.init()
        pygame.display.set_caption("Circles")
        self.WindowSize = (1920,1080)

        self.BGroundColor = (255,128,45)
        self.screen = pygame.display.set_mode(self.WindowSize,pygame.FULLSCREEN)
        self.bGameShouldLoop = True
        self.EL = EventListener(self.screen)
        self.screen.fill((255,128,45))


    def Update(self):
            if self.bGameShouldLoop:
                    self.EL.CheckEvents()
                    self.screen.fill(self.BGroundColor)
                    for x in self.EL.circles:
                        if x.radius < self.WindowSize[0]:
                            pygame.draw.circle(self.screen,x.color,(x.Location[0],x.Location[1]),x.radius,x.thickness)
                            x.UpdateSize()
                        else:
                            if x.thickness == 0:
                                self.BGroundColor = x.color
                                self.screen.fill(self.BGroundColor)
                            self.EL.circles.remove(x)
                    pygame.display.flip()
