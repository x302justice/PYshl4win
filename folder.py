import os
import sys
os1 = sys.platform
def make(self):
    folder_name = input("Name your new folder here: ")
    os.mkdir(folder_name)
    
def explore(self):
    if sys.platform == 'linux':
        os.system("ls")
    else:
        os.system("DIR")
    dest_folder = input("what folder do you want to go in to?(case sensitive)")
    if os1 == win32:
        if  dest_folder == 'C:' or 'c:' or 'c' or 'C':
            os.system("C:")
        else:
            os.system("cd" + dest_folder)
