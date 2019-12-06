import os
def pkg(self):
    pkg = input("name of package to install: ")
    dist = input("distro name here")
    if dist == 'ubuntu' or 'mint' or 'debian':
        os.system("sudo apt-get install " + pkg)
    input()

def pip(self):
    pip = input("name of pip thing here:")
    os.system("pip install " + pip)
