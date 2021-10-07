import tkinter as tk
from tkinter import ttk
import sys
#from Controller import *
import Controller 
#import numpy as np
#!/usr/bin/env python3.6

print(tk.TkVersion)
print(sys.version)

class View(object):
    
    def __init__(self,master):
        self.master = master
        #self.controller = Controller()
        self.master.title("Web Crawler")
        self.master.geometry("600x400") #fixed window size
        self.create_label("Enter Websites:(e.g. www.google.com,www.yahoo.com,...)",0,0)
        self.create_button("Submit","top",command=self.get_textbox_text)
        self.create_button("Clear","top",command=self.clear_box_text)
        self.create_button("Close","bottom",command=self.master.destroy)
        self.create_textbox()
        self.create_Vscrollbar()

    def create_label(self,text,xpad,ypad):
        self.text = text
        self.xpad = xpad
        self.ypad = ypad
        self.label = tk.Label(self.master,text=self.text)
        self.label.pack(padx=self.xpad,pady=self.ypad)

    def create_textbox(self):
        self.textbox = tk.Text(self.master,bd=2,height=20,width=50,highlightbackground="black",font=("calibri",10,
                                                                            "bold"),insertborderwidth=4)
        self.textbox.pack(side="left",padx=60)
        
    def get_textbox_text(self):
        arr = []
        for i in self.textbox.get("1.0","end-1c").split(","):
            if i[0:4] == "www." and i[-4::] == ".com":
                arr.append(i)
        print(arr)
    
    def clear_box_text(self):
        return self.textbox.delete("1.0","end")
        
    def create_Vscrollbar(self):
        self.Vscroll = tk.Scrollbar(self.master,bd=3,highlightbackground="blue"
                                    ,jump=0,orient="vertical")
        self.Vscroll.config(command=self.textbox.yview)         #hook scrollbar to textbox      
        self.textbox.config(yscrollcommand=self.Vscroll.set)
        self.Vscroll.pack(side="right",fill="y")
        #self.Vscroll.place(bordermode="inside")
        
    def widget_pos(self,x,y): #unused helper fx
        self.x = x
        self.y = y
        return [self.x,self.y]

    def create_button(self,text,side,command):
        self.text = text
        self.side = side
        self.command = command
        self.button = tk.Button(self.master,text=self.text,command=self.command,bg="white",activebackground="blue")
        self.button.pack(side=self.side)

    def main():
        root = tk.Tk()
        view = View(root)
        root.resizable(0,0) #Do not permit resize of window
        root.mainloop() #main window frame/parent window/"master" for View(master)
        
if __name__ == "__main__":
    View.main()

    
        
