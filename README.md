# ENVYYY Rocket League Macros 🎮⚡
Controller-first mechanics macros for Rocket League using **keyboard + mouse input injection** (works while you play on controller).

Built for clean execution, consistency, and fast mechanics — **no overlays**, no memory reading, no game injection.

---

## ✅ What This Project Does
This project gives you:
- **8-way directional speedflip macro** (tap LB / L1)
- **wavedash / speedboost macro** (hold LB / L1)
- **mode selector using D-pad while holding LB**
- **separate toggles for each system**
- **Windows notifications** for toggles + mode changes

---

## ⚡ Features
### ✅ Speedflip (8-way)
- Tap **LB / L1** → speedflip in the direction your **left stick** is held
- Supports forward/back/left/right + diagonals

### ✅ Wavedash / Speedboost
- Hold **LB / L1** → wavedash macro executes
- Optional **DOUBLE wavedash** mode (2x chained)

### ✅ Mode Selector (LB + D-pad)
While holding LB:
- **D-pad Left** → Wavedash LEFT  
- **D-pad Right** → Wavedash RIGHT  
- **D-pad Down** → Wavedash FORWARD (default)  
- **D-pad Up** → DOUBLE WAVEDASH (2x)

### ✅ Independent Toggles
- **F7** → Speedflip ON/OFF  
- **F8** → Wavedash ON/OFF  

You’ll get a Windows notification confirming each toggle/mode change.

---

## 🎮 Controls (Controller + Keyboard)
### Controller
| Input | Action |
|------|--------|
| Tap LB / L1 | Speedflip macro (8-way) |
| Hold LB / L1 | Wavedash macro |
| LB + D-pad Left | Wavedash mode: LEFT |
| LB + D-pad Right | Wavedash mode: RIGHT |
| LB + D-pad Down | Wavedash mode: FORWARD |
| LB + D-pad Up | Wavedash mode: DOUBLE |

### Keyboard / Mouse
| Key | Action |
|-----|--------|
| F7 | Toggle Speedflip ON/OFF |
| F8 | Toggle Wavedash ON/OFF |
| `>` / `<` | Increase / decrease multiplier (timing tuning) |
| `g` | Speedflip trigger (keyboard backup) |
| Mouse Right Click | Jump input used by macros |

---

## ✅ Quick Install
### Option A (Recommended): Run the batch file
Just run the batch file and it installs everything + launches the script:
- `RUN_ENVYYY_MACRO_ADMIN.bat`

### Option B: Manual install (venv)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python Main_Macros.py...

✅ Running
One-click (recommended)

Double click:

• RUN_ENVYYY_MACRO_ADMIN.bat

Manual run
python Main_Macros.py

----- Tip: Run as Administrator for the most reliable key injection in Rocket League. -----

🔧 Tuning

You may want to tune a few values for your setup.

>Controller deadzone<

• If stick triggers too easily:
DEADZONE = 0.55

>Wavedash timing (main tuning knob)<

• If wavedash is too early/late:
WAVEDASH_LAND_DELAY = 0.11
~ Recommended range: 0.09 → 0.13 ~

>Hold threshold<

• Tap vs hold LB sensitivity:
HOLD_THRESHOLD = 0.25


### 🧪 Test Tools (Folder: Test_Tools/)

- These are helper scripts to identify controller input:

•Controller_Test.py → shows controller name + axes/buttons
•Button_Identifier.py → find your LB/L1 index
•AxisConfirm.py → verify left stick axis mapping

#  🛠 Troubleshooting
Macro does nothing in Rocket League

✅ Run the script as Administrator
✅ Use Borderless Windowed mode
✅ Ensure the script sees your controller (prints “Controller detected”)

No notifications showing

Windows may hide them:

•Settings → System → Notifications
•Disable “Focus Assist”
•Controller direction feels wrong

Your controller may use different axis mapping:
Try changing:
AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1


⚠️ Disclaimer!!!

•This project uses input automation (keyboard/mouse simulation).
•Use responsibly. You are responsible for how and where you use it.


📜 License

This project is released under a restrictive license.
No redistribution, no derivatives, no re-uploads without permission.
See LICENSE for full terms.

# -----------------------------------------------END----------------------------------------------------------
