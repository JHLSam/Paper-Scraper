import urllib.request
import io
from PIL import Image
import pytesseract as pyt
import wand
from wand.image import Image as wi
import cv2
from screencap import *
import os

"""
URL = input("Enter URL(e.g www.abc.com):" + " ")
urltest = "https://www.google.com"
DRIVER_PATH =  os.getcwd() "/chromedriver"
screencap(DRIVER_PATH,"https://" + URL,"screenshot.png")
"""

class OCR(object):
    def __init__(self,URL,screenshot_name):
        #Initialize with URL of webpage and chosen name of webpage screenshot file
        self.URL = URL
        self.screenshot_name = screenshot_name
    """
    def input_path(self, path):
        self.path = input(path)
        return self.path
        """
    
    def url_to_png(self, DRIVER_PATH):
        local_path = os.getcwd() + "/chromedriver"
        self.DRIVER_PATH = local_path
        return screencap(self.DRIVER_PATH, "https://" + self.URL, self.screenshot_name)

    def locate_screenshot_file(self):
        if i in os.path().

    def text_recognition(self):
        """
        Apply OCR to image file
        """
               
    def text_search(self):
        pass

def getURL():
    stream = urllib.request.urlopen(URL)
    text = stream.read().decode('utf-8')
    stream.close()
    return text

def getText():
    """
    Read & Return text in file

    """
    fd = open('test.html', 'r')
    text = fd.read()
    fd.close()
    return text

def find(substr, string, start):
    """Return the position of the first substr in string, starting from start.
    Return None if not found

    Parameters:
        substr(str): substring being searched for
        string(str): string being searched
        start(str): index where the search begines

    Return:
        int: index where substr is found within string
    """
    pos = start
    size = len(substr)
    while pos < len(string):
        if substr == string[pos:pos+size]:
            return pos
        pos += 1
    return None

"""
#text = getText()
text2 = getURL()
heading_index = find("E-commerce training site", text2, 0)
if heading_index is None:
    print("Heading not found")
else:
    room_index = find("Room:", text2, heading_index)
    if room_index is None:
        print("Room not found")
    else:
        tag_index = find("<", text2, room_index)
        if tag_index is None:
            print("tag not found")
        else:
            print(text2[room_index+6:tag_index])
"""
