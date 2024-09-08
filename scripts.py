import pyautogui
import time
import keyboard

def venderItens(number):
    ## Mover até o jogo
    ## pyautogui.click(x=1001, y=1053, clicks=1, button='left')
    timeSleep = 0.3

    for i in range(number):
        if keyboard.is_pressed('esc'):
            print("Execução interrompida pela tecla 'Esc'.")
            break

        ## Mover para vender
        pyautogui.click(x=1186, y=461, clicks=1, button='left') 
        time.sleep(timeSleep)

        ## Mover para 1c a menos
        pyautogui.click(x=668, y=611, clicks=1, button='left')
        time.sleep(timeSleep)

        ## Mover para criar ordem
        pyautogui.click(x=905, y=683, clicks=1, button='left')
        time.sleep(timeSleep)

venderItens(8)