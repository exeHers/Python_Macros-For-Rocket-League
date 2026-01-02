import pygame, time
pygame.init()
pygame.joystick.init()

c = pygame.joystick.Joystick(0)
c.init()

print("Buttons:", c.get_numbuttons())

while True:
    pygame.event.pump()
    for i in range(c.get_numbuttons()):
        if c.get_button(i):
            print("Pressed:", i)
            time.sleep(0.2)