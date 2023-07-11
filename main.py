import requests
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)


def SignUp():
    win = Toplevel(root)
    win.title("SignUp")
    win.geometry('450x560+500+200')
    win.configure(bg="#f4fdfe")
    win.resizable(False, False)

    Label(win, text='New User? SignUp Now!! ', bg="white", fg="black", font='arial 18 bold').place(x=60, y=30)

    Label(win, text='Email Id: ', bg="white", fg="black", font='arial 12').place(x=50, y=100)
    Entry(win, width=30).place(x=120, y=100)

    Label(win, text='Password: ', bg="white", fg="black", font='arial 12').place(x=50, y=130)
    Entry(win, width=30).place(x=140, y=130)

    Button(win, text="Submit", width=6, height=1, font='arial 14 bold', bg='#000', fg='#fff').place(x=150, y=200)


def LogIn():
    win = Toplevel(root)
    win.title("SignUp")
    win.geometry('450x560+500+200')
    win.configure(bg="#f4fdfe")
    win.resizable(False, False)

    Label(win, text='Already an User? Login Now!! ', bg="white", fg="black", font='arial 18 bold').place(x=60, y=30)

    Label(win, text=f'Email Id: ', bg="white", fg="black", font='arial 12').place(x=50, y=100)
    Entry(win, width=30).place(x=120, y=100)

    Label(win, text=f'Password: ', bg="white", fg="black", font='arial 12').place(x=50, y=130)
    Entry(win, width=30).place(x=140, y=130)

    Button(win, text="Submit", width=6, height=1, font='arial 14 bold', bg='#000', fg='#fff').place(x=150, y=200)


def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                              filetype=(('file_type', '*.txt'), ('all files', '.*')))

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Waiting for incoming connections...')
        conn, addr = s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transferred successfully")
        conn.close()

    # icon
    image_icon1 = PhotoImage(file="Image/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="Image/sender.png")
    Label(window, image=Sbackground).place(x=-2, y=0)

    Mbackground = PhotoImage(file="Image/id.png")
    Label(window, image=Mbackground, bg='#f4fdfe').place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg="white", fg="black").place(x=100, y=260)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000",
           command=select_file).place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg='#000', fg='#fff',
           command=sender).place(x=300, y=150)
    window.mainloop()


def Receive():
    def receiver():
        host = socket.gethostname()
        port = 8080

        s = socket.socket()
        s.connect((host, port))

        filename1 = incoming_file.get()

        file_dir = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Directory')
        filepath = os.path.join(file_dir, filename1)

        with open(filepath, 'wb') as file:
            while True:
                file_data = s.recv(1024)
                if not file_data:
                    break
                file.write(file_data)

        print('File has been received successfully')

    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    # icon
    image_icon1 = PhotoImage(file="Image/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="Image/receiver.png")
    Label(main, image=Hbackground).place(x=-2, y=0)

    logo = PhotoImage(file='Image/profile.png')
    Label(main, image=logo, bg="#f4fdfe").place(x=100, y=250)

    Label(main, text='Receive', font=('arial', 20), bg="#f4fdfe").place(x=100, y=280)
    Label(main, text="Input sender id", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="Filename for the incoming file", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    imageicon = PhotoImage(file='Image/arrow.png')
    rr = Button(main, text='Receive', compound=LEFT, image=imageicon, width=130, bg='#39c790', font="arial 14 bold",
                command=receiver)
    rr.place(x=20, y=500)

    main.mainloop()




#icon
image_icon=PhotoImage(file="Image\icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
b1= Button(root,text="Login",width=5, bg='white',fg='black',command=LogIn)
b1.place(x=330,y=30)
b1= Button(root,text="SignUp",width=5, bg='white',fg='black',command=SignUp)
b1.place(x=390,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="Image/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="Image/receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)


background=PhotoImage(file="Image/background.png")
Label(root,image=background).place(x=-2,y=323)


root.mainloop()



