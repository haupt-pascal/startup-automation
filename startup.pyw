from pynput.keyboard import Key, Listener
import subprocess
import os


def on_press(key):
    if key == Key.pause:
        print("alright, let's start that shit")
        os.system(r'start explorer shell:appsfolder\notion.id')
        os.system(r'start explorer shell:appsfolder\brave')
        os.system(r'start explorer shell:appsfolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!WhatsAppDesktop')
        os.system(r'start explorer shell:appsfolder\Microsoft.WindowsTerminal_8wekyb3d8bbwe!App')
        subprocess.call(r'C:\Users\Pasca\AppData\Local\Programs\Microsoft VS Code\\code.exe')
        subprocess.call([r'C:\Users\Pasca\AppData\Roaming\Telegram Desktop\Telegram.exe'])


# Collect events until released
with Listener(on_press=on_press) as listener: listener.join()

