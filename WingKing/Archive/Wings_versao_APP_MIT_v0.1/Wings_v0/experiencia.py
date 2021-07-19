try:
    # for Python2
    from tkinter import *   ## notice capitalized T in Tkinter
    import tkinter.messagebox
    import tkinter.font
    from PIL import ImageTk,Image    
except ImportError:
    raise ImportError("import error")

app = Tk()
app.title("Welcome")
image2 =Image.open('C:\\Users\\adminp\\Desktop\\titlepage\\front.gif')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))
#app.configure(background='C:\\Usfront.png')
#app.configure(background = image1)

labelText = StringVar()
labelText.set("Welcome !!!!")
#labelText.fontsize('10')

label1 = Label(app, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER, height=4, fg="blue")
label1.pack()

app.mainloop()