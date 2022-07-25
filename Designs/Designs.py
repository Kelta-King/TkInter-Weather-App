from tkinter import font
import tkinter as tk
import tkinter.font as font

class Designs:

    def __init__(self, actions) -> None:
        self.window = tk.Tk()
        self.frame_up = tk.Frame(self.window, width=700, bg="white")
        self.frame_down = tk.Frame(self.window, width=700, bg="white")
        self.city = tk.StringVar()
        self.city_name = tk.StringVar()
        self.temperature = tk.StringVar()
        self.weather = tk.StringVar()
        self.actions = actions     

    def define_window(self):
        self.window.title("Kelta Weather App")
        self.window.configure(bg='#87CEFA')
        
        photo = tk.PhotoImage(file = "Media/icon.png")
        self.window.iconphoto(False, photo)
        self.window.minsize(width=800, height=400)


    def top_frame(self):
        
        # Entry box
        entry = tk.Entry(self.frame_up, textvariable=self.city, font=('Arial', 13), borderwidth=0, width=40)
        entry.grid(row = 0, column = 0, padx=(5,0))
        entry.focus()

        # Submit button
        myFont = font.Font(weight="bold")
        submit_btn = tk.Button(self.frame_up, text="Enter", font=('Arial', 13), 
                bg='#87CEFA', foreground='#ffffff', borderwidth=0, command=lambda: self.handler())
        submit_btn['font'] = myFont

        submit_btn.grid(row = 0, column = 1, padx=(10,5), pady=(4,4))

        self.frame_up.pack(pady=(10,5))

    def bottom_frame(self):
        # City name
        label_city = tk.Label(self.frame_down, bg="white", text="City", font=("Arial", 13), width=24)
        label_city.grid(row=0, column=0, pady=(20,4))
        
        label_city_value = tk.Label(self.frame_down, bg="white", textvariable=self.city_name, font=("Arial", 13), width=24)
        label_city_value.grid(row=0, column=1, pady=(20,4))

        # Temperature 
        label_temp = tk.Label(self.frame_down, bg="white", text="Temperature", font=("Arial", 13), width=24)
        label_temp.grid(row=1, column=0, pady=(4,4))
        
        label_temp_value = tk.Label(self.frame_down, bg="white", textvariable=self.temperature, font=("Arial", 13), width=24)
        label_temp_value.grid(row=1, column=1, pady=(4,4))

        # Humidity 
        label_weather = tk.Label(self.frame_down, bg="white", text="Weather", font=("Arial", 13), width=24)
        label_weather.grid(row=2, column=0, pady=(4,20))
        
        label_weather_value = tk.Label(self.frame_down, bg="white", font=("Arial", 13), width=24, textvariable=self.weather)
        label_weather_value.grid(row=2, column=1, pady=(4,20))

        # Packing the frame down
        self.frame_down.pack(fill=None, pady=(10,5), expand=False)

    def handler(self):
        res = self.actions.getWeather(self.city.get())
        self.city_name.set(res[0])
        self.temperature.set(res[1])
        self.weather.set(res[2])

    def execute(self):
        tk.mainloop()

    