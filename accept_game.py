import time
import mouse_functions as ms
import image_processing as img


# coordinates for resolution 1024x768
menu_cords = {
    'play': (642, 139),
    'coop_vs_ai': (357, 274),
    'classic': (469, 241),
    'summoners_rift': (702, 247),
    'beginner': (892, 239),
    'intermediate': (871, 271)
    }

# Choose the type of the game  - 5 humans vs 5 bots (level easy)
ms.move_mouse(menu_cords['play'])
time.sleep(.1)
ms.left_click()
ms.move_mouse(menu_cords['coop_vs_ai'])
time.sleep(.1)
ms.left_click()
ms.move_mouse(menu_cords['classic'])
time.sleep(.1)
ms.left_click()
ms.move_mouse(menu_cords['summoner_rift'])
time.sleep(.1)
ms.left_click()
ms.move_mouse(menu_cords['beginner'])
time.sleep(.1)
ms.left_click()

# Wait for the game

in_champ_select = False
while(not in_champ_select):
    pass
