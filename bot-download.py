#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install pyautogui


# In[260]:


import pyautogui
import time
import itertools
linhas = 1
pyautogui.pause = 0.8
time.sleep(7)
num = 1


# In[261]:


while num < 190:
    num += 1
    #copiar
    pyautogui.hotkey('ctrl' , 'c')
    #alt tab
    pyautogui.hotkey('alt' , 'tab')
    #nova consulta
    pyautogui.moveTo(520, 257)
    pyautogui.click()
    #colar
    pyautogui.hotkey('ctrl' , 'v')
    #consultar nota
    pyautogui.moveTo(831, 249)
    pyautogui.click()
    time.sleep(3)
    #não sou robô
    pyautogui.moveTo(612 , 439)
    pyautogui.click()
    time.sleep(2)
    #download XML
    pyautogui.moveTo(840, 317)
    time.sleep(2)
    pyautogui.click()
    #alt tab
    pyautogui.hotkey('alt' , 'tab')
    #descer linha
    pyautogui.press('down')


# In[190]:


pyautogui.position()

