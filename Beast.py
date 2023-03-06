import os,platform
os.system('git pull')
 
ass=platform.architecture()[0]
if ass=="32bit":
    __import__("dn").main()
elif ass=="64bit":
    __import__("ana").main()
