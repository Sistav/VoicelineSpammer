#By Georgios Dialynas-Vatsis
#Upload Date 2020-05-25
from ahk import AHK
import threading
import tkinter as tk

root = tk.Tk()
root.geometry("170x170")
root.title("")
root.resizable(False, False)

ahk = AHK()
stop = False
seconds = 1
selection = ""
hotkey = "-"

PRE_OPTIONS = ["Letters", "Numbers", "Symbols","Function Keys"]
LETTERS = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
NUMBERS = ["1","2","3","4","5","6","7","8","9","0"]
SYMBOLS = ["`","-","=","[","]",";",",",".","/","*",]
FUNCTION = ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12",]

pre_options = tk.StringVar(root)
pre_options.set(PRE_OPTIONS[2])
options = tk.StringVar(root)
options.set(SYMBOLS[7])

def callback(event=None):
    global options
    global selection
    if pre_options.get() == "Letters":
        grid_remove(LETTERS)
    elif pre_options.get() == "Numbers":
        grid_remove(NUMBERS)
    elif pre_options.get() == "Symbols":
        grid_remove(SYMBOLS)
    elif pre_options.get() == "Function Keys":
        grid_remove(FUNCTION)
    pass
def grid_remove(LIST):
        global selection
        selection.grid_remove()
        options.set(LIST[0])
        selection = tk.OptionMenu(root, options, *LIST)
        selection.grid(row=4,column=1)
def spammer():
    global stop
    global seconds
    global hotkey
    print(ahk.key_state(hotkey))
    if stop == False and not ahk.key_state(hotkey):
        button = options.get()
        ahk.key_press(button)
        threading.Timer(seconds, spammer).start()
    else:
        stop = True
def make_true():
    global stop
    global seconds
    global hotkey
    stop = False
    seconds = float(speed_entry.get())
    hotkey = hotkey_entry.get()
    spammer()
def stop():
    global stop
    stop = True

pre_selection = tk.OptionMenu(root, pre_options, *PRE_OPTIONS, command=callback)
pre_selection.grid(row=3,column=1)
selection = tk.OptionMenu(root, options, *SYMBOLS)
selection.grid(row=4,column=1)
speed_text =tk.Label(text='How Fast (Seconds)')
speed_text.grid(row=1,column=1)
speed_entry = tk.Entry(root, width=10,)
speed_entry.grid(row=2,column=1)
blank_text =tk.Label(text='     ')
blank_text.grid(row=1,column=2)
hotkey_text =tk.Label(text='Hotkey')
hotkey_text.grid(row=5,column=1)
hotkey_entry = tk.Entry(root, width=10,)
hotkey_entry.grid(row=6,column=1)
start_button = tk.Button(root, text="Start", command=make_true)
start_button.grid(row=1,column=3)
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.grid(row=5,column=3)

# button = input("Please Input the voice line button\n")
# seconds = float(input("\nPlease how often you want the buttons to spam\n"))
# threading.Timer(seconds, spammer()).start()

root.mainloop()