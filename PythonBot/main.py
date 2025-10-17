from Tools import botTools as bt
from Tools import winTools as wt
import time


window = wt.get_window("Brave")
wt.activate_window(window=window)
time.sleep(1)

wt.screenshot_window(window=window)