import pygame, time
pygame.init()
pygame.joystick.init()

c = pygame.joystick.Joystick(0)
c.init()

while True:
    pygame.event.pump()
    print("X:", round(c.get_axis(0), 2), "Y:", round(c.get_axis(1), 2))
    time.sleep(0.2)