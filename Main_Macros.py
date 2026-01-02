import time
import keyboard
import mouse
import pygame

# ✅ SAFE Windows notifications
from plyer import notification

def notify(msg, duration=2):
    try:
        notification.notify(
            title="ENVYYY",
            message=msg,
            timeout=duration
        )
    except Exception:
        print(f"[ENVYYY] {msg}")

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0) if pygame.joystick.get_count() > 0 else None
if controller:
    controller.init()
    print("✅ Controller detected:", controller.get_name())
    print("Axes:", controller.get_numaxes(), "| Buttons:", controller.get_numbuttons(), "| Hats:", controller.get_numhats())
else:
    print("⚠️ No controller detected. Keyboard-only mode.")

# ---------------- SETTINGS ----------------
multiplier = 0.85
hotKey = 'g'
RMB = "right"  # jump (mouse right click)

airRollRight = "e"
airRollLeft = "q"

randomizerChange = 0.06
randomizer = True
randomizerPlus = 0

AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1

DEADZONE = 0.55
TRIGGER_BUTTON = 4  # LB / L1

# tap vs hold LB
HOLD_THRESHOLD = 0.25
lb_down_time = None
wavedash_triggered = False

# cooldowns
COOLDOWN_SPEEDFLIP = 0.35
COOLDOWN_WAVEDASH = 0.50
last_speedflip_time = 0
last_wavedash_time = 0

# toggles
SPEEDFLIP_ENABLED = True   # F7
WAVEDASH_ENABLED = True    # F8

TOGGLE_SPEEDFLIP_KEY = "f7"
TOGGLE_WAVEDASH_KEY = "f8"

# wavedash mode selector (LB + D-pad)
WAVEDASH_MODE = "FORWARD"  # FORWARD / LEFT / RIGHT / DOUBLE
last_hat = (0, 0)
HAT_COOLDOWN = 0.12
last_hat_change_time = 0

# wavedash timings (tunable)
WAVEDASH_LAND_DELAY = 0.11   # main tuning knob (0.09 - 0.13)
WAVEDASH_BETWEEN_DELAY = 0.20  # delay between double wavedash attempts

# ---------------- UI ----------------
def PrintBanner(endTime=0.0):
    banner = f"""\n\n\n\n\n
 ███████╗███╗   ██╗██╗   ██╗██╗   ██╗██╗   ██╗██╗   ██╗
 ██╔════╝████╗  ██║██║   ██║╚██╗ ██╔╝╚██╗ ██╔╝╚██╗ ██╔╝
 █████╗  ██╔██╗ ██║██║   ██║ ╚████╔╝  ╚████╔╝  ╚████╔╝ 
 ██╔══╝  ██║╚██╗██║╚██╗ ██╔╝  ╚██╔╝    ╚██╔╝    ╚██╔╝  
 ███████╗██║ ╚████║ ╚████╔╝    ██║      ██║      ██║   
 ╚══════╝╚═╝  ╚═══╝  ╚═══╝     ╚═╝      ╚═╝      ╚═╝   
----------------------------------------------------------------
(">": Increase, "<": Decrease)  Multiplier:            {multiplier}
(Speed flip time)               Last time:             {str(endTime)[0:5]}
(Randomizer "/")                Randomizer:            {randomizer}
(Trigger Button)                LB/L1 index:           {TRIGGER_BUTTON}
(F7)                            Speedflip Enabled:     {SPEEDFLIP_ENABLED}
(F8)                            Wavedash Enabled:      {WAVEDASH_ENABLED}
(LB + D-pad)                     Wavedash Mode:         {WAVEDASH_MODE}
(Deadzone)                      DEADZONE:              {DEADZONE}
"""
    print(banner)

# ---------------- Delays ----------------
def UpdateDelays(print=True):
    global delay1, delay2, delay3, delay4, delay5, delay6
    delay1 = round(0.007 * multiplier, 4)
    delay2 = round(0.06 * multiplier, 4)
    delay3 = round(0.012 * multiplier, 4)
    delay4 = round(0.6 * multiplier, 4)
    delay5 = round(0.15 * multiplier, 4)
    delay6 = round(0.1 * multiplier, 4)
    if print:
        PrintBanner()

