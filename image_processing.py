import cv2


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
    center = ((top_left[0] + bottom_right[0])/2.0,
             (top_left[1] + bottom_right[1])/2.0)

    return center

#print find_image(cv2.imread('red_buff_screen.jpeg', 0), cv2.imread('red_buff.jpeg', 0))
