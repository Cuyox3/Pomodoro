from pynput import keyboard

def on_press(key):
    print(f"Key {key} pressed.")

def on_release(key):
    print(f"Key {key} released.")

# Create a listener for keyboard event
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the program running until interrupted
try:
    while True:
        pass
except KeyboardInterrupt:
    # Stop the listener
    listener.stop()
