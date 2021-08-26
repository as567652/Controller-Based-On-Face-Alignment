# import OpenCV and GUI automation Python module
import cv2 as cv
import pyautogui

# capturing webcam
# add link to video instead of '0' if want to add a video
vid = cv.VideoCapture(0)

while True:
    # taking each frame as input
    val, frame = vid.read()

    #converting to grayscale image
    gray_im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Using Haar Cascade for eye detection
    # cv.data.haarcascades is path to all classifiers pre installed with OpenCV
    left = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_lefteye_2splits.xml')

    # getting numpi 2d array of 2 eyes
    face_rect = left.detectMultiScale(gray_im, 1.1, 1)

    # remove anomoly of irregular object detection as an eye
    # runs only if 2 objects are found
    if (len(face_rect) == 2):

        # getting centre of both boxes drawn
        centre1 = ((2 * face_rect[0][0] + face_rect[0][2]) // 2, (2 * face_rect[0][1] + face_rect[0][3]) // 2)
        centre2 = ((2 * face_rect[1][0] + face_rect[1][2]) // 2, (2 * face_rect[1][1] + face_rect[1][3]) // 2)

        # drawing circle to center of square
        # joined with line
        cv.circle(frame, centre1, 10, (0, 0, 255), 2)
        cv.circle(frame, centre2, 10, (0, 0, 255), 2)
        cv.line(frame, centre1, centre2, (0, 255, 0), 1)

        # calculating slope using formula
        # y2 - y1 = m(x2 - x1)
        # m is slope
        slope = (centre2[1] - centre1[1]) / (centre2[0] - centre1[0])

        # Limiting slope, excluding resting face slope
        # using pyautogui to press left on active window if slope is +ve
        if 0.15 < slope < 2:
            pyautogui.press('left')
            #print(f'{slope} = LEFT')
        # using pyautogui to press right on active window if slope is -ve
        elif -2 < slope < -0.15:
            pyautogui.press('right')
            #print(f'{slope} = RIGHT')
        
    # showing webcam and drawn circles and lines for better understanding
    cv.imshow('Video', frame)

    # break on key 'd' press
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# release captured video
vid.release()

# close all windows
cv.destroyAllWindows()