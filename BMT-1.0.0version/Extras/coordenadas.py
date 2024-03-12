import tkinter as tk
window = tk.Tk()
window.config(highlightbackground='#000000')
canvas = tk.Canvas(window, width=100, height=100, background='#000000')
canvas.pack()
label = tk.Label(canvas,borderwidth=0,bg='#000000')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','#000000')
window.wm_attributes('-topmost', True)
canvas.create_window(0, 0, anchor=tk.NW, window=label)
tk.mainloop()