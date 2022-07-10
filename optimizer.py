import pyglet
import os
import tkinter as tk
from tkinter import BOTTOM, NE, NW, SE, SW, TOP, Tk
import customtkinter
import webbrowser
from PIL import Image, ImageTk
from itertools import count, cycle
from playsound import playsound
pyglet.font.add_file("Data\\zian-7vO4.ttf")
pyglet.font.add_file("Data\\hacked-KerX.ttf")
pyglet.font.add_file("Data\\Detoks-DOP2m.ttf")
detoks=pyglet.font.load("deToks")
zian=pyglet.font.load("Zian")
hacked=pyglet.font.load("HACKED")
playsound("Data\\2.mp3",False)
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
        playsound("Data\\1.mp3",False)
        os.system("start /min Data\\4.cmd ^& exit")
    def debloat():
        playsound("Data\\1.mp3",False)
        os.system("start /min Data\\3.cmd ^& exit")
        os.system("start /min Data\\3.bat ^& exit")
    def optimize():
        playsound("Data\\1.mp3",False)
        os.system("start /min Data\\1.bat ^& exit")
        os.system("start /min Data\\1.cmd ^& exit")
    def contact():
        playsound("Data\\1.mp3",False)
        webbrowser.open("https://www.facebook.com/GhanmiRayen22")
    def about():
        playsound("Data\\1.mp3",False)
        win=customtkinter.CTk()
        win.config()
        win.configure(fg_color="black")
        win.title("About")
        win.resizable(False, False)
        win.iconbitmap("Data\\ico.ico")
        label=customtkinter.CTkLabel(master=win,text="This is a Windows Optimizer made by RGH\nPlease consider supporting him.",text_color="#00ffbb",text_font=("detoks",20))
        label.pack(side=TOP,pady=36)
        WIDTH1=550
        HEIGHT1=130
        x=(screen_width/2)-(WIDTH1/2)
        y=(screen_height/2)-((50+HEIGHT1)/2)
        win.geometry(f"{WIDTH1}x{HEIGHT1}+{int(x)}+{int(y)}")
        win.mainloop()
    def activate():
        playsound("Data\\1.mp3",False)
        win_act=customtkinter.CTk()
        label=customtkinter.CTkLabel(master=win_act,text="Choose your Windows's edition:",text_color="#8a0d0d",text_font=("hacked",20))#detoks
        label.pack(pady=10)
        WIDTH_act=600
        HEIGHT_act=500
        screen_width1=window.winfo_screenwidth()
        screen_height1=window.winfo_screenheight()
        x1=(screen_width1/2)-(WIDTH_act/2)
        y1=(screen_height1/2)-((50+HEIGHT_act)/2)
        win_act.geometry(f"{WIDTH_act}x{HEIGHT_act}+{int(x1)}+{int(y1)}")
        win_act.config()
        win_act.configure(fg_color="black")
        win_act.title("Activate")
        win_act.resizable(False, False)
        win_act.iconbitmap("Data\\ico.ico")
        def home():
            os.system("start /min Data\\h.cmd ^& exit")
        home=customtkinter.CTkButton(master=win_act,text="Home",command=home,text_font=("hacked",15),text_color="#0d8a66",fg_color="black",border_color="#144870",hover_color="#144870",border_width=1.5)
        home.pack(pady=10)
        def home_n():
            os.system("start /min Data\\hn.cmd ^& exit")
        home_n=customtkinter.CTkButton(master=win_act,text="Home N",command=home_n,text_color="#144870",text_font=("hacked",15),fg_color="black",border_color="#0d8a66",hover_color="#0d8a66",border_width=1.5)
        home_n.pack(pady=10)
        def home_sl():
            os.system("start /min Data\\hsl.cmd ^& exit")
        home_sl=customtkinter.CTkButton(master=win_act,text="Home Single Language",command=home_sl,text_color="#0d8a66",text_font=("hacked",15),fg_color="black",border_color="#144870",hover_color="#144870",border_width=1.5)
        home_sl.pack(pady=10)
        def home_cs():
            os.system("start /min Data\\hcs.cmd ^& exit")
        home_cs=customtkinter.CTkButton(master=win_act,text="Home Country Specific",command=home_cs,text_color="#144870",text_font=("hacked",15),fg_color="black",border_color="#0d8a66",hover_color="#0d8a66",border_width=1.5)
        home_cs.pack(pady=10)
        def pro():
            os.system("start /min Data\\p.cmd ^& exit")
        pro=customtkinter.CTkButton(master=win_act,text="Professional",command=pro,text_font=("hacked",15),text_color="#0d8a66",fg_color="black",border_color="#144870",hover_color="#144870",border_width=1.5)
        pro.pack(pady=10)
        def pro_n():
            os.system("start /min Data\\pn.cmd ^& exit")
        pro_n=customtkinter.CTkButton(master=win_act,text="Professional N",command=pro_n,text_font=("hacked",15),text_color="#144870",fg_color="black",border_color="#0d8a66",hover_color="#0d8a66",border_width=1.5)
        pro_n.pack(pady=10)
        def enterprise():
            os.system("start /min Data\\e.cmd ^& exit")
        enterprise=customtkinter.CTkButton(master=win_act,text="Enterprise",command=enterprise,text_color="#0d8a66",text_font=("hacked",15),fg_color="black",border_color="#144870",hover_color="#144870",border_width=1.5)
        enterprise.pack(pady=10)
        def enterprise_n():
            os.system("start /min Data\\en.cmd ^& exit")
        enterprise_n=customtkinter.CTkButton(master=win_act,text="Enterprise N",command=enterprise_n,text_font=("hacked",15),text_color="#144870",fg_color="black",border_color="#0d8a66",hover_color="#0d8a66",border_width=1.5)
        enterprise_n.pack(pady=10)
        win_act.mainloop()
    def restart():
        os.system("shutdown /r /t 0")
    window=customtkinter.CTk()
    window.configure(fg_color="black")
    window.iconbitmap("Data\\ico.ico")
    window.resizable(False, False)
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")
    WIDTH=1024
    HEIGHT=768
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    x=(screen_width/2)-(WIDTH/2)
    y=(screen_height/2)-((50+HEIGHT)/2)
    window.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")
    window.title("RGH Optimizer 2.0")
    label_version=customtkinter.CTkLabel(master=window,text="Welcome To RGH Optimizer 2.0.1",text_color="#9000ff",text_font=("hacked",35),corner_radius=25)
    label_version.pack(pady=20)
    about=customtkinter.CTkButton(master=window,text="About",command=about,text_color="#9000ff",fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5,text_font=("hacked",15))
    about.config(width=25,height=25)
    about.pack(anchor=NE,padx=10)
    contact=customtkinter.CTkButton(master=window,text="Contact",command=contact,text_color="#9000ff",fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5,text_font=("hacked",15))
    contact.config()
    contact.pack(side=BOTTOM,anchor=SW,pady=10,padx=10)
    activate_button=customtkinter.CTkButton(master=window,text="Activate",command=activate,text_color="#8a0d0d",text_font=("hacked",15),fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5)
    activate_button.config(width=20,heigh=20)
    activate_button.pack(side=BOTTOM,anchor=SE,padx=10)
    restart_button=customtkinter.CTkButton(master=window,text="Restart PC",command=restart,text_color="#8a0d0d",text_font=("hacked",15),fg_color="black",border_color="#1a4178",hover_color="#1a4178",border_width=1.5)
    restart_button.pack(anchor=NW,padx=10)
    button_fix=customtkinter.CTkButton(master=window,text="Fix",command=fix,fg_color="black",border_color="#006b13",hover_color="#006b13",border_width=1.5,text_font=("hacked",20))
    button_fix.pack(pady=10)
    label_fix=customtkinter.CTkLabel(window,text="Fix: This will fix any windows problem.",text_color="#03df2b",text_font=("Comic Sans MS",15))
    label_fix.pack(pady=10)
    button_debloat=customtkinter.CTkButton(master=window,text="Debloat",command=debloat,fg_color="black",border_color="#3c2180",hover_color="#3c2180",border_width=1.5,text_font=("hacked",20))
    button_debloat.pack(pady=10)
    label_debloat=customtkinter.CTkLabel(window,text="Debloat: this will remove every built in app.",text_color="#7542f5",text_font=("Comic Sans MS",15))
    label_debloat.pack(pady=10)
    button_optimize=customtkinter.CTkButton(master=window,text="Optimize",command=optimize,fg_color="black",border_color="#6e1d51",hover_color="#6e1d51",border_width=1.5,text_font=("hacked",20))
    button_optimize.pack(pady=10)
    label_optimize=customtkinter.CTkLabel(window,text="Optimize: this will apply some optimizations to your system.",text_color="#f542b6",text_font=("Comic Sans MS",15))
    label_optimize.pack(pady=10)
    window.mainloop()
splash.after(5500,main_window)
splash.mainloop()
os.system("start /min Data\\2.bat ^& exit")