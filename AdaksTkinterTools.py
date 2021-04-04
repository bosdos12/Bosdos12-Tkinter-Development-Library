from PIL import ImageTk, Image
import requests
from io import BytesIO
import tkinter as tk

#///////////////////////////////////////////////////////////////////////////////////////////////////////

# This function will be called whenever a web-based image is wanted to be displayed;
# The url of the web hosted image is passed via parameters;
# The function gets the web-hosted image via the requests module, then uses BytesIO to convert it to binary data;
# The Binary data is then converted to an image via PIL module functions [ImageTK and Image];
# The function then returns the image, which can be assigned to a value later;
def TK_WebImage(webImageURL):
	return ImageTk.PhotoImage(Image.open(BytesIO(requests.get(webImageURL).content)))

#///////////////////////////////////////////////////////////////////////////////////////////////////////

# This a class which allows you to create rounded buttons in tkinter, implementation is just like any other tkinter element;
# The required properties are: (parent, width, height, cornerradius, padding, fg, bg, command);
class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, fg, bg,command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg="lightgray")
        self.command = command
        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None
        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None
        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=fg, outline=fg)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=fg, outline=fg)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=fg, outline=fg)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=fg, outline=fg)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=fg, outline=fg)
        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
    def _on_press(self, event):
        self.config(relief="sunken")
    def _on_release(self, event):
        if self.command is not None:
            self.command()

#///////////////////////////////////////////////////////////////////////////////////////////////////////
		
