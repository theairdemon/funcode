# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:23:48 2019

@author: hgall
"""

import pyautogui as pyg
import time

pyg.FAILSAFE = True
time.sleep(5)
for i in range(0, 1000):
    pyg.press("left")
    pyg.press("down")
    pyg.press("right")
    pyg.press("down")
    if i % 101 == 0:
        pyg.press("up")
        pyg.press("down")