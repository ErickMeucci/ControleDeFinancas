from tkinter import *
from tkinter import ttk
import sqlite3 as lite

Janela = Tk()

class Funcoes():
    def limpatelaframe1(self):
        self.psentrada.delete(0, END)
        self.pientrada.delete(0, END)
        self.pdentrada.delete(0, END)
        self.pimentrada.delete(0, END)
        self.plazer.delete(0, END)
    def limpatelaframe2(self):
        self.einvestimentos.delete(0, END)
        self.vinvestimentos.delete(0, END)
        self.dinvestimentos.delete(0, END)
    def limpatelaframe3(self):
        self.elazer.delete(0, END)
        self.vlazer.delete(0, END)
        self.dlazer.delete(0, END)
    def limpatelaframe4(self):
        self.edespesas.delete(0, END)
        self.vdespesas.delete(0, END)
        self.ddespesas.delete(0, END) 
    def limpatelaframe5(self):
        self.eimprovisos.delete(0, END)
        self.vimprovisos.delete(0, END)
        self.dimprovisos.delete(0, END) 
    def conecta_bd(self):
        self.conn = lite.connect("pagamentos.bd")
        self.cursor = self.conn.cursor(); print('conecta banco de dados')
    def desconecta_bd(self):
        self.conn.close(); print('desconecta banco de dados')
    def montatabela(self):
        self.conecta_bd()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pagamentos (cod INTEGER PRIMARY KEY, descricao CHAR(40) NOT NULL, valor INTEGER(20) NOT NULL, data INTEGER(20) NOT NULL) """)
        self.conn.commit();print("banco de dados criado")
        self.desconecta_bd()
    def addinvestimentos(self):
        self.investimentos = self.einvestimentos.get()
        self.investimentos1 = self.vinvestimentos.get()
        self.investimentos2 = self.dinvestimentos.get()
        self.conecta_bd()
        self.cursor.execute("""INSERT INTO pagamentos (descricao, valor, data) VALUES (?,?,?)""",(self.investimentos,self.investimentos1,self.investimentos2))
        self.conn.commit()
        self.desconecta_bd
        self.selectlista()
        self.limpatelaframe2()
    def addlazer(self):
        self.lazer1 = self.elazer.get()
        self.lazer2 = self.vlazer.get()
        self.lazer3 = self.dlazer.get()
        self.conecta_bd()
        self.cursor.execute("""INSERT INTO pagamentos (descricao, valor, data) VALUES (?,?,?)""",(self.lazer1,self.lazer2,self.lazer3))
        self.conn.commit()
        self.desconecta_bd
        self.selectlista()
        self.limpatelaframe3()
    def selectlista(self):
        self.listagasto.delete(*self.listagasto.get_children())
        self.conecta_bd()
        listas = self.cursor.execute("""SELECT cod, descricao, valor, data FROM pagamentos ORDER BY data ASC;""")
        for i in listas:
            self.listagasto.insert("",END, values=i)
        self.desconecta_bd()


class aplicacao(Funcoes):
    def __init__(self):
        self.Janela = Janela
        self.tela()
        self.frames_tela_principal()
        self.botoes()
        self.textosentradas()
        self.lista()
        self.montatabela()
        self.selectlista()
        Janela.mainloop()  
    def tela(self):
        self.Janela.title("Controle Finanças")
        self.Janela.configure(background="LightBlue1")
        self.Janela.geometry("900x700")
        self.Janela.resizable(True,True)
        self.Janela.maxsize(width=1280,height=960)
        self.Janela.minsize(width=800,height=600)
        self.imagemlixo = PhotoImage(file="C:/Users/Erick/Desktop/Controle financeiro/ControleDeFinancas/img/delete.png")
    def frames_tela_principal(self):
      self.frame_1 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.12)
      self.frame_2 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_2.place(relx=0.01,rely=0.14,relwidth=0.485,relheight=0.17)
      self.frame_3 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_3.place(relx=0.505,rely=0.14,relwidth=0.485,relheight=0.17)
      self.frame_4 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_4.place(relx=0.01,rely=0.32,relwidth=0.485,relheight=0.17)
      self.frame_5 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_5.place(relx=0.505,rely=0.32,relwidth=0.485,relheight=0.17)
      self.frame_6 = Frame(self.Janela, bd=4, bg="azure",highlightbackground="gray44",highlightthickness=2 )
      self.frame_6.place(relx=0.01,rely=0.50,relwidth=0.98,relheight=0.48)
    def botoes(self):

        #botao para adcionar as porcentagens
        self.bt_f1 = Button(self.frame_1, text="Adicionar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'))
        self.bt_f1.place(relx=0.89, rely=0.05,relwidth=0.1,relheight=0.40)
        self.bta_f1 = Button(self.frame_1, text="Limpar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.limpatelaframe1)
        self.bta_f1.place(relx=0.89, rely=0.55,relwidth=0.1,relheight=0.40)
        #botao para adicinar o salario
        self.bt_f2 = Button(self.frame_2, text="Adicionar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command= self.addinvestimentos)
        self.bt_f2.place(relx=0.80, rely=0.73,relwidth=0.20,relheight=0.25)

        self.bta_f2 = Button(self.frame_2, image=self.imagemlixo,bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.limpatelaframe2)
        self.bta_f2.place(relx=0.7, rely=0.73,relwidth=0.09,relheight=0.25)
        #botao para adicinar o investimentos
        self.bt_f3 = Button(self.frame_3, text="Adicionar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.addlazer)
        self.bt_f3.place(relx=0.80, rely=0.73,relwidth=0.20,relheight=0.25)

        self.bta_f3 = Button(self.frame_3, image=self.imagemlixo,bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.limpatelaframe3)
        self.bta_f3.place(relx=0.70, rely=0.73,relwidth=0.09,relheight=0.25)
        #botao para adicinar o despesas
        self.bt_f4 = Button(self.frame_4, text="Adicionar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'))
        self.bt_f4.place(relx=0.80, rely=0.73,relwidth=0.20,relheight=0.25)

        self.bta_f4 = Button(self.frame_4, image=self.imagemlixo,bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.limpatelaframe4)
        self.bta_f4.place(relx=0.70, rely=0.73,relwidth=0.09,relheight=0.25)
        #botao para adicinar o improvisos
        self.bt_f5 = Button(self.frame_5, text="Adicionar",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'))
        self.bt_f5.place(relx=0.80, rely=0.73,relwidth=0.20,relheight=0.25)

        self.bta_f5 = Button(self.frame_5, image=self.imagemlixo, bd=3, bg="ghost white",fg="gray1",font=('arial', 9, 'bold'),command=self.limpatelaframe5)
        self.bta_f5.place(relx=0.70, rely=0.73,relwidth=0.09,relheight=0.25)
        #botao para remover
        self.bt_f6 = Button(self.frame_6, text="Remover",bd=3,bg="ghost white",fg="gray1",font=('arial', 9, 'bold'))
        self.bt_f6.place(relx=0.90, rely=0.90,relwidth=0.08,relheight=0.09)
    def textosentradas(self):
        #introdiçao frame 1
        self.instrucao = Label(self.frame_1, text="Digite suas porcentagens:",bg='azure',fg="gray1",font=('arial', 11, 'bold'))
        self.instrucao.place(relx=0.005,rely=0.05)
        #salario frame 1
        self.salario = Label(self.frame_1, text="Porcentagens do Salário:",bg='azure',fg="gray1",font=('arial', 9))
        self.salario.place(relx=0.23,rely=0.05)
        self.psentrada = Entry(self.frame_1,borderwidth=1,relief="solid")
        self.psentrada.place(relx=0.40,rely=0.05,relwidth=0.05)
        #investimento frame 1
        self.investimento = Label(self.frame_1, text="Porcentagens dos Investimentos:",bg='azure',fg="gray1",font=('arial', 9))
        self.investimento.place(relx=0.30,rely=0.60)
        self.pientrada = Entry(self.frame_1,borderwidth=1,relief="solid")
        self.pientrada.place(relx=0.52,rely=0.60,relwidth=0.05)
        #despesas frame 1
        self.despesas = Label(self.frame_1, text="Porcentagens das Despesas:",bg='azure',fg="gray1",font=('arial', 9))
        self.despesas.place(relx=0.004,rely=0.60)
        self.pdentrada = Entry(self.frame_1,borderwidth=1,relief="solid")
        self.pdentrada.place(relx=0.2,rely=0.60,relwidth=0.05)
        #improvisos frame 1
        self.improvisos = Label(self.frame_1, text="Porcentagens do Imprevisto:",bg='azure',fg="gray1",font=('arial', 9))
        self.improvisos.place(relx=0.60,rely=0.60)
        self.pimentrada = Entry(self.frame_1,borderwidth=1,relief="solid",fg="gray1",font=('arial', 9))
        self.pimentrada.place(relx=0.80,rely=0.60,relwidth=0.05)
        #lazer frame 1
        self.lazer = Label(self.frame_1, text="Porcentagens das Lazer:",bg='azure',fg="gray1",font=('arial', 9))
        self.lazer.place(relx=0.50,rely=0.05)
        self.plazer = Entry(self.frame_1,borderwidth=1,relief="solid")
        self.plazer.place(relx=0.68,rely=0.05,relwidth=0.05)

        #entrada investimentos frame 2
        self.investimentos = Label (self.frame_2, text="Investimentos",bg='azure',fg="gray1",font=('arial', 11, 'bold'))
        self.investimentos.place(relx=0.005,rely=0.05)
        self.tipo = Label(self.frame_2,text="Tipo do invetimento:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.3)
        self.einvestimentos = Entry(self.frame_2)
        self.einvestimentos.place(relx=0.3,rely=0.3 )
        self.tipo = Label(self.frame_2,text="Valor do invetimento:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.6)
        self.vinvestimentos = Entry(self.frame_2)
        self.vinvestimentos.place(relx=0.3,rely=0.6 )
        self.tipo = Label(self.frame_2,text="Data:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.15)
        self.dinvestimentos = Entry(self.frame_2)
        self.dinvestimentos.place(relx=0.80,rely=0.15,relwidth=0.15 )
        self.tipo = Label(self.frame_2,text="Meta:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.40)
        self.minvestimentos = Label(self.frame_2,text="x",bg='azure',fg="gray1",font=('arial', 9))
        self.minvestimentos.place(relx=0.80,rely=0.40)

        #entrada lazer frame 3
        self.lazer1 = Label (self.frame_3, text="Lazer",bg='azure',fg="gray1",font=('arial', 11, 'bold'))
        self.lazer1.place(relx=0.005,rely=0.05)
        self.tipo = Label(self.frame_3,text="Tipo do Lazer:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.3)
        self.elazer = Entry(self.frame_3)
        self.elazer.place(relx=0.3,rely=0.3 )
        self.tipo = Label(self.frame_3,text="Valor do Lazer:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.6)
        self.vlazer = Entry(self.frame_3)
        self.vlazer.place(relx=0.3,rely=0.6 )
        self.tipo = Label(self.frame_3,text="Data:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.15)
        self.dlazer = Entry(self.frame_3)
        self.dlazer.place(relx=0.80,rely=0.15,relwidth=0.15 )
        self.tipo = Label(self.frame_3,text="Meta:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.40)
        self.mlazer = Label(self.frame_3,text="x",bg='azure',fg="gray1",font=('arial', 9))
        self.mlazer.place(relx=0.80,rely=0.40)
        

        #entrada despesas frame 4
        self.despesas1 = Label (self.frame_4, text="Despesas",bg='azure',fg="gray1",font=('arial', 11, 'bold'))
        self.despesas1.place(relx=0.005,rely=0.05)
        self.tipo = Label(self.frame_4,text="Tipo do Despesas:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.3)
        self.edespesas = Entry(self.frame_4)
        self.edespesas.place(relx=0.3,rely=0.3 )
        self.tipo = Label(self.frame_4,text="Valor do Despesas:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.6)
        self.vdespesas = Entry(self.frame_4)
        self.vdespesas.place(relx=0.3,rely=0.6 )
        self.tipo = Label(self.frame_4,text="Data:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.15)
        self.ddespesas = Entry(self.frame_4)
        self.ddespesas.place(relx=0.80,rely=0.15,relwidth=0.15 )
        self.tipo = Label(self.frame_4,text="Meta:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.40)
        self.mdespesas = Label(self.frame_4,text="x",bg='azure',fg="gray1",font=('arial', 9))
        self.mdespesas.place(relx=0.80,rely=0.40)

        #entrada improvisos frame 5
        self.improvisos1 = Label (self.frame_5, text="Improvisos",bg='azure',fg="gray1",font=('arial', 11, 'bold'))
        self.improvisos1.place(relx=0.005,rely=0.05)
        self.tipo = Label(self.frame_5,text="Tipo do Improvisos:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.3)
        self.eimprovisos = Entry(self.frame_5)
        self.eimprovisos.place(relx=0.3,rely=0.3 )
        self.tipo = Label(self.frame_5,text="Valor do Improvisos:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.005,rely=0.6)
        self.vimprovisos = Entry(self.frame_5)
        self.vimprovisos.place(relx=0.3,rely=0.6 )
        self.tipo = Label(self.frame_5,text="Data:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.15)
        self.dimprovisos = Entry(self.frame_5)
        self.dimprovisos.place(relx=0.80,rely=0.15,relwidth=0.15 )
        self.tipo = Label(self.frame_5,text="Meta:",bg='azure',fg="gray1",font=('arial', 9))
        self.tipo.place(relx=0.70,rely=0.40)
        self.mimprovisos = Label(self.frame_5,text="x",bg='azure',fg="gray1",font=('arial', 9))
        self.mimprovisos.place(relx=0.80,rely=0.40)
    def lista(self):
        self.listagasto = ttk.Treeview(self.frame_6, height=3, column=("coli1", "coli2", "coli3","coli4"))
        self.listagasto.heading("#0",text="")
        self.listagasto.heading("#1",text="id")
        self.listagasto.heading("#2",text="Descrição")
        self.listagasto.heading("#3",text="Valor")
        self.listagasto.heading("#4",text="Datas")
        self.listagasto.column('#0',width=1)
        self.listagasto.column('#1',width=50)
        self.listagasto.column('#2',width=200)
        self.listagasto.column('#3',width=125)
        self.listagasto.column('#4',width=125)
        self.listagasto.place(relx=0.01,rely=0.02,relwidth=0.95,relheight=0.85)

        self.rolagem = Scrollbar(self.frame_6, orient='vertical')
        self.listagasto.configure(yscroll=self.rolagem.set)
        self.rolagem.place(relx=0.96, rely=0.02, relwidth=0.02,relheight=0.85)
       

aplicacao()