# TkInter-Weather-App
Simple Tkinter weather app. It uses Open Weather API to fetch the weather data of a city. Here are the technologies used to build this application.
- Python
- TkInter
- OpenWeather API
- PyInstaller
- auto-py-to-exe

Now to run this project install Python in the system and then simply clone this project though following command. 
```
git clone https://github.com/Kelta-King/TkInter-Weather-App.git
```
Then go to the TkInter-Weather-App folder and run the main.py file
```
cd TkInter-Weather-App
python main.py
```

## How to make EXE file of the application
For that, we will use 2 things
- PyInstaller
- auto-py-to-exe

We can install them both through pip. Below are the commands of it.
```
pip install pyinstaller
pip install auto-py-to-exe
```
After that run the following command. It will open a window in web browser through which we can generate the command for converting .py file to .exe file
```
auto-py-to-exe
```

Then choose the options accordingly and it will generate the command for you. That command is of PyInstaller. Run that command in cmd and you will get your Executable file in dist folder in the cmd directory.

Here is the image of how the application looks

![](https://github.com/Kelta-King/TkInter-Weather-App/blob/main/Media/Weather-App.PNG)
