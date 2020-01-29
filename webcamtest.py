import cv2
from matplotlib import pyplot as plt
import numpy as np
import vision_params
import threading
import time
from playsound import playsound

def onmouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)

def coordinate(img):
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)  # 构建窗口
    cv2.setMouseCallback("img",onmouse,0) # 回调绑定窗口
    cv2.imshow("img",img) # 显示图像

def getcolor(p):
    """Decide the color of a facelet by its h value (non white) or by s and v (white)."""
    sz = 10
    p = p.astype(np.uint16)
    rect = hsv[p[1] - sz:p[1] + sz, p[0] - sz:p[0] + sz]
    median = np.sum(rect, axis=(0, 1)) / sz / sz / 4
    mh, ms, mv = median
    if ms <= vision_params.sat_W and mv >= vision_params.val_W:
        return median, 'white'
    elif vision_params.orange_L <= mh < vision_params.orange_H:
        return median, 'orange'
    elif vision_params.orange_H <= mh < vision_params.yellow_H:
        return median, 'yellow'
    elif vision_params.yellow_H <= mh < vision_params.green_H:
        if ms < 100:
            return median, 'white'  # green saturation is always higher
        else:
            return median, 'green'
    elif vision_params.green_H <= mh < vision_params.blue_H:
        if ms < 150:
            return median, 'white'  # blue saturation is always higher
        else:
            return median, 'blue'
    else:
        return median, 'red'

def display_colorname(bgrcap, p):
    """Display the colornames on the webcam picture."""
    p = p.astype(np.uint16)
    _, col = getcolor(p)
    if col in ('blue', 'green', 'red'):
        txtcol = (255, 255, 255)
    else:
        txtcol = (0, 0, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    tz = cv2.getTextSize(col, font, 0.4, 1)[0]
    cv2.putText(
        bgrcap, col, tuple(p - (tz[0] // 2, -tz[1] // 2)), font, 0.4, txtcol, 1)
    return col

def coord(center):
    cent=[]
    for i in range(3):
        cent.append(np.asarray(center[i]))
    return cent

def movement(colis):
    if colis[0]==colis[1] and colis[1]==colis[2]:
        if colis[0] == 'red':
            return 0
        else:
            return 1
    else:
        return 3

def detect_color():
    global cent, hsv
    cap=cv2.VideoCapture(0)
    centlist=[(133,350),(307,350),(468,350)]
    while 1:
        _,bgrcap = cap.read()
        cent=coord(centlist)
        hsv = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2HSV)
        colors=[]
        for i in cent:
            col=display_colorname(bgrcap, i)
            colors.append(col)
        move=movement(colors)  #decided is it need to move
        vision_params.move=move
        cv2.imshow('Webcam',bgrcap)
        if move == 0:
            print('jobdone')
            break #no need to move then stop
        k = cv2.waitKey(5) & 0xFF
        if k == 120: # type x to exit
            break
        if k == ord('q'):
            pic = bgrcap
            pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
            coordinate(pic)
        if k == ord('m'):
            print(move)
    cap.release()
    #cv2.destroyAllWindows()
def poiu():
    thr = threading.Thread(target=detect_color, args=())
    thr.start()

def gen():
    if vision_params.move == 1 :

        print('keep move')
        return 1
    elif vision_params.move == 0:
        print('stop')
        return 0
    elif vision_params.move == 3:
        print('the color in last layer is not correct')

# ##############################################################################
poiu()
print ("current has %d threads" % (threading.activeCount() - 1))
T=1
while 1:
    x=gen()
    if x==0:
        break
    elif x==1:
        playsound('0.8.wav')
    time.sleep(1)
