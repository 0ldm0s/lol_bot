import cv2
import os
import ImageGrab


def screen_grab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + 'test.png', 'PNG')
    return im


def find_image(screen, pattern):
    """
    Screen and pattern are objects returned
    from cv2.imread('filename', 0) function
    """

    method = cv2.TM_CCOEFF
    w, h = pattern.shape[::-1]

    # Apply template Matching
    res = cv2.matchTemplate(screen, pattern, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Find center
    center = (int((top_left[0] + bottom_right[0])/2.0),
             int((top_left[1] + bottom_right[1])/2.0))

    return center

#print find_image(screen_grab(), cv2.imread('red_buff.jpeg', 0))
