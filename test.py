import pyautogui
import threading



def main():
    threading.Timer(15.0, main).start()
    pyautogui.typewrite('Goose1840')
    pyautogui.press('enter')

main()
