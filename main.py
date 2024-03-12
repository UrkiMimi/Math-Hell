# Import libraries 
import tkinter as tk
import subprocess
from time import sleep

# Make notepad rape thing but launch calc instead of notepad
def executeCalc():
    while True:
        subprocess.Popen("calc", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sleep(0.01)


# =====Window shenanigans start here=====

# Initalize window
window = tk.Tk()
window.geometry('400x250')
window.title('Math Hell')

# Make main window frame
mainFrame = tk.Frame(window, pady=45)
mainFrame.pack()

# Set title label
titleLabel = tk.Label(mainFrame, text='Math hell', font=('Comic Sans MS', 25))
titleLabel.pack()
smallTitleLabel = tk.Label(mainFrame, text='holy shit a clone of notepad rape \nwritten by urki', compound='top')
smallTitleLabel.pack(pady=20)

# Start button
startButton = tk.Button(mainFrame, text='Destroy my pc with calculators', command=lambda:executeCalc())
startButton.pack()


# loop window
window.mainloop()