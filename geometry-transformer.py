import tkinter as tk

dots_coords=[]

def on_press(event):
    x,y=event.x,event.y
    canvas.create_oval(x-2,y-2,x+2,y+2,fill='black')
    dots_coords.append((x,y))
    
    if(len(dots_coords)>=2):
        start_x,start_y=dots_coords[-2]
        end_x,end_y=dots_coords[-1]
        canvas.create_line(start_x,start_y,end_x,end_y)
        

root = tk.Tk()
root.title("Geometry Transformer")

frame= tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

canvas=tk.Canvas(frame, width=400, height=400)
canvas.pack(fill=tk.BOTH, expand=1)

canvas.bind('<ButtonPress-1>', on_press)

root.mainloop()