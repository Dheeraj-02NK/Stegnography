from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
from stegano import lsb

Alpahbets = ' A!1B@2C#D3$E%4F^G5&H*6I(J7)K_8L-M9+N=0O:P;Q\'R"S?T/U>V<W.X,Y`Z~'
Key = 3

def Caesar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    for c in plain_text:
        index = Alpahbets.find(c)
        index = (index + Key) % len(Alpahbets)
        cipher_text = cipher_text + Alpahbets[index]
    print(cipher_text)
    return cipher_text

def Caesar_decryption(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = Alpahbets.find(c)
        index = (index - Key) % len(Alpahbets)
        plain_text = plain_text + Alpahbets[index]
    print(cipher_text)
    return plain_text

# Create a new top-level window for the steganography application
root = Tk()
# Set the title and size of the window, and position it on the screen
root.title("Steganography - Hide a Secret Text ")
root.geometry("700x500+150+180")
# Disable the ability to resize the window
root.resizable(False, False)
# Set the background color of the window
root.configure(bg="navy")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image',
                                          filetypes=(("PNG file","*.png"),
                                                     ("JPG file","*.jpg"),
                                                     ("All file","*.txt")))
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img

def Hide():
    global secret
    message  = text1.get(1.0, END)
    secret = lsb.hide(str(filename), Caesar_encrypt(message))

def Show():
    clear_message = lsb.reveal(filename)
    clear_message = clear_message.decode()  # decode the bytes to string
    text1.delete(1.0, END)
    text1.insert(END, Caesar_decryption(clear_message))

def save():
    secret.save("hidden.jpg")


#icon
image_icon = PhotoImage(file='ghij.png')
root.iconphoto(False, image_icon)

#logo
logo = PhotoImage(file='ghij.png')
logo = logo.subsample(4)
Label(root, image=logo,bg="#2f4155").place(x=10, y=10)

# Title for the application
Label(root, text="KASHtech Cyber", bg='navy', fg='white', font=('Times New Roman', 25, 'bold')).place(x=80, y=20)

# First Frame
f1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f1.place(x=10, y=80)

lbl = Label(f1, bg='black')
lbl.place(x=40,y=10)

# Second Frame
f2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

# Creates a vertical scrollbar, places it in f2, and configures it to scroll text1 vertically
scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview())
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
f3 = Frame(root, bd=3, bg="navy", width=330, height=100, relief=GROOVE)
f3.place(x=10, y=370)

Button(f3,text="Open Image", width=10, height=2, font=('Times New Roman', 14, 'bold'), command=showimage).place(x=20, y=30)
Button(f3,text="Save Image", width=10, height=2, font=('Times New Roman', 14, 'bold'), command=save).place(x=180, y=30)
Label(f3, text='Picture, Image, Photo File', bg="navy", fg='white').place(x=20, y=5)

# Fourth Frame
f4 = Frame(root, bd=3, bg="navy", width=330, height=100, relief=GROOVE)
f4.place(x=360, y=370)

Button(f4,text="Hide message", width=10, height=2, font=('Times New Roman', 14, 'bold'), command=Hide).place(x=20, y=30)
Button(f4,text="Show message", width=10, height=2, font=('Times New Roman', 14, 'bold'), command=Show).place(x=180, y=30)
Label(f4, text='Picture, Image, Photo File', bg="navy", fg='white').place(x=20, y=5)

# Start the main event loop to keep the window open and responsive
root.mainloop()

