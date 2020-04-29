import pyperclip
import pyautogui

def write(text):
    prev_clipboard = pyperclip.paste()
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    pyperclip.copy(prev_clipboard)
