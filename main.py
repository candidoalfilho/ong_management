from turtle import Canvas

from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox


adm_log = "admin"
adm_pass = "hello_world"

root = Tk()
root.title("Sistema de Gestão de ONG")
root.minsize(width=400,height=400)
root.geometry("1000x600")
count = 0
empFrameCount = 0


def gettingAdmDetails():
    login = en1a.get()
    password = en2a.get()

    if login == adm_log and adm_pass == password:
        print("Logged in")

    en1a.delete(0, END)
    en2a.delete(0, END)


def LoginAdm():
    global labelFrame

    global count
    count += 1

    if (count >= 2):
        labelFrame.destroy()

    global en1a, en2a, SubmitBtn, btn1a, btn2a

    labelFrame = Frame(root, bg='#044F67')
    labelFrame.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.3)

    # Login ID
    lb1 = Label(labelFrame, text="ID de Login: ", bg='#044F67', fg='white')
    lb1.place(relx=0.05, rely=0.1)

    en1a = Entry(labelFrame)
    en1a.place(relx=0.3, rely=0.1, relwidth=0.62)

    lb2 = Label(labelFrame, text="Senha : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    en2a = Entry(labelFrame)
    en2a.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="SUBMIT", bg='#264348', fg='white', command=gettingAdmDetails)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)



# Admin Home Page
def Admin():
    global headingFrame1, headingFrame2, headingLabel, btn1, btn2, Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Olá administração!", fg='black')
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    btn2 = Button(root, text="Login", bg='black', fg='white', command=LoginAdm)
    btn2.place(relx=0.53, rely=0.3, relwidth=0.2, relheight=0.1)

    btn3 = Button(root, text="Sair", bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)



# Student Home Page
def Funcionario():
    global headingFrame1, headingFrame2, headingLabel, btn1, btn2, Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Hello, Student", fg='black')
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

# Take n greater than 0.25 and less than 5
same = True
n = 0.3

# Adding a background image
background_image = Image.open("./assets/images/collab.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#333945", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

headingLabel = Label(headingFrame2, text="Bem-vindo(a) ao Sistema de Gestão de ONGs!", fg='black')
headingLabel.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Administrador",bg='black', fg='white', command=Admin)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Funcionário",bg='black', fg='white', command=Funcionario)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)





root.mainloop()