import tkinter as tk
import random

def clearWindow():
    for child in window.winfo_children():
        #print(child)
        child.destroy()
    return

def createExitButton(padding=10):
    exitButton = tk.Button(window, text = "Exit", command=window.destroy)
    exitButton.pack(pady=padding)
    return

def createReturnButton(padding=10):
    returnButton = tk.Button(window, text="Return", command=initHub)
    returnButton.pack(pady=padding)
    return

def initRandom():
    clearWindow()
    randomLabel = tk.Label(window, text=f"{random.randint(1,100000000000000)}")
    randomLabel.pack(pady=5)
    createReturnButton(5)
    createExitButton(5)
    return

def initHub():
    clearWindow()
    label = tk.Label(window, text="Choose which function you would like to access")
    label.pack(pady=20)

    randomButton = tk.Button(window, text="Click this for something random", command=initRandom)
    randomButton.pack()

    createExitButton()
    return

window = tk.Tk()
window.title("Swiss Army Knife")

initHub()

window.mainloop()