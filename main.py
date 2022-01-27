import tkinter as tk
from tkinter import *
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from monitor import monitor
from PIL import Image, ImageTk
import tkinter.ttk as ttk 

window = tk.Tk()
window.title("CCTV")
window.iconphoto(False, tk.PhotoImage(file='C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/mn.png'))
window.geometry('900x675')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="CCTV Surveillance")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)

#gui = tk.Tk()

icon = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/lamp.jpg')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/mark.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image) 


btn3_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('C:/Users/archi/OneDrive/Desktop/ML projects/smart-cctv-tkinter-master/icons/record.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='red',command=monitor, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Marker', height=90, width=180, fg='red', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

# btn_font = font.Font(size=25)
# btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left')
# btn3['font'] = btn_font
# btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='red', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='red', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10))

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image, compound='left')
btn5['font'] = btn_font
btn5.grid(row=4, pady=(20,10), column=2)


frame1.configure(bg='peach puff')
window.configure(bg='black')

frame1.pack()
window.mainloop()


#'F:/Rough/smart-cctv-tkinter-master-20210714T112842Z-001/smart-cctv-tkinter-master/icons/back.png'