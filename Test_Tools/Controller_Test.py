import pygame
import time

pygame.init()
pygame.joystick.init()

print("Joysticks found:", pygame.joystick.get_count())

if pygame.joystick.get_count() == 0:
    print("❌ No controller detected.")
    exit()

controller = pygame.joystick.Joystick(0)
controller.init()

print("✅ Controller name:", controller.get_name())
print("Axes:", controller.get_numaxes())
print("Buttons:", controller.get_numbuttons())

while True:
    pygame.event.pump()

    x = controller.get_axis(0)
    y = controller.get_axis(1)

    buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]

    print(f"X:{x:.2f} Y:{y:.2f} Buttons:{buttons}")
    time.sleep(0.2)