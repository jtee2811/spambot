# importing modules
import pyautogui
import time
# introducing sleep time to switch between code to app/tab
time.sleep(5)
n = 0
# open file from which contents will be copied from
f = open('file.txt')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press('enter')
f.close()