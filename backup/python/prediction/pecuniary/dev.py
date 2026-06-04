import time
import subprocess  # Import the subprocess module
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from screeninfo import get_monitors

# This script automates a sequence of mouse and keyboard actions.
# It has been updated to specifically target the first monitor in a multi-monitor setup
# but can now also handle clicks on absolute physical coordinates.

# --- Setup Controllers ---
mouse = MouseController()
keyboard = KeyboardController()

# Get monitors info
monitors = get_monitors()
if not monitors:
    print("Error: No monitors detected. Exiting script.")
    exit()

first_monitor = monitors[0]
print(f"Targeting 'screen 1' with coordinates: x={first_monitor.x}, y={first_monitor.y}, width={first_monitor.width}, height={first_monitor.height}")

# --- Functions for Actions ---

def move_and_left_click(x, y):
    absolute_x = first_monitor.x + x
    absolute_y = first_monitor.y + y
    print(f"Moving mouse to ({absolute_x}, {absolute_y}) and left-clicking.")
    mouse.position = (absolute_x, absolute_y)
    time.sleep(0.5)
    mouse.click(Button.left)

def move_and_right_click(x, y):
    absolute_x = first_monitor.x + x
    absolute_y = first_monitor.y + y
    print(f"Moving mouse to ({absolute_x}, {absolute_y}) and right-clicking.")
    mouse.position = (absolute_x, absolute_y)
    time.sleep(0.5)
    mouse.click(Button.right)

def type_text_and_enter(text):
    print(f"Typing text: '{text}'")
    keyboard.type(text)
    time.sleep(0.5)
    print("Pressing Enter")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def move_and_paste(x, y):
    absolute_x = first_monitor.x + x
    absolute_y = first_monitor.y + y
    print(f"Moving mouse to ({absolute_x}, {absolute_y}) for paste.")
    mouse.position = (absolute_x, absolute_y)
    time.sleep(0.5)
    print("Performing Ctrl+V (paste)...")
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(1.0)

def type_heading_then_paste(x, y, heading_text, separator, blank_lines=1):
    move_and_left_click(x, y)
    time.sleep(1.0)

    print(f"Typing heading: '{heading_text}'")
    keyboard.type(heading_text)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    print(f"Typing separator: '{separator}'")
    keyboard.type(separator)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for _ in range(blank_lines):
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    time.sleep(2.0)
    print("Pasting clipboard content...")
    move_and_paste(x, y)

# --- Main Automation Sequence ---
if __name__ == "__main__":
    print("--- Starting Automation Script ---")

    move_and_left_click(x=585, y=971)
    time.sleep(1.0)

    move_and_right_click(x=922, y=600)
    time.sleep(1.0)

    type_text_and_enter('cc')
    time.sleep(1.0)

    print("Step 4: Birth Data heading + paste with spacing after.")
    type_heading_then_paste(x=718, y=1052, heading_text="This is the Birth Data", separator="======================", blank_lines=1)

    move_and_left_click(x=559, y=1049)
    time.sleep(1.0)

    move_and_left_click(x=267, y=114)
    time.sleep(1.0)

    move_and_right_click(x=1295, y=428)
    time.sleep(1.0)

    keyboard.type('L')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.0)

    move_and_right_click(x=1295, y=428)
    time.sleep(1.0)

    type_text_and_enter('cc')
    time.sleep(1.0)

    print("Step 9: Dasa Scheme heading + paste with spacing after.")
    type_heading_then_paste(x=721, y=1062, heading_text="This is the Dasa Scheme", separator="================", blank_lines=1)
    
    move_and_left_click(x=544, y=1074)
    move_and_left_click(x=341, y=116)
    move_and_left_click(x=618, y=222)
    move_and_left_click(x=110, y=119)
    move_and_right_click(x=858, y=555)
    type_text_and_enter('cc')
    type_heading_then_paste(x=719, y=1050, heading_text="This is Transit data", separator="====================", blank_lines=0)
    
    move_and_left_click(x=555, y=1058)
    move_and_left_click(x=343, y=113)
    move_and_left_click(x=618, y=165)
    move_and_left_click(x=212, y=115)
    move_and_left_click(x=647, y=974)
    move_and_right_click(x=1353, y=253)
    type_text_and_enter('cc')
    move_and_left_click(x=721, y=1051)

    # Step 25: Type 'Planetary Strength' and the separator
    print("Step 25: Typing heading 'Planetary Strength' and separator.")
    time.sleep(1)
    keyboard.type('Planetary Strength')
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.type('===================')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.0)

    # Step 26: Paste the clipboard content
    print("Step 26: Pasting the clipboard content.")
    move_and_paste(x=721, y=1051)
    time.sleep(3.0)  # Increased delay to give the application more time to respond.

    print("--- Automation Script Finished ---")
    exit()
