# --------------------- ADD CHROME ---------------------
import webbrowser
webbrowser.open_new_tab('https://sellercentral.amazon.com/')
import time
time.sleep(2)
# --------------------------------------------------------
# --------------------- ADD MOUSE MOVE RANDOM IN BOUNDARY ---------------------
import pyautogui
import random
import time
import math
def move_like_human(x_start, y_start, x_end, y_end, duration):
    steps = random.randint(1, 7)  # Giảm số bước để di chuyển nhanh hơn
    sleep_time = duration / steps
    for step in range(steps):
        t = step / (steps - 1)  # Đảm bảo t = 1 ở bước cuối cùng
        ease_t = (math.sin((t - 0.5) * math.pi) + 1) / 2  # Hiệu ứng di chuyển mượt
        x = x_start + (x_end - x_start) * ease_t
        y = y_start + (y_end - y_start) * ease_t
        
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)  # Thời gian nghỉ giữa mỗi bước
    pyautogui.moveTo(x_end, y_end)

x_start, y_start = pyautogui.position()
x_end = random.randint(1488, 1527)
y_end = random.randint(223, 256)
move_like_human(x_start, y_start, x_end, y_end, duration=0.02)
time.sleep(2)
# --------------------------------------------------------
# --------------------- ADD MOUSE LEFT CLICK ---------------------
import pyautogui
pyautogui.leftClick()
import time
time.sleep(2)
# --------------------------------------------------------
# --------------------- ADD MOUSE MOVE RANDOM IN BOUNDARY ---------------------
import pyautogui
import random
import time
import math
def move_like_human(x_start, y_start, x_end, y_end, duration):
    steps = random.randint(1, 7)  # Giảm số bước để di chuyển nhanh hơn
    sleep_time = duration / steps
    for step in range(steps):
        t = step / (steps - 1)  # Đảm bảo t = 1 ở bước cuối cùng
        ease_t = (math.sin((t - 0.5) * math.pi) + 1) / 2  # Hiệu ứng di chuyển mượt
        x = x_start + (x_end - x_start) * ease_t
        y = y_start + (y_end - y_start) * ease_t
        
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)  # Thời gian nghỉ giữa mỗi bước
    pyautogui.moveTo(x_end, y_end)

x_start, y_start = pyautogui.position()
x_end = random.randint(1580, 1613)
y_end = random.randint(488, 499)
move_like_human(x_start, y_start, x_end, y_end, duration=0.02)
time.sleep(2)
# --------------------------------------------------------

# --------------------- ADD MOUSE LEFT CLICK ---------------------
import pyautogui
pyautogui.leftClick()
import time
time.sleep(2)
# --------------------------------------------------------

# --------------------------------------------------------


# --------------------- ADD MOUSE MOVE RANDOM IN BOUNDARY ---------------------
import pyautogui
import random
import time
import math
def move_like_human(x_start, y_start, x_end, y_end, duration):
    steps = random.randint(1, 7)  # Giảm số bước để di chuyển nhanh hơn
    sleep_time = duration / steps
    for step in range(steps):
        t = step / (steps - 1)  # Đảm bảo t = 1 ở bước cuối cùng
        ease_t = (math.sin((t - 0.5) * math.pi) + 1) / 2  # Hiệu ứng di chuyển mượt
        x = x_start + (x_end - x_start) * ease_t
        y = y_start + (y_end - y_start) * ease_t
        
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)  # Thời gian nghỉ giữa mỗi bước
    pyautogui.moveTo(x_end, y_end)

x_start, y_start = pyautogui.position()
x_end = random.randint(1136, 1286)
y_end = random.randint(260, 307)
move_like_human(x_start, y_start, x_end, y_end, duration=0.02)
time.sleep(2)
# --------------------------------------------------------
# --------------------- ADD MOUSE LEFT CLICK ---------------------
import pyautogui
pyautogui.leftClick()
import time
time.sleep(2)
# --------------------------------------------------------

# --------------------- ADD SLEEP ---------------------
import time
import random
time.sleep(5 - random.randint(-3, 3))
# --------------------------------------------------------



# --------------------- ADD MOUSE MOVE RANDOM IN BOUNDARY ---------------------
import pyautogui
import random
import time
import math
def move_like_human(x_start, y_start, x_end, y_end, duration):
    steps = random.randint(1, 7)  # Giảm số bước để di chuyển nhanh hơn
    sleep_time = duration / steps
    for step in range(steps):
        t = step / (steps - 1)  # Đảm bảo t = 1 ở bước cuối cùng
        ease_t = (math.sin((t - 0.5) * math.pi) + 1) / 2  # Hiệu ứng di chuyển mượt
        x = x_start + (x_end - x_start) * ease_t
        y = y_start + (y_end - y_start) * ease_t
        
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)  # Thời gian nghỉ giữa mỗi bước
    pyautogui.moveTo(x_end, y_end)

x_start, y_start = pyautogui.position()
x_end = random.randint(915, 926)
y_end = random.randint(439, 451)
move_like_human(x_start, y_start, x_end, y_end, duration=0.02)
time.sleep(1)
# --------------------------------------------------------
# --------------------- ADD MOUSE LEFT CLICK ---------------------
import pyautogui
pyautogui.leftClick()
import time
time.sleep(1)
# --------------------------------------------------------
# --------------------- ADD MOUSE MOVE RANDOM IN BOUNDARY ---------------------
import pyautogui
import random
import time
import math
def move_like_human(x_start, y_start, x_end, y_end, duration):
    steps = random.randint(1, 7)  # Giảm số bước để di chuyển nhanh hơn
    sleep_time = duration / steps
    for step in range(steps):
        t = step / (steps - 1)  # Đảm bảo t = 1 ở bước cuối cùng
        ease_t = (math.sin((t - 0.5) * math.pi) + 1) / 2  # Hiệu ứng di chuyển mượt
        x = x_start + (x_end - x_start) * ease_t
        y = y_start + (y_end - y_start) * ease_t
        
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)  # Thời gian nghỉ giữa mỗi bước
    pyautogui.moveTo(x_end, y_end)

x_start, y_start = pyautogui.position()
x_end = random.randint(1294, 1417)
y_end = random.randint(596, 621)
move_like_human(x_start, y_start, x_end, y_end, duration=0.02)
time.sleep(1)
# --------------------------------------------------------
# --------------------- ADD MOUSE LEFT CLICK ---------------------
import pyautogui
pyautogui.leftClick()
import time
time.sleep(1)
# --------------------------------------------------------
