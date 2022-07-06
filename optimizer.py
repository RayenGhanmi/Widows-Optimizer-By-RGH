import pyglet
import os
import tkinter as tk
from tkinter import*
from tkinter.font import BOLD, ITALIC
import customtkinter
import webbrowser
import platform
import psutil
from PIL import Image, ImageTk
from itertools import count, cycle
from playsound import playsound
pyglet.font.add_file("Data\\zian-7vO4.ttf")
pyglet.font.add_file("Data\\hacked-KerX.ttf")
zian=pyglet.font.load("Zian")
hacked=pyglet.font.load("HACKED")
playsound("Data\\3.mp3",False)
splash=Tk()
splash.overrideredirect(True)
WIDTH=802
HEIGHT=602
screen_width=splash.winfo_screenwidth()
screen_height=splash.winfo_screenheight()
x=(screen_width/2)-(WIDTH/2)
y=(screen_height/2)-((50+HEIGHT)/2)
splash.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im=Image.open(im)
        frames=[]
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames=cycle(frames)
        try:
            self.delay=im.info["duration"]
        except:
            self.delay=100
        if len(frames)==1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
lbl=ImageLabel(splash)
lbl.pack()
lbl.config(bg="#00ddff")
lbl.load("Data\\1.gif")
def main_window():
    splash.destroy()
    def fix():
        playsound("Data\\1.mp3")
        os.system("start /min Data\\14.cmd ^& exit")
    def debloat():
        playsound("Data\\1.mp3")
        os.system("start /min Data\\15.cmd ^& exit")
        os.system("start /min Data\\5.bat ^& exit")
    def optimize():
        playsound("Data\\1.mp3")
        os.system("start /min Data\\2.bat ^& exit")
        os.system("start /min Data\\3.bat ^& exit")
        os.system("start /min Data\\16.cmd ^& exit")
        os.system("start /min Data\\17.cmd ^& exit")
        os.system("start /min Data\\1.bat ^& exit")
    def support():
        playsound("Data\\1.mp3")
        webbrowser.open("https://www.facebook.com/GhanmiRayen22")
    def about():
        playsound("Data\\1.mp3")
        win=customtkinter.CTk()
        win.config(cursor="plus")
        win.configure(fg_color="black")
        win.title("About")
        win.resizable(False, False)
        win.iconbitmap("Data\\ico.ico")
        label=customtkinter.CTkLabel(master=win,text="This is a Windows Optimizer made by RGH\nPlease consider supporting him.",text_color="#00ffbb",text_font=("hacked",15,BOLD))
        label.pack(side=TOP,pady=36)
        WIDTH1=550
        HEIGHT1=130
        x=(screen_width/2)-(WIDTH1/2)
        y=(screen_height/2)-((50+HEIGHT1)/2)
        win.geometry(f"{WIDTH1}x{HEIGHT1}+{int(x)}+{int(y)}")
        win.mainloop()
    def info():
        playsound("Data\\1.mp3")
        root1=customtkinter.CTk()
        root1.config(cursor="plus")
        root1.configure(fg_color="black")
        root1.title("System info")
        root1.resizable(False, False)
        root1.iconbitmap("Data\\ico.ico")
        WIDTH_info=800
        HEIGHT_info=500
        screen_width=root1.winfo_screenwidth()
        screen_height=root1.winfo_screenheight()
        x=(screen_width/2)-(WIDTH_info/2)
        y=(screen_height/2)-((50+HEIGHT_info)/2)
        root1.geometry(f"{WIDTH_info}x{HEIGHT_info}+{int(x)}+{int(y)}")
        label_info=customtkinter.CTkLabel(master=root1,text=f"Computer network name: {platform.node()}",text_color="#e0a66c",text_font=("hacked",25,ITALIC,BOLD))
        label_info.pack()
        label_info1=customtkinter.CTkLabel(master=root1,text=f"Machine type: {platform.machine()}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info1.pack()
        label_info2=customtkinter.CTkLabel(master=root1,text=f"Processor type: {platform.processor()}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info2.pack()
        label_info3=customtkinter.CTkLabel(master=root1,text=f"Number of physical cores: {psutil.cpu_count(logical=False)}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info3.pack()
        label_info4=customtkinter.CTkLabel(master=root1,text=f"Number of logical cores: {psutil.cpu_count(logical=True)}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info4.pack()
        label_info5=customtkinter.CTkLabel(master=root1,text=f"Current CPU frequency: {psutil.cpu_freq().current}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info5.pack()
        label_info6=customtkinter.CTkLabel(master=root1,text=f"Min CPU frequency: {psutil.cpu_freq().min}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info6.pack()
        label_info7=customtkinter.CTkLabel(master=root1,text=f"Max CPU frequency: {psutil.cpu_freq().max}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info7.pack()
        label_info8=customtkinter.CTkLabel(master=root1,text=f"Current CPU utilization: {psutil.cpu_percent(interval=1)}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info8.pack()
        label_info9=customtkinter.CTkLabel(master=root1,text=f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info9.pack()
        label_info10=customtkinter.CTkLabel(master=root1,text=f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info10.pack()
        label_info11=customtkinter.CTkLabel(master=root1,text=f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info11.pack()
        label_info12=customtkinter.CTkLabel(master=root1,text=f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info12.pack()
        label_info13=customtkinter.CTkLabel(master=root1,text=f"RAM usage: {psutil.virtual_memory().percent}%",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info13.pack()
        label_info14=customtkinter.CTkLabel(master=root1,text=f"Operating system: {platform.system()}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info14.pack()
        label_info15=customtkinter.CTkLabel(master=root1,text=f"Operating system version: {platform.version()}",text_color="#7fe3c5",text_font=("hacked",15,BOLD))
        label_info15.pack()
        root1.mainloop()
    window=customtkinter.CTk()
    window.configure(fg_color="black",cursor="plus")
    window.iconbitmap("Data\\ico.ico")
    window.resizable(False, False)
    lbl1=customtkinter.CTkLabel(master=window,text="beta",text_color="#00ddff",text_font=("zian",15))
    lbl1.pack()
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    WIDTH=1024
    HEIGHT=768
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    x=(screen_width/2)-(WIDTH/2)
    y=(screen_height/2)-((50+HEIGHT)/2)
    window.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")
    window.title("RGH Optimizer 2.0")
    label_version=customtkinter.CTkLabel(master=window,text="Welcome To RGH Optimizer 2.0.1",text_color="#9000ff",text_font=("hacked",35),corner_radius=25)
    label_version.pack()
    label=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    label.pack()
    about=customtkinter.CTkButton(master=window,text="About",command=about,fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5,text_font=("hacked",15))
    about.config(width=25,height=25,cursor="plus")
    about.pack(anchor=NE)
    about.config(width=25,height=25)
    info=customtkinter.CTkButton(master=window,text="System info",command=info,fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5,text_font=("hacked",15))
    info.config(width=25,height=25,cursor="plus")
    info.pack(side=TOP,anchor=NW)
    support=customtkinter.CTkButton(master=window,text="Support",command=support,fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5,text_font=("hacked",15))
    support.config(cursor="plus")
    support.pack(side=BOTTOM,anchor=SW)
    label1=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 5))
    label1.pack()
    label=customtkinter.CTkLabel(window,text="\n")
    label.pack()
    button_fix=customtkinter.CTkButton(master=window,text="Fix",command=fix,fg_color="black",border_color="#006b13",hover_color="#006b13",border_width=1.5,text_font=("hacked",20))
    button_fix.config(cursor="plus")
    button_fix.pack()
    labelf=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labelf.pack()
    label_fix=customtkinter.CTkLabel(window,text="Fix: This will fix any windows problem.",text_color="#03df2b",text_font=("Comic Sans MS",15))
    label_fix.pack()
    labelf1=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labelf1.pack()
    button_debloat=customtkinter.CTkButton(master=window,text="Debloat",command=debloat,fg_color="black",border_color="#3c2180",hover_color="#3c2180",border_width=1.5,text_font=("hacked",20))
    button_debloat.config(cursor="plus")
    button_debloat.pack()
    labeld=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labeld.pack()
    label_debloat=customtkinter.CTkLabel(window,text="Debloat: this will remove every built in app.",text_color="#7542f5",text_font=("Comic Sans MS",15))
    label_debloat.pack()
    labeld1=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labeld1.pack()
    button_optimize=customtkinter.CTkButton(master=window,text="Optimize",command=optimize,fg_color="black",border_color="#6e1d51",hover_color="#6e1d51",border_width=1.5,text_font=("hacked",20))
    button_optimize.config(cursor="plus")
    button_optimize.pack()
    labelo=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labelo.pack()
    label_optimize=customtkinter.CTkLabel(window,text="Optimize: this will apply some optimizations to your system.",text_color="#f542b6",text_font=("Comic Sans MS",15))
    label_optimize.pack()
    labelo1=customtkinter.CTkLabel(master=window,text="\n",text_font=("Roboto Small", 1))
    labelo1.pack()
    def quit():
        playsound("Data\\1.mp3")
        window.destroy()
    exit_button=customtkinter.CTkButton(master=window,text="exit",text_font=("hacked",15),command=quit,fg_color="black",border_color="#700101",hover_color="#700101",border_width=1.5)
    exit_button.config(width=20,heigh=20,cursor="plus")
    exit_button.pack(side=BOTTOM,anchor=SE)
    window.mainloop()
splash.after(5500,main_window)
splash.mainloop()
os.system("start /min Data\\13.bat ^& exit")