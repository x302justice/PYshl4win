import os,sys

global ops
ops = sys.platform
print(os)

if ops == "win32":
    os.system("systeminfo")
    os.system("echo look as much as you want")

elif ops == "win64":
    os.system("systeminfo")
    os.system("echo look as much as you want")
    
else ops == "Linux"
    os.system("uname")
    os.system("lscpu")
    os.system("sudo lshw")
