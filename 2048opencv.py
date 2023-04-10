import cv2
import time
import HandTrackingModule as htm 
import pyautogui
from selenium import webdriver

wCam, hCam = 680, 480
url = "file:///C:/Users/SINCHANA/Desktop/Work/Objectdetection_opencv/2048/2048.html"
# chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome()
driver.get(url)
def keyup():
    return driver.execute_script("""
    var event = new KeyboardEvent('keyup', {
        key: 'ArrowLeft',
        code: 'ArrowLeft',
        keyCode: 37,
        isTrusted: true
    });
    
    // Dispatch the event to the webpage
    document.dispatchEvent(event);
""")

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0

detector = htm.HandDetector()
prev_xlandmark = None
prev_ylandmark = None
counter = 0
leftc, rightc = 0, 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img= cv2.flip(img, 1)
    landmarks = detector.findPosition(img, draw=False)
    if len(landmarks)!=0:
        landmark_x = landmarks[9][1]
        landmark_y = landmarks[9][2]
        if prev_xlandmark is not None:
            print('x', prev_xlandmark - landmark_x)
            print('y', prev_ylandmark - landmark_y)
            if (prev_xlandmark - landmark_x)< 0:
                leftc += 1
                if leftc > 10:
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
                    leftc = 0
            else:
                rightc += 1
                if rightc > 10:
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
                    rightc = 0
        
        if not counter % 10:
            prev_ylandmark = landmark_y
            prev_xlandmark = landmark_x
    counter += 1
    cv2.imshow('Img', img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break