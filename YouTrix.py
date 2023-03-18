import pyautogui
import time

def click(c):
    pyautogui.click(x=c[0],y=c[1])

def write(text):
    pyautogui.typewrite(text)

def enter():
    pyautogui.press("enter")

def scroll(val):
    pyautogui.scroll(val)

def sleep(val):
    time.sleep(val)

def find_click(img):
    res = pyautogui.locateOnScreen(img)
    edit_but = pyautogui.center(res)
    pyautogui.moveTo(edit_but)
    sleep(5)
    click(edit_but)

def find(img):
    res = pyautogui.locateOnScreen(img)
    edit_but = pyautogui.center(res)
    pyautogui.moveTo(edit_but)
    return edit_but

#coordinates
#if code not working adjust the coordinates accordingly
c1 = [18,15]
c2 = [622,156]
c3 = [343,441]
c4 = [300,309]
c5 = [205,412]
c6 = [363,509]
c7 = [333,385]
c8 = [329,471]
c9 = [477,223]

user = ["UCLB87he2D_4Bl8kaTA3nVwA"]
passwd = ["pornstar"]

def log_in(usr,passw):
    click(c1)
    sleep(10)
    write("ch")
    sleep(10)
    enter()
    sleep(20)
    pyautogui.hotkey("win","ctrl","left")
    sleep(10)
    write("https://www.subpals.com/")
    enter()
    sleep(15)
    click(c2)
    sleep(10)
    click(c3)
    sleep(10)
    click(c4)
    sleep(10)
    write(usr)
    sleep(10)
    click(c5)
    sleep(10)
    click(c6)
    sleep(10)
    click(c7)
    sleep(10)
    write(passw)
    sleep(10)
    click(c8)
    sleep(10)
    scroll(-5)
    sleep(10)
    click(c9)




#coordinates
#if code not working adjust the coordinates accordingly

t1 = [318,428]
t2 = [498,235]
t3 = [326,508]
t4 = [413,630]
t5 = [477,80]
t6 = [154,537]
t7 = [369,162]

def mine_sub():
    sleep(20)
    click(t7)
    sleep(15)
    scroll(-5)
    sleep(15)
    click(t1)
    sleep(15)
    find_click("sub.png")
    e = find("vid.png")
    print(e)
    xv = e.x
    yv = e.y + 137
    cv = [xv,yv]
    click(cv)
    sleep(10)
    find_click("like.png")
    sleep(15)
    click(t5)
    sleep(20)
    click(t6)
    sleep(40)


def run():
    log_in(user[0],passwd[0])
    for sub in range(0,6):
        mine_sub()

run()

# Get the current x and y coordinate of the mouse
#uncomment it for finding coordinates when required
#after finding coordinates comment it again
"""
while True:
    x, y = pyautogui.position()

    print(f"Current mouse position: x={x}, y={y}")
"""    
