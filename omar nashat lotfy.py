from tkinter import *

-



window = Tk()
window.title ("youtube")
window.geometry("600x400")
window.configure(bg = "beige")
 

label=Label(window,text = "add your youtube link here", font ="bold", bg =window['bg'])
label.place(x=200,y=30)

entry = Entry(window)
entry.place (x=225,y=70)

hight =Button(window, text= "hight quality" , command= print)
medium =Button(window, text= "medium quality" , command= print)
low =Button(window, text= "low quality" , command= print)
hight.place(x=100,y=200)
medium.place(x=150,y=250)
low.place(x=200,y=300)

audio=Button(window, text="Get Audio" , command=print,font ="bold")
audio.place(x=400,y=250)
window.mainloop()



