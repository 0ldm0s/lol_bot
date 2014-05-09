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
    'match_me': (777, 811),
    'lock_in': (875, 609),
    'lol_logo':(91, 132)
    }

time_to_wait = 1

#correct_cords = img.find_image(cv2.imread('img/accept_button_screen.png', 0), cv2.imread('img/accept_button.jpg', 0))
correct_cords = (545, 541)


def enter_champion_select():
	in_champ_select = False
	while(not in_champ_select):
	    print 'waiting for accept button...'
	    img.screen_grab()
	    cords = img.find_image(cv2.imread('test.png', 0), cv2.imread('img/accept_button.jpg', 0))
	    if abs(correct_cords[0] - cords[0]) < 30 and abs(correct_cords[1] - cords[1]) < 30:
		    in_champ_select = True
	    print cords
	ms.move_mouse(cords)
	ms.left_click()
	time.sleep(10)
	# Now we should be in champion select

def select_champion():
	# Select Master Yi
	img.screen_grab()
	cords = img.find_image(cv2.imread('test.png', 0), cv2.imread('img/master_yi_portrait.jpg', 0))
	ms.move_mouse(cords)
	time.sleep(1)
	ms.left_click()
	time.sleep(1)

def check_if_in_champ_select():
	cords = img.find_image(cv2.imread('test.png', 0), cv2.imread('img/lock_in_button.jpg', 0))
	if abs(cords[0] - menu_cords['lock_in'][1]) < 50 and abs(cords[1] - menu_cords['lock_in'][0]) < 50:
		return True
	return False

def check_if_in_game():
	cords = img.find_image(cv2.imread('test.png', 0), cv2.imread('img/lol_logo.jpg', 0))
	if abs(cords[0] - menu_cords['lol_logo'][1]) < 50 and abs(cords[1] - menu_cords['lol_logo'][0]) < 50:
		return True
	return False


# wait 5 seconds before starting
#time.sleep(5)

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


succes = False
in_champ_select = False

while(not succes):
	# Wait for the game asking for confirmation
	print 'STARTED MAIN LOOP'
	enter_champion_select()
	in_champ_select = check_if_in_champ_select()
	select_champion()
	if not in_champ_select:
		print 'not in champ select!'
		continue
	else:
		# Lock in
		ms.move_mouse(menu_cords['lock_in'])
		ms.left_click()
		# Wait for other ppl to select their champions
		time.sleep(105)
		# Check if game started (smbdy could quit the champ select)
		succes = check_if_in_game


# Wait for the game to start and launch second bot
