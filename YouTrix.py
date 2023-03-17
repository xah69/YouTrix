import pyautogui
import time


# Type some text
#pyautogui.typewrite("Hello, world!")

# Press Enter
#pyautogui.press("enter")
#time.sleep(5)
#pyautogui.click(x=389,y=159)
#pyautogui.scroll(-10000)

"""
youtb_xy = [390,539,619,163,404,357,444,514]
# Press down the "Shift" key for 2 seconds
pyautogui.click(x=youtb_xy[0], y=youtb_xy[1])
time.sleep(30)
pyautogui.click(x=youtb_xy[2], y=youtb_xy[3])
time.sleep(5)
pyautogui.click(x=youtb_xy[4], y=youtb_xy[5])
time.sleep(2)
pyautogui.click(x=youtb_xy[6], y=youtb_xy[7])
time.sleep(15)
pyautogui.scroll(-10000)
"""
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

c1 = [18,15]
c2 = [622,156]
c3 = [343,441]
c4 = [300,309]
c5 = [205,412]
c6 = [363,509]
c7 = [333,385]
c8 = [329,471]
#c9 = [389,159]
c9 = [477,223]

user = ["UCLB87he2D_4Bl8kaTA3nVwA"]
passwd = ["pornstar"]

def log_in(usr,passw):
    click(c1)
    sleep(10)
    write("ch")
    sleep(10)
    enter()
    sleep(10)
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

log_in(user[0],passwd[0])




t1 = [318,428]
t2 = [498,235]
t3 = [326,508]
t4 = [413,630]
t5 = [477,80]
t6 = [154,537]
t7 = [369,162]
#def mine_sub():

"""
for i in range(0,3):
    sleep(20)
    click(t7)
    sleep(15)
    scroll(-5)
    sleep(15)
    click(t1)
    sleep(15)
    click(t2)
    sleep(15)
    click(t3)
    sleep(35)
    click(t4)
    sleep(15)
    click(t5)
    sleep(20)
    click(t6)
    sleep(40)
"""
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

#for sub in range(0,6):
#    mine_sub()


# Get the current x and y coordinate of the mouse
"""
while True:
    x, y = pyautogui.position()

    print(f"Current mouse position: x={x}, y={y}")
"""    