UpdateDelays()

# ---------------- Tuning ----------------
def Increase(x):
    global multiplier
    multiplier = round(multiplier + 0.025, 4)
    UpdateDelays()

def Decrease(x):
    global multiplier
    multiplier = round(multiplier - 0.025, 4)
    if multiplier < 0:
        multiplier = 0
    UpdateDelays()

# ---------------- Randomizer ----------------
i = 1
def UpdateI():
    global i
    if not randomizer:
        return

    if i == 1:
        i = 2
    elif i == 2:
        i = 3
    elif i == 3:
        i = 4
    elif i == 4:
        i = 1

# ---------------- Stick direction ----------------
def get_stick_direction_8way():
    if not controller:
        return (0, 0)

    x = controller.get_axis(AXIS_LEFT_STICK_X)
    y = controller.get_axis(AXIS_LEFT_STICK_Y)
    y = -y

    x_dir = 0
    y_dir = 0

    if x > DEADZONE: x_dir = 1
    elif x < -DEADZONE: x_dir = -1

    if y > DEADZONE: y_dir = 1
    elif y < -DEADZONE: y_dir = -1

    return (x_dir, y_dir)

# ---------------- Speedflip macro ----------------
def DoSpeedFlipDirectional(x_dir, y_dir):
    start = time.time()

    lastW = keyboard.is_pressed('w')

    move_keys = []
    if y_dir == 1:
        move_keys.append('w')
    elif y_dir == -1:
        move_keys.append('s')

    air_roll_key = None
    if x_dir == 1:
        move_keys.append('d')
        air_roll_key = airRollRight
    elif x_dir == -1:
        move_keys.append('a')
        air_roll_key = airRollLeft

    mouse.press(RMB)
    time.sleep(delay2)
    mouse.release(RMB)
    time.sleep(delay3)

    for k in move_keys:
        keyboard.press(k)

    time.sleep(delay1)

    mouse.press(RMB)
    time.sleep(delay3)
    mouse.release(RMB)
    time.sleep(delay3)

    for k in move_keys:
        keyboard.release(k)

    time.sleep(delay3)

    if air_roll_key:
        keyboard.press(air_roll_key)

    time.sleep(delay4)

    if x_dir == 1:
        keyboard.press('d'); time.sleep(delay5); keyboard.release('d')
    elif x_dir == -1:
        keyboard.press('a'); time.sleep(delay5); keyboard.release('a')

    time.sleep(delay6)

    if air_roll_key:
        keyboard.release(air_roll_key)

    if lastW:
        keyboard.press('w')

    keyboard.release(hotKey)

    end = time.time() - start
    PrintBanner(endTime=end)

# ---------------- Wavedash macro ----------------
def DoWaveDash(direction="FORWARD"):
    """
    Wavedash logic:
    - jump (RMB)
    - wait a short landing delay
    - dodge in chosen direction (RMB + WASD)
    """
    # First jump
    mouse.press(RMB)
    time.sleep(0.015)
    mouse.release(RMB)

    time.sleep(WAVEDASH_LAND_DELAY * multiplier)

    # Directional dodge
    if direction == "FORWARD":
        keyboard.press('w')
    elif direction == "LEFT":
        keyboard.press('a')
    elif direction == "RIGHT":
        keyboard.press('d')

    mouse.press(RMB)
    time.sleep(0.015)
    mouse.release(RMB)

    # Release direction keys
    if direction == "FORWARD":
        keyboard.release('w')
    elif direction == "LEFT":
        keyboard.release('a')
    elif direction == "RIGHT":
        keyboard.release('d')

def DoDoubleWaveDash():
    DoWaveDash("FORWARD")
    time.sleep(WAVEDASH_BETWEEN_DELAY * multiplier)
    DoWaveDash("FORWARD")

