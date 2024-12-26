import tkinter as tk
from tkinter import Menu

# create main window
root = tk.Tk()
root.title("menu bar created by suling chu")
root.geometry("500x300")

#create a menu bar
menub = Menu(root)
root.config(menu=menub)

def newfile():
    print("you have clicked the New File option unfortunetaly we cannot make a New File at this momment")

def openfile():
    print("you have clicked the Open File option unfortunetaly we cannot Open File at this momment")

def save():
    print("you have clicked the Save option unfortunetaly we cannot Save at this momment")

#creating file menu
file_menu = Menu(menub)
file_menu.add_command(label = "New File",command = newfile)
file_menu.add_command(label = "Open File",command = openfile)
file_menu.add_command(label = "Save",command = save)

#add a separating line
file_menu.add_separator()
file_menu.add_command(label = "Exit",command = root.quit)

menub.add_cascade(label = "File",menu = file_menu)

# creating edit file
edit_menu = Menu(menub)
edit_menu.add_command(label = "Cut")

edit_menu.add_separator()

edit_menu.add_command(label = "Find")
edit_menu.add_command(label = "Replace")

menub.add_cascade(label = "Edit",menu = edit_menu)

root.mainloop()