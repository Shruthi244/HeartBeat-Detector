#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Flask installation


# In[ ]:


from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return"Welcoming you all to this interesting application"

@app.route('/hello')
def hello():
    return"Hello world"

@app.route('/html')
def html():
    return render_template("new.html")

@app.route('/ipynb')
def ipynb():
    return render_template("detect.ipynb")

@app.route('/detect')
def detect():
    import numpy as np
    from matplotlib import pyplot as plt
    import cv2
    import io
    import time
    # Camera stream
    #from tkinter import tkinter as Tk
 
    # Following will import tkinter.ttk module and
    # automatically override all the widgets
    # which are present in tkinter module.
    from tkinter.ttk import tkinter
 
    # Create Object
    root = Tk()
 
    # Initialize tkinter window with dimensions 100x100            
    root.geometry('100x100')    
 
    btn = Button(root, text = 'Detect heartbeat',
                    command = root.destroy)
     
    # Set the position of button on the top of window
    btn.pack(side = 'top')    
 
    root.mainloop()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    # cap = cv2.VideoCapture("video.mp4")
    # Image crop
    x, y, w, h = 800, 500, 100, 100
    x, y, w, h = 950, 300, 100, 100
    heartbeat_count = 128
    heartbeat_values = [0]*heartbeat_count
    heartbeat_times = [time.time()]*heartbeat_count
    # Matplotlib graph surface
    fig = plt.figure()
    ax = fig.add_subplot(111)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        crop_img = img[y:y + h, x:x + w]
        # Update the data
        heartbeat_values = heartbeat_values[1:] + [np.average(crop_img)]
        heartbeat_times = heartbeat_times[1:] + [time.time()]
        # Draw matplotlib graph to numpy array
        ax.plot(heartbeat_times, heartbeat_values)
        fig.canvas.draw()
        plot_img_np = np.fromstring(fig.canvas.tostring_rgb(),
                                    dtype=np.uint8, sep='')
        plot_img_np = plot_img_np.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.cla()
        # Display the frames
        cv2.imshow('Crop', crop_img)
        cv2.imshow('Graph', plot_img_np)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    app.run()
