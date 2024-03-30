import tkinter as tk

# declaring transformation class
class Rotation:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

class Translation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Scaling:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        
class Shearing:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Mirror:
    def __init__(self, axis,x,y):
        self.axis = axis
        self.x=x
        self.y=y 

# declaring constants
cartesian_grid_length=50
final_cartesian_coord=5000
center_coord_x=500
center_coord_y=500

# declaring global variables
transformation_query=[]
dots_coords=[]

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

# transformation interface

def open_transform_selection_window():
    transform_selection_window = tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    center_window(transform_selection_window)
    transform_selection_window.title("Transform Options")
    
    transform_query_window=tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    center_window(transform_query_window)
    
    global transformation_query_list
    transformation_query_list=tk.Listbox(transform_query_window)
    transformation_query_list.pack(side='top',anchor='center',pady=10)

    transform_options_text = ["Translate", "Rotate", "Scale", "Shear","Mirror"]
    transform_options_command = [open_translation, open_rotation, open_scaling, open_shearing,open_mirror]
    for text,command in zip(transform_options_text,transform_options_command):
        tk.Button(transform_selection_window, text=text,command=command,bg='red',fg='white',font='Arial 12').pack(side='top',anchor='center',pady=10)
        
def open_rotation():
    rotation_window = tk.Toplevel(root,height=200,width=400,padx=20,pady=10)
    rotation_window.title("Rotation")
    center_window(rotation_window)
    
    # X Center Coordinate
    x_label = tk.Label(rotation_window, text="Rotation X Coordinate:")
    x_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    
    x_entry=tk.Entry(rotation_window)
    x_entry.grid(row=0,column=1,padx=10,pady=5,sticky=tk.W)
    
    
    # Y Center Coordinate
    y_label=tk.Label(rotation_window,text="Rotation Y Coordinate:")
    y_label.grid(row=1,column=0,padx=10,pady=5,sticky=tk.W)
    
    y_entry=tk.Entry(rotation_window)
    y_entry.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Rotation Angle
    angle_label = tk.Label(rotation_window, text="Rotation Angle:")
    angle_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    
    angle_entry=tk.Entry(rotation_window)
    angle_entry.grid(row=2,column=1,padx=10,pady=5,sticky=tk.W)

    # Create a button to submit input
    submit_button=tk.Button(rotation_window,text="Submit",command=lambda: submit_rotation(float(x_entry.get()),float(y_entry.get()),float(angle_entry.get())),bg='blue',fg='white',font='Arial 12')
    submit_button.grid(row=3,column=0,columnspan=2,pady=10)
        
def open_translation():
    translation_window =  tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    translation_window.title("Translation")
    center_window(translation_window)
    
     # X Center Coordinate
    x_label = tk.Label(translation_window, text="Translation X :")
    x_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    
    x_entry=tk.Entry(translation_window)
    x_entry.grid(row=0,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Y Center Coordinate
    y_label=tk.Label(translation_window,text="Translation Y :")
    y_label.grid(row=1,column=0,padx=10,pady=5,sticky=tk.W)
    
    y_entry=tk.Entry(translation_window)
    y_entry.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Create a button to submit input
    submit_button=tk.Button(translation_window,text="Submit",command=lambda: submit_translation(float(x_entry.get()),float(y_entry.get())),bg='blue',fg='white',font='Arial 12')
    submit_button.grid(row=3,column=0,columnspan=2,pady=10)
    
def open_scaling():
    scaling_window= tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    scaling_window.title("Scaling")
    center_window(scaling_window)
    
    # X factor
    x_label = tk.Label(scaling_window, text="Scaling factor X :")
    x_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    
    x_entry=tk.Entry(scaling_window)
    x_entry.grid(row=0,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Y factor
    y_label=tk.Label(scaling_window,text="Scaling factor Y :")
    y_label.grid(row=1,column=0,padx=10,pady=5,sticky=tk.W)
    
    y_entry=tk.Entry(scaling_window)
    y_entry.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Create a button to submit input
    submit_button=tk.Button(scaling_window,text="Submit",command=lambda: submit_scaling(float(x_entry.get()),float(y_entry.get())),bg='blue',fg='white',font='Arial 12')
    submit_button.grid(row=3,column=0,columnspan=2,pady=10)
    
def open_shearing():
    shearing_window= tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    shearing_window.title("Shearing")
    center_window(shearing_window)
    
    # X factor
    x_label = tk.Label(shearing_window, text="Shearing factor X :")
    x_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    
    x_entry=tk.Entry(shearing_window)
    x_entry.grid(row=0,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Y factor
    y_label=tk.Label(shearing_window,text="Shearing factor Y :")
    y_label.grid(row=1,column=0,padx=10,pady=5,sticky=tk.W)
    
    y_entry=tk.Entry(shearing_window)
    y_entry.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Create a button to submit input
    submit_button=tk.Button(shearing_window,text="Submit",command=lambda: submit_shearing(float(x_entry.get()),float(y_entry.get())),bg='blue',fg='white',font='Arial 12')
    submit_button.grid(row=3,column=0,columnspan=2,pady=10)
    
    
def open_mirror():
    mirror_window= tk.Toplevel(root,height=300,width=300,padx=10,pady=10)
    mirror_window.title("Mirror")
    center_window(mirror_window)
    
    # Axis
    axis_label=tk.Label(mirror_window,text="Axix (x or y) :")
    axis_label.grid(row=0,column=0,padx=10,pady=5,sticky=tk.W)
    
    axis_entry=tk.Entry(mirror_window)
    axis_entry.grid(row=0,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Coordinate 
    coordinate_label=tk.Label(mirror_window,text="Coordinate :")
    coordinate_label.grid(row=1,column=0,padx=10,pady=5,sticky=tk.W)
    
    coordinate_entry=tk.Entry(mirror_window)
    coordinate_entry.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)
    
    # Create a button to submit input
    submit_button=tk.Button(mirror_window,text="Submit",command=lambda: submit_mirror(axis_entry.get(),float(coordinate_entry.get()),float(coordinate_entry.get())),bg='blue',fg='white',font='Arial 12')
    submit_button.grid(row=2,column=0,columnspan=2,pady=10)

# transformation submit functions
def submit_rotation(x,y,angle):
    rotation = Rotation(x, y, angle)
    transformation_query.append(rotation)
    transformation_query_list.insert(tk.END,"HAI")
    
    
def submit_translation(x,y):
    translation = Translation(x, y)
    transformation_query.append(translation)
    
    
def submit_scaling(x,y,scale):
    scaling = Scaling(x, y, scale)
    transformation_query.append(scaling)

def submit_shearing(x,y):
    shearing = Shearing(x, y)
    transformation_query.append(shearing)

def submit_mirror(axis,x,y):
    mirror = Mirror(axis,x,y)
    transformation_query.append(mirror)
    

# tkinter helper

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# main function

# initializing the tkinter window
root = tk.Tk()
root.title("Geometry Transformer")

# initializing the main frame
frame= tk.Frame(root,width=150, height=150)
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

# attaching transform button
transform_button = tk.Button(frame, text="Transform", command=open_transform_selection_window,bg="blue", fg="white",font='Arial 12')
transform_button.place(x=frame.winfo_width()+100,y=frame.winfo_height()+100, anchor=tk.CENTER)

root.mainloop()