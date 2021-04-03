import tkinter as tk
from tkinter import ttk
#import Controller as Controller
#import Model as model

class View(object):
    def __init__(self,master):
        self.master = master
        #self.label = tk.Label(self.master,text="hello")
        #self.label.pack(padx=10,pady=10)
        self.master.title("Web Crawler")
        self.master.geometry("600x400") #fixed window size
        self.create_label("Enter Websites:(e.g. www.google.com,www.yahoo.com,...)",0,0)
        self.create_button("Submit")
        self.create_button("Clear")
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
        
        self.textbox.pack()

    def create_Vscrollbar(self):
        self.Vscroll = tk.Scrollbar(self.master,bd=3,highlightbackground="blue"
                                    ,jump=0,orient="vertical",width=30)
        self.Vscroll.config(command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.Vscroll.set)
        self.Vscroll.pack(side="right",fill="x")
        #self.Vscroll.place(bordermode="inside")
        
    def widget_pos(self,x,y):
        self.x = x
        self.y = y
        return [self.x,self.y]

    def create_button(self,text):
        self.text = text
        self.button = tk.Button(self.master,text=self.text)
        self.button.pack()
        
        
def main():
    root = tk.Tk()
    view = View(root)
    #root.create_button("hi")
    root.mainloop()
       
if __name__ == "__main__":
    main()

    
        
