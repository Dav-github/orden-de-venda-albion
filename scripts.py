import pyautogui
import time

def venderItens(number):
    ## Mover até o jogo
    pyautogui.click(x=1001, y=1053, clicks=1, button='left')
    timeSleep = 0.3

    for i in range(number):
        ## Mover para vender
        pyautogui.click(x=1269, y=432, clicks=1, button='left')
        time.sleep(timeSleep)

        ## Mover para 1c a menos
        pyautogui.click(x=564, y=635, clicks=1, button='left')
        time.sleep(timeSleep)

        ## Mover para criar ordem
        pyautogui.click(x=885, y=734, clicks=1, button='left')
        time.sleep(timeSleep)

venderItens(48)