import os,platform
os.system('git pull')
 
ass=platform.architecture()[0]
if ass=="32bit":
    __import__("dnx").main()
elif ass=="64bit":
    __import__("anu").main()
