import cv2 as cv
import pyautogui

vid = cv.VideoCapture(0)

while True:
    val, frame = vid.read()
    gray_im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    left = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
    face_rect = left.detectMultiScale(gray_im, 1.1, 1)

    if (len(face_rect) == 2):
        centre1 = ((2 * face_rect[0][0] + face_rect[0][2]) // 2, (2 * face_rect[0][1] + face_rect[0][3]) // 2)
        centre2 = ((2 * face_rect[1][0] + face_rect[1][2]) // 2, (2 * face_rect[1][1] + face_rect[1][3]) // 2)

        cv.circle(frame, centre1, 10, (0, 0, 255), 2)
        cv.circle(frame, centre2, 10, (0, 0, 255), 2)
        cv.line(frame, centre1, centre2, (0, 255, 0), 1)

        slope = (centre2[1] - centre1[1]) / (centre2[0] - centre1[0])

        if 0.15 < slope < 2:
            pyautogui.press('left')
            #print(f'{slope} = LEFT')
        elif -2 < slope < -0.15:
            pyautogui.press('right')
            #print(f'{slope} = RIGHT')
        
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()