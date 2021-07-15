from View import *
import tkinter
from tkinter import ttk
#from scrape import *

class Controller(object):
    def __init__(self):
        self.view = View()

    def clear_box_text(self):
        return self.view.textbox.delete("1.0","end")

    def main():
        root = tk.Tk()
        view = View(root)
        root.mainloop()

if __name__ == "__main__":
    Controller.main()
        
