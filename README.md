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
This guide was written on the assumption that you work for android on odroid-xu3/4 and have the android NDK and host system is ubuntu 14.04.
You can download the ndk from here ->  https://developer.android.com/ndk/downloads/index.html

0. install basic stuff

$ sudo apt-get update
$ sudo apt-get install cmake liblockdev1-dev libudev-dev libxrandr-dev python-dev swig git

1. export NDK path

$ export ANDROID_NDK=/path/to/the/android/ndk/

2. download android cmake toolchains

$ mkdir ~/libcec
$ cd ~/libcec
$ git clone https://github.com/taka-no-me/android-cmake

3. build & install platform stuff

$ cd ~/libcec
$ git clone https://github.com/Pulse-Eight/platform
$ mkdir platform/build
$ cd platform/build
$ cmake -DCMAKE_TOOLCHAIN_FILE=../../android-cmake/android.toolchain.cmake \
-DCMAKE_INSTALL_PREFIX:PATH=~/libcec/lib/platform/ -DANDROID_ABI="armeabi-v7a with NEON" \
-DANDROID_STL=gnustl_static -DANDROID_TOOLCHAIN_NAME=arm-linux-androideabi-4.9 ..
$ make install -j4

4. build & install libcec

$ cd ~/libcec
$ git clone https://github.com/Pulse-Eight/libcec
$ mkdir libcec/build
$ cd libcec

4.1 remove (or make it be comment) a line for using exynos api

$ vi src/libcec/cmake/CheckPlatformSupport.cmake

remove a line number 30 -> set(HAVE_EXYNOS_API 0)


4.2 Add two lines to CMakeList.txt (for 5.0)

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIE -pie")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIE -pie")

$ vi CMakeLists.txt


4.3 compile and build it

$ cd ~/libcec/libcec/build
$ cmake -DCMAKE_TOOLCHAIN_FILE=../../android-cmake/android.toolchain.cmake \
-DCMAKE_INSTALL_PREFIX:PATH=~/libcec/lib/libcec -DANDROID_ABI="armeabi-v7a with NEON" \
-DANDROID_STL=gnustl_static -DANDROID_TOOLCHAIN_NAME=arm-linux-androideabi-4.9 \
-DCMAKE_PREFIX_PATH=~/libcec/lib/platform/ -DHAVE_EXYNOS_API=1 ..
$ make install -j4

5. push libcec library and binary to odroid-xu3/xu4 by adb
5.1 remount odroid file system

$ adb shell mount -o remount,rw /

5.2 push library and binary

$ cd ~/libcec/lib/libcec
$ adb push ./lib /lib
$ adb push ./bin /bin

6. run libcec. (it run in odroid-xu3/xu4 by console)

$ cec-client

screenshot (it be connenct to lg
