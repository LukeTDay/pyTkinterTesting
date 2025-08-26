import tkinter as tk

window = tk.Tk()
label = tk.Label(window, text = "Hello World")
label.pack()

button = tk.Button(window, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()


window.title("Test Application")
window.geometry("400x400")

window.mainloop()