# ---------------- D-pad selection gated by LB ----------------
def update_wavedash_mode_from_hat():
    global WAVEDASH_MODE, last_hat, last_hat_change_time

    if not controller or controller.get_numhats() == 0:
        return

    now = time.time()
    hat = controller.get_hat(0)

    if hat != last_hat and (now - last_hat_change_time) > HAT_COOLDOWN:
        last_hat = hat
        last_hat_change_time = now

        # left/right/down/up
        if hat[0] == -1:
            WAVEDASH_MODE = "LEFT"
            notify("Wavedash: LEFT")
            PrintBanner()
        elif hat[0] == 1:
            WAVEDASH_MODE = "RIGHT"
            notify("Wavedash: RIGHT")
            PrintBanner()
        elif hat[1] == -1:
            WAVEDASH_MODE = "FORWARD"
            notify("Wavedash: FORWARD")
            PrintBanner()
        elif hat[1] == 1:
            WAVEDASH_MODE = "DOUBLE"
            notify("Wavedash: DOUBLE")
            PrintBanner()

# ---------------- Toggles ----------------
def ToggleSpeedflip(x=None):
    global SPEEDFLIP_ENABLED
    SPEEDFLIP_ENABLED = not SPEEDFLIP_ENABLED
    notify(f"Speedflip {'ENABLED' if SPEEDFLIP_ENABLED else 'DISABLED'}")
    PrintBanner()

def ToggleWavedash(x=None):
    global WAVEDASH_ENABLED
    WAVEDASH_ENABLED = not WAVEDASH_ENABLED
    notify(f"Wavedash {'ENABLED' if WAVEDASH_ENABLED else 'DISABLED'}")
    PrintBanner()

keyboard.on_press_key(">", Increase)
keyboard.on_press_key("<", Decrease)
keyboard.on_press_key("/", lambda x: ToggleRandomizer(x) if False else None)  # placeholder
keyboard.on_press_key(TOGGLE_SPEEDFLIP_KEY, ToggleSpeedflip)
keyboard.on_press_key(TOGGLE_WAVEDASH_KEY, ToggleWavedash)

PrintBanner()

# ---------------- MAIN LOOP ----------------
while True:
    time.sleep(0.005)
    pygame.event.pump()

    now = time.time()
    trigger_pressed = controller.get_button(TRIGGER_BUTTON) if controller else 0

    # D-pad only works for macro when holding LB
    if trigger_pressed:
        update_wavedash_mode_from_hat()

    # Track LB press
    if trigger_pressed and lb_down_time is None:
        lb_down_time = now
        wavedash_triggered = False

    # LB release = tap => speedflip (if enabled)
    if not trigger_pressed and lb_down_time is not None:
        held_time = now - lb_down_time
        lb_down_time = None

        if held_time < HOLD_THRESHOLD and SPEEDFLIP_ENABLED and (now - last_speedflip_time > COOLDOWN_SPEEDFLIP):
            last_speedflip_time = now
            x_dir, y_dir = get_stick_direction_8way()
            if x_dir == 0 and y_dir == 0:
                continue
            DoSpeedFlipDirectional(x_dir, y_dir)
            time.sleep(0.25)

    # Hold LB => wavedash (if enabled)
    if trigger_pressed and lb_down_time is not None:
        held_time = now - lb_down_time
        if held_time >= HOLD_THRESHOLD and WAVEDASH_ENABLED and not wavedash_triggered and (now - last_wavedash_time > COOLDOWN_WAVEDASH):
            wavedash_triggered = True
            last_wavedash_time = now

            if WAVEDASH_MODE == "DOUBLE":
                DoDoubleWaveDash()
            else:
                DoWaveDash(WAVEDASH_MODE)

            time.sleep(0.25)

    # keyboard hotkey still triggers speedflip (if enabled)
    if keyboard.is_pressed(hotKey) and SPEEDFLIP_ENABLED and (now - last_speedflip_time > COOLDOWN_SPEEDFLIP):
        last_speedflip_time = now
        x_dir, y_dir = get_stick_direction_8way()
        if x_dir == 0 and y_dir == 0:
            continue
        DoSpeedFlipDirectional(x_dir, y_dir)
        time.sleep(0.25)