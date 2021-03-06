from modulos import *
from validEntry import Validadores
from frameGrad import GradientFrame
from reports import Relatorios
from funcionalidades import Funcs

import pycep_correios

root = tix.Tk()
media = 0

class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()####
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def cepCorreios(self):
        try:
            self.cidade_entry.delete(0, END)
            self.lograd_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            zipcode = self.cep_entry.get()
            dadosCep = pycep_correios.get_address_from_cep(zipcode)
            print(dadosCep)
            self.cidade_entry.insert(END, dadosCep['cidade'])
            self.lograd_entry.insert(END, dadosCep['logradouro'])
            self.bairro_entry.insert(END, dadosCep['bairro'])
        except:
            messagebox.showinfo("Titulo da janela", "Cep não encontrado")
    def tela(self):
        self.root.title("Cadastro de alunos")
        #self.root.configure(background= '#1e3743')
        self.bg=ImageTk.PhotoImage(file="img/login.png")
        self.bg_img=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width=500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background= "#dfe3ee")
        self.aba2.configure(background= "lightgray")

        self.abas.add(self.aba1, text = "Aba 1")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas_bt = Canvas(self.aba1, bd=0, bg='#1e3743', highlightbackground = 'gray',
            highlightthickness=5)
        self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight=0.19)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.aba1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white',
                                activebackground='#108ecb', activeforeground="white"
                                , font = ('verdana', 8, 'bold'), command= self.limpa_aluno)
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)
        
        ### Criação do botao buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = self.janela2)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        texto_balao_buscar = "Digite no campo nome o aluno que deseja pesquisar"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = texto_balao_buscar)

        ### Criação do botao novo
        ## imgNovo
        self.btnovo = PhotoImage(data=base64.b64decode(self.btnovo_base64))
        self.btnovo = self.btnovo.subsample(2, 2)

        self.bt_novo = Button(self.aba1, bd =0, image = self.btnovo, command= self.add_aluno)
        self.bt_novo.place(relx=0.55, rely=0.1, width=60, height=30)

        ### Criação do botao alterar
        self.btalterar = PhotoImage(data=base64.b64decode(self.btalterar_base64))
        self.btalterar = self.btalterar.subsample(2, 2)

        self.bt_alterar = Button(self.aba1, image = self.btalterar, bd=0,
                                 command=self.altera_aluno)
        self.bt_alterar.place(relx=0.67, rely=0.1, width=60, height=30)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.deleta_aluno)
        self.bt_apagar.place(relx=0.8, rely=0.1,
                             relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text = "Matricula", bg= '#dfe3ee', fg = '#107db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd2)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text="Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.01, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.08, rely=0.35, relwidth=0.5)

        ## Criação da label e entrada do cep
        self.lb_cep = Label(self.aba1, text="CEP", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cep.place(relx=0.6, rely=0.35)
        
        self.lb_cep = Button(self.aba1, text="Buscar", bg='#dfe3ee', fg='#107db2',
                             command= self.cepCorreios)
        self.lb_cep.place(relx=0.86, rely=0.35)

        self.cep_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd2)
        self.cep_entry.place(relx=0.65, rely=0.35, relwidth=0.2)

        ## Criação da label e entrada do telefone
        self.lb_fone = Label(self.aba1,  text="Telefone", bg= '#dfe3ee', fg = '#107db2')
        self.lb_fone.place(relx=0.01, rely=0.55)

        self.fone_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd3)
        self.fone_entry.place(relx=0.1, rely=0.55, relwidth=0.3)

        ## Criação da label e entrada da cidade
        self.lb_cidade = Label(self.aba1, text="Cidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cidade.place(relx=0.42, rely=0.55)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.55, relwidth=0.3)

        ## Criação da label e entrada do logradouro
        self.lb_lograd = Label(self.aba1, text="Endereço", bg='#dfe3ee', fg='#107db2')
        self.lb_lograd.place(relx=0.01, rely=0.75)

        self.lograd_entry = Entry(self.aba1)
        self.lograd_entry.place(relx=0.1, rely=0.75, relwidth=0.3)

        ## Criação da label e entrada da bairro
        self.lb_bairro = Label(self.aba1, text="Bairro", bg='#dfe3ee', fg='#107db2')
        self.lb_bairro.place(relx=0.42, rely=0.75)

        self.bairro_entry = Entry(self.aba1)
        self.bairro_entry.place(relx=0.5, rely=0.75, relwidth=0.3)
        
        ## Criação da label e entrada da Nota Ad1
        self.lb_ad1 = Label(self.aba1, text="AD1", bg= '#dfe3ee', fg = '#107db2', )
        self.lb_ad1.place(relx=0.82, rely=0.55)

        self.ad1_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd4)
        self.ad1_entry.place(relx=0.87, rely=0.55, relwidth=0.04)
        
        ## Criação da label e entrada da Nota Ad2
        self.lb_ad2 = Label(self.aba1, text="AD2", bg= '#dfe3ee', fg = '#107db2')
        self.lb_ad2.place(relx=0.82, rely=0.75)

        self.ad2_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd4)
        self.ad2_entry.place(relx=0.87, rely=0.75, relwidth=0.04)
        
       # def media():
        #global media
            #ad1 = self.ad1_entry.get()
            #nota1 = float(ad1)
            #ad2 = self.ad2_entry.get()
            #nota2 = float(ad2)
            #media = nota1 + nota2 / 2
            
            #return media
            
        
        ## Criação da label e entrada da Nota Adf
        self.lb_adf = Label(self.aba1, text="ADF", bg= '#dfe3ee', fg = '#107db2')
        self.lb_adf.place(relx=0.94, rely=0.60)
        
        if media >= 7:
            self.adf_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd4, state="disabled")
            self.adf_entry.place(relx=0.94, rely=0.73, relwidth=0.04)
            
        elif media == 0:
            self.adf_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd4, state="disabled")
            self.adf_entry.place(relx=0.94, rely=0.73, relwidth=0.04)
        else:
            self.adf_entry = Entry(self.aba1, validate="key",validatecommand=self.vcmd4)
            self.adf_entry.place(relx=0.94, rely=0.73, relwidth=0.04)
            
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Matrícula")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="AD1")
        self.listaCli.heading("#4", text="AD2")
        self.listaCli.heading("#5", text="Media")
        self.listaCli.column("#0", width=0)
        self.listaCli.column("#1", width=60, anchor="center")
        self.listaCli.column("#2", width=100, anchor="center")
        self.listaCli.column("#3", width=100, anchor="center")
        self.listaCli.column("#4", width=100, anchor="center")
        self.listaCli.column("#5", width=100, anchor="center")
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85,)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu=filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpa aluno", command= self.limpa_aluno)

        filemenu2.add_command(label="Ficha do aluno", command=self.geraRelataluno)
    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title(" Janela 2  ")
        self.root2.configure(background='gray75')
        self.root2.geometry("360x160")
        self.root2.resizable(TRUE, TRUE)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
    def validaEntradas(self):
        ### Naming input validators

        self.vcmd2 = (self.root.register(self.validate_entry20), "%P")
        self.vcmd3 = (self.root.register(self.validate_entry11), "%P")
        self.vcmd4 = (self.root.register(self.validate_entry2float), "%P")

  

Application()