from pynput import keyboard
import time

def on_key_press(key):
    if key ==key.right:
        print("Right key pressed")
    if key==key.left:
        print("Left key pressed")
    
\
def on_key_release(key):
  pass

#   if key == keyboard.Key.shift:
#     print("SHIFT KEY RELEASED!")

keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release)

# start the listener
keyboard_listener.start()

time.sleep(1000)