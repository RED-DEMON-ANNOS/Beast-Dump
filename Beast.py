import os,platform
os.system('git pull')
 
ass=platform.architecture()[0]
if ass=="32bit":
    print("Please Wait For Next Update")
elif ass=="64bit":
    __import__("dump").main_menu()
