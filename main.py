from Database import History as h
import tkinter as tk
from Designs import *

def main():
    
    window = tk.Tk()

    window.title("Kelta Weather App")
    window.configure(bg='#87CEFA') 
    photo = tk.PhotoImage(file = "Media/icon.png")

    window.iconphoto(False, photo)
    window.minsize(width=600, height=400)

    tk.mainloop()


if __name__=="__main__":
    main()