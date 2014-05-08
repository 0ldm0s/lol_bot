import time
import mouse_functions as ms
import image_processing as img
import cv2


# coordinates for resolution 1024x768
menu_cords = {
    'play': (642, 139),
    'coop_vs_ai': (357, 274),
    'classic': (469, 241),
    'summoners_rift': (702, 247),
    'beginner': (892, 239),
    'intermediate': (871, 271),
    'match_me': (777, 811)
    }

time_to_wait = 0.5


# wait 5 seconds before starting
time.sleep(5)

# Choose the type of the game  - 5 humans vs 5 bots (level easy)
ms.move_mouse(menu_cords['play'])
time.sleep(time_to_wait)
ms.left_click()
ms.move_mouse(menu_cords['coop_vs_ai'])
time.sleep(time_to_wait)
ms.left_click()
ms.move_mouse(menu_cords['classic'])
time.sleep(time_to_wait)
ms.left_click()
ms.move_mouse(menu_cords['summoners_rift'])
time.sleep(time_to_wait)
ms.left_click()
ms.move_mouse(menu_cords['beginner'])
time.sleep(time_to_wait)
ms.left_click()
ms.move_mouse(menu_cords['match_me'])
time.sleep(time_to_wait)
ms.left_click()

# Wait for the game

in_champ_select = False
while(not in_champ_select):
    cords = img.find_image(img.screen_grab(),
                           cv2.imread('img/accept_button.jpg', 0))
    print cords
    ms.left_click(cords)
