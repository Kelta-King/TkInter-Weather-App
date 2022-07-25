from tkinter import font
from matplotlib.pyplot import margins
from Database import History as h
import tkinter as tk
from Designs import *
import tkinter.font as font

def main():
    
    window = tk.Tk()

    window.title("Kelta Weather App")
    window.configure(bg='#87CEFA')
    
    photo = tk.PhotoImage(file = "Media/icon.png")
    window.iconphoto(False, photo)
    window.minsize(width=800, height=400)

    # Up frame to have Entry box and button 
    frame_up = tk.Frame(window, width=700, bg="white")

    city = tk.StringVar()
    entry = tk.Entry(frame_up, textvariable=city, font=('Arial', 13), borderwidth=0, width=40)
    entry.grid(row = 0, column = 0, padx=(5,0))

    myFont = font.Font(weight="bold")
    submit_btn = tk.Button(frame_up, text="Enter", font=('Arial', 13), 
            bg='#87CEFA', foreground='#ffffff', borderwidth=0)
    submit_btn['font'] = myFont

    submit_btn.grid(row = 0, column = 1, padx=(10,5), pady=(4,4))

    frame_up.pack(pady=(10,5))

    # Down frame to have Output box
    frame_down = tk.Frame(window, width=700, bg="white")

    # City name
    label_city = tk.Label(frame_down, bg="white", text="City", font=("Arial", 13), width=24)
    label_city.grid(row=0, column=0, pady=(20,4))
    city = tk.StringVar()
    label_city_value = tk.Label(frame_down, bg="white", textvariable=city, font=("Arial", 13), width=24)
    label_city_value.grid(row=0, column=1, pady=(20,4))

    # Temperature 
    label_temp = tk.Label(frame_down, bg="white", text="Temperature", font=("Arial", 13), width=24)
    label_temp.grid(row=1, column=0, pady=(4,4))
    temperature = tk.StringVar()
    label_temp_value = tk.Label(frame_down, bg="white", textvariable=temperature, font=("Arial", 13), width=24)
    label_temp_value.grid(row=1, column=1, pady=(4,4))

    # Humidity 
    label_hum = tk.Label(frame_down, bg="white", text="Humidity", font=("Arial", 13), width=24)
    label_hum.grid(row=2, column=0, pady=(4,20))
    humidity = tk.StringVar()
    label_hum_value = tk.Label(frame_down, bg="white", font=("Arial", 13), width=24, textvariable=humidity)
    label_hum_value.grid(row=2, column=1, pady=(4,20))

    frame_down.pack(fill=None, pady=(10,5), expand=False)

    tk.mainloop()


if __name__=="__main__":
    main()