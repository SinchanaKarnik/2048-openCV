import cv2
import time
import HandTrackingModule as htm 
import pyautogui
from selenium import webdriver
import os

dir = os.getcwd()
wCam, hCam = 680, 480
# to load my game html file

url = os.path.join(dir, '2048.html')
driver = webdriver.Chrome()
driver.get(url)

# capture my video using device camera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0

# detect using HandTracking Module
detector = htm.HandDetector()
prev_xlandmark = None
prev_ylandmark = None
# to press cursor only once while moving from mid to any 4 direction
counter = False

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img= cv2.flip(img, 1)
    landmarks = detector.findPosition(img, draw=False)
    if len(landmarks)!=0:
        landmark_x = landmarks[8][1]
        landmark_y = landmarks[8][2]
        if prev_xlandmark is not None and counter:
        
            print(counter)
            counter = False
            #check if hand is mid with respect to y axis then it is either left or right
            if ( landmark_y > 160 and landmark_y < 320):
                
                if landmark_x > 450 and landmark_y > 160 and landmark_y < 320:
                    print('left')
                    #pyautogui.keyDown('left')
                    #time.sleep(1)
                    #pyautogui.keyUp('left')
                    
                    driver.execute_script("""
                    var event = new KeyboardEvent('keyup', {
                    key: 'ArrowLeft',
                    code: 'ArrowLeft',
                    keyCode: 37,
                    isTrusted: true
                    });
                    document.dispatchEvent(event);
                    """)
                elif landmark_x < 226 and landmark_y > 160 and landmark_y < 320:
                
                    print('right')
                    #pyautogui.keyDown('right')
                    #time.sleep(1)
                    #pyautogui.keyUp('right')
                    driver.execute_script("""
                    var event = new KeyboardEvent('keyup', {
                    key: 'ArrowRight',
                    code: 'ArrowRight',
                    keyCode: 38,
                    isTrusted: true
                    });
                    document.dispatchEvent(event);
                    """)
            #check if hand is mid with respect to x axis then it is either up or down
            elif (landmark_x > 226 and landmark_x < 450):
                 print('inside else')
                 counter = False
                 if landmark_y < 160 and landmark_x > 226 and landmark_x < 450:
                        #pyautogui.keyDown('left')
                        #time.sleep(1)
                        #pyautogui.keyUp('left')
                    print('up')  
                    driver.execute_script("""
                    var event = new KeyboardEvent('keyup', {
                    key: 'ArrowUp',
                    code: 'ArrowUp',
                    keyCode: 39,
                    isTrusted: true
                    });
                    document.dispatchEvent(event);
                    """)

                 elif landmark_y > 320 and landmark_x > 226 and landmark_x < 450:
                        #pyautogui.keyDown('right')
                        #time.sleep(1)
                    #pyautogui.keyUp('right')
                    print('down')
                    driver.execute_script("""
                    var event = new KeyboardEvent('keyup', {
                    key: 'ArrowDown',
                    code: 'ArrowDown',
                    keyCode: 40,
                    isTrusted: true
                    });
                    document.dispatchEvent(event);
                    """)


        if not counter and landmark_x > 226 and landmark_x < 450 and landmark_y > 160 and landmark_y < 320:
            counter = True
            prev_ylandmark = landmark_y
            prev_xlandmark = landmark_x
            print('prev', prev_xlandmark, prev_ylandmark)

    cv2.imshow('Img', img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break