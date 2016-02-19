import tkinter as tk

lives = 3
root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width=900, height=600, bg='#ffffff')
frame.pack()
canvas.pack()
root.title('Pyong')
root.mainloop()
