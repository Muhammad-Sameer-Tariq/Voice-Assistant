import os

apps = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": r"C:\Users\Pc Planet\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
}

def open_app(app_name):
    for name, path in apps.items():
        if name in app_name.lower():
            os.startfile(path)
            return True

    return False