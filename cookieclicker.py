import pyautogui
import time
import keyboard
import datetime
import pyttsx3

engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)


rate=engine.getProperty("rate")
engine.setProperty("rate",rate-30)
speak("""als erstes startet das tool, 
die Position muss ermittelt werden was du gerne anklicken möchstest dann gehe auf
die computerps.txt die im selben Projekt Ordner erstellt wird und passe den pyautogui.moveTo mit der richtigen position,
der Grund jeder hat ein anderen Bildschirm
""")
engine.runAndWait()


time.sleep(10)

pos=pyautogui.position()
autoguipos=open("computerpos.txt","a")

autoguipos.write(f"Cookie pos: {str(pos)}")
autoguipos.write("\n")

# print(pos)
# clicken=1000
i=0
pyautogui.moveTo(286, 491)
while True:
    
    i=i+1
    if i==10000:
        exit()
    pyautogui.click(clicks=i,interval=0.25)
    


