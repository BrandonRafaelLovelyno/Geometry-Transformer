import tkinter as tk

# declaring constants
dots_coords=[]
cartesian_grid_length=50
final_cartesian_coord=5000
center_coord_x=500
center_coord_y=500

# main canvas config function
def draw_cartesian_grid():
    for i in range(-final_cartesian_coord, final_cartesian_coord, cartesian_grid_length): 
        # drawing the grid lines
        main_canvas.create_line(i, -final_cartesian_coord-1, i, final_cartesian_coord+1, fill="lightgray", dash=(2, 2)) 
        main_canvas.create_line(-1*final_cartesian_coord-1, i, final_cartesian_coord+1, i, fill="lightgray", dash=(2, 2)) 
        
        # adding grid number
        main_canvas.create_text(i,center_coord_y+20,text=(str(-i+500)),fill="black")
        main_canvas.create_text(center_coord_x+20,i,text=(str(-i+500)),fill="black")
        
def draw_cartesian_axes():
    main_canvas.create_line(center_coord_x,center_coord_y, final_cartesian_coord+1, center_coord_y, arrow=tk.LAST)
    main_canvas.create_line(center_coord_x,center_coord_y, -1*final_cartesian_coord,center_coord_y, arrow=tk.LAST)
    main_canvas.create_line(center_coord_x,center_coord_y, center_coord_x, -1*final_cartesian_coord-1, arrow=tk.LAST)
    main_canvas.create_line(center_coord_x,center_coord_y, center_coord_x, final_cartesian_coord+1, arrow=tk.LAST)
   
#  maincanvas event listener
def on_press(event):
    x,y=event.x,event.y
    relative_x,relative_y=x-center_coord_x,y-center_coord_y
    main_canvas.create_oval(x-2,y-2,x+2,y+2,fill='black')
    dots_coords.append((relative_x,relative_y))
    
    
    if(len(dots_coords)>=2):
        start_x,start_y=dots_coords[-2]
        end_x,end_y=dots_coords[-1]
        main_canvas.create_line(start_x+center_coord_x,start_y+center_coord_y,end_x+center_coord_x,end_y+center_coord_y)
        
def open_transform_options():
    transform_window = tk.Toplevel(root)
    transform_window.title("Transform Options")

    transform_options = ["Translate", "Rotate", "Scale", "Shear"]
    for option in transform_options:
        tk.Button(transform_window, text=option).pack()

# scroll bar canvas config function
def draw_scrollbar():
    
    right_frame = tk.Frame(root)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    x_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL,command=main_canvas.xview)
    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    y_scrollbar = tk.Scrollbar(right_frame, orient=tk.VERTICAL,command=main_canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    main_canvas.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

# main function

# initializing the tkinter window
root = tk.Tk()
root.title("Geometry Transformer")

# initializing the main frame
frame= tk.Frame(root)
frame.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

# initializing the main canvas
main_canvas=tk.Canvas(frame,width=100, height=100)
main_canvas.pack(fill=tk.BOTH, expand=True)

# preparing the main canvas
draw_cartesian_grid()
draw_cartesian_axes()

# preparing the scrollbar canvas
draw_scrollbar()

# attaching main canvas event listener
main_canvas.bind('<ButtonPress-1>', on_press)

root.mainloop()