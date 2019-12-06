#dependancy modules are here
import sys
#custom modules to make stuff work goes here
import folder as f
import boot as b
import clear_screen as c
import installer as i
#this is where the actual menu is.
b.boot('')
os = sys.platform
def menu():
    #this is the menu's interface, this is where you select stuff.
    #it looks like spaghetti code, but it's actuallt how i make sense of stuff
    #and how i make it look professional
    c.clr('')
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if os == 'win32':
        print("Base OS: Windows")
    else:
        print("Base OS Linux probably")
        #this is where the spaghetti code ends for now you're welcome
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("1)New Folder")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("2)File Explorer(n/a)")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("3) Package Installer")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("4) pip installer")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #this is the menus if else stuff, this is how the menu works and crap
    option = input("Select option here: ")
    if option == '1':
        f.make('')
        menu()
    elif option == '2':
        print("only available in debug mode")
        menu()
    elif option == '3':
        if os == 'win32':
            print("you're on windows, you can't use it.")
            input()
            menu()
        else:
            i.pkg('')
            menu()
    elif option == '4':
        i.pip('')
        menu()
    elif option == 'set debug mode true':
        f.explore
        input()
        menu()
    else:
        print("error 2124-4007, view support.nintendo.com for more info")
        input()
        menu()
menu()
