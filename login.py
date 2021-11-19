#Declarando as bibliotecas
from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import messagebox

from app import Application

class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login Academia Ninja")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)

        # Background Img
        self.bg=ImageTk.PhotoImage(file="img/login.png")
        self.bg_img=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # painel login
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)


        #test=Label(Frame_login,text="Login Here", font=("Ninja Naruto", 35))
        title=Label(Frame_login, text="Login Shinobi ",font=("Ninja Naruto",35,"bold"), fg="#d77337", bg="white").place(x=55,y=30)
        desc=Label(Frame_login, text="Programação de Computadores",font=("Goudy old style",15,"bold"), fg="#d25d17", bg="white").place(x=90,y=100)
        
        lbl_user=Label(Frame_login, text="Usuário:",font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login, font=("times new roman", 15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login, text="Senha:",font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login, font=("times new roman", 15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,command=self.forget_function,text="Esqueceu a Senha Click Aqui!",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)   
        login_btn=Button(self.root,command=self.login_function,text="Entrar",bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=470, width=180,height=40)
    
    #funções para Validação do login    
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","Os campos não podem ficar vazios", parent=self.root)
        elif self.txt_user.get()=="adm" and self.txt_pass.get()=="adm":
            messagebox.showinfo("Bem Vindo!", f"Bem vindo! {self.txt_user.get()}" +  " ao Sistema de notas Shinobi", parent=self.root)  

        else:
            messagebox.showerror("Error","Nome de Usuário ou Senha Incorretos", parent=self.root)
    
    def forget_function(self):
        messagebox.showinfo("Recuperação de senha", f"Usuário: adm \n" + "Senha: adm", parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()
