## Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from turtle import back
from PIL import Image,ImageTk
import numpy
import numpy as np

# Loading the Model
from keras.models import load_model
model = load_model('Hair_eye_color_Detection.h5')

# Initializing the GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Hair And Eye Color Dectector')
top.configure(background='#CDCDCD')

# Initializing the Labels (1 for age and 1 for sex)
label1 = Label(top,background="#CDCDCD",font=('arial',15,"bold"))
label2 = Label(top,background="#CDCDCD",font=('arial',15,"bold"))
sign_image = Label(top)

# Defining Detect function which detects the hair & Eye Color of the person in image using the model
def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((80,80))
    image = numpy.expand_dims(image,axis=0)
    image = np.array(image)
    image = np.delete(image,0,1)
    image = np.resize(image,(80,80,3))
    print (image.shape)
    hair_f=["Black", "Brown", "Blonde or Strawberry"," Gray or Partially","Red or Auburn", "Bald ","Salt and Pepper", "White", "Sandy"]
    eye_f =["Brown" , "Blue", "Hazel" ,"Green", "Black","Gray", "Maroon"]
    image = np.array([image])/255
    pred = model.predict(image)
    hair = int(np.round(pred[1][0]))
    eye = int(np.round(pred[0][0]))
    print("Predicted Hair Color is "+hair_f[hair])
    print("Predicted Eye Color is "+eye_f[eye])
    label1.configure(foreground="#011638",text="Hair color is "+hair_f[hair])
    label2.configure(foreground="#011638",text="Eye color is "+eye_f[eye])

# Defining Show_detect button function
def show_Detect_button(file_path):
    Detect_b = Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46)

# Defining Upload Image Function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass

upload = Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)

label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
heading = Label(top,text="Hair And Eye Color Detector",pady=20,font=('arial',20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()

