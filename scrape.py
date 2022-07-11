#!/usr/bin/env python3.6
import screencap
import urllib.request
import requests
import io
from PIL import Image
import pytesseract
import wand
from wand.image import Image as wi
import cv2
from screencap import *
import os
import pytesseract
import codecs
import sys


print(sys.version)

URL = input("Enter URL(e.g www.abc.com):" + " ")
urltest = "https://www.google.com"
DRIVER_PATH =  os.getcwd() + "/chromedriver"
screencap(DRIVER_PATH,"https://" + URL,"screenshot.png")

class OCR(object):

    #pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract' 

    def __init__(self,URL,screenshot_name):
        ###e.g a = OCR("www.google.com","screenshots.png")
        #Initialize with URL of webpage and chosen name of webpage screenshot file
        self.URL = URL
        self.screenshot_name = screenshot_name
    
    def url_to_png(self):
        self.DRIVER = os.getcwd() + "/chromedriver"
        return screencap(self.DRIVER, "https://" + self.URL, self.screenshot_name)

    def locate_screenshot_file(self):
        self.dir = os.getcwd() + "/Screenshots_storage/"
        self.file = self.dir + self.screenshot_name
        return self.file

    def text_recognition(self):
        """
        Apply OCR to image file
        """
        ocr_text = pytesseract.image_to_string(Image.open(self.locate_screenshot_file()))
        fp = open("test.txt", "w")
        fp.write(ocr_text)
        fp.close

    def text_search(self):
        fd = codecs.open("test.txt",mode="r",encoding="utf-8")
        text = fd.readlines().strip()
        fd.close()
        arr = []
        for lines in text:
            lines.strip()
            arr.append(lines)
        print(arr)

    def main():
        pass

"""
TBC - substring search feature
"""
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