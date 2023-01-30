import pyautogui
import pywinauto
import time

from headless.headless_game import HeadlessGame

# window = pyautogui.getWindowsWithTitle('Super Auto Pets')[0]

def click_on(image_name: str):
    x, y = pyautogui.locateCenterOnScreen(f'images/{image_name}', region=(window.left, window.top, window.width, window.height))
    pyautogui.click(x, y)

def wait_for(image_name: str):
    while True:
        pos = pyautogui.locateCenterOnScreen(f'images/{image_name}', region=(window.left, window.top, window.width, window.height))
        if pos is None:
            print("Not found")
            time.sleep(1)
            continue
        break

if __name__ == "__main__":
    # if window is None:
    #     raise('Game is not running')
    
    # print(window)
    # # Connecting to the game and bringing it to the front
    # app = pywinauto.Application('win32')
    # app.connect(title='Super Auto Pets')
    # app.top_window().set_focus()

    # pyautogui.click(984, 888)
    # wait_for('roll.png')
    # print("Whoooo")

    game = HeadlessGame()
    game.play()
