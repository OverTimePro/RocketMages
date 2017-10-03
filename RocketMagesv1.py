print("[!]Importing...")


import time
import random
import pygame
import sys
from pygame.locals import *
import tkinter
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter import *
import tkinter as tk
import datetime
import os


print("[!]Loading game data...")
main = Tk()

print("[!]Finalizing...")
main.wm_title("RocketMages launcher")

try:
    with open("screensettings","r") as settings:
        settings_string_screen = str(settings.read())
        if settings_string_screen 0 <=:
            screen_dimensions = int(settings_string_screen)
except:
    screen_dimensions = (1920,1080)


def Launcher():
    

