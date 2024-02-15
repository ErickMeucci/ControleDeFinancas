from tkinter import * 
from tkinter import ttk

Janelacalculadora = Tk()

class aplicacao():
    def __init__(self):
        self.Janelacalculadora = Janelacalculadora
        self.visor_texto = StringVar()  # Variável para armazenar o texto do visor
        self.visor_texto.set("")  # Inicializa o texto do visor
        self.cria_interface()
        self.vincula_eventos_teclado()
        Janelacalculadora.mainloop()
    def limpa_calcula(self):
        self.visor_texto.set("")
    def backspace(self):
        texto_atual = self.visor_texto.get()
        novo_texto = texto_atual[:-1]
        self.visor_texto.set(novo_texto)
    def atualiza_visores(self, valor):
        texto_atual = self.visor_texto.get()
        if valor == '.' and '.' in texto_atual:
            return
        novo_texto = texto_atual + str(valor)
        self.visor_texto.set(novo_texto)
    def realiza_divisao(self):
        self.atualiza_visores("/")
    def realiza_mutiplica(self):
        self.atualiza_visores("*")
    def realiza_subtracao(self):
        self.atualiza_visores("-")
    def realiza_soma(self):
        self.atualiza_visores("+")
    def realiza_calculo(self):
        try:
            resultado = eval(self.visor_texto.get())
            self.visor_texto.set(resultado)
        except Exception as e:
            self.visor_texto.set("Erro")
    def cria_interface(self):
        self.Janelacalculadora.geometry("300x450")
        self.Janelacalculadora.title("Calculadora")
        self.Janelacalculadora.configure(background="LightBlue1")
        self.Janelacalculadora.resizable(True,True)
        self.Janelacalculadora.maxsize(width=300,height=450)
        self.Janelacalculadora.minsize(width=300,height=450)
        #visor
        self.visor = Entry(self.Janelacalculadora,textvariable=self.visor_texto,borderwidth=1,relief="solid",font=('arial', 25, 'bold'), justify='right' )
        self.visor.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.15)
        #botoes7
        self.numero7 = Button(self.Janelacalculadora,text="7",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(7))
        self.numero7.place(relx=0.01,rely=0.17,relwidth=0.24,relheight=0.19)
        #botoes8
        self.numero8 = Button(self.Janelacalculadora,text="8",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(8))
        self.numero8.place(relx=0.26,rely=0.17,relwidth=0.24,relheight=0.19)
        #botoes4
        self.numero4 = Button(self.Janelacalculadora,text="4",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(4))
        self.numero4.place(relx=0.01,rely=0.37,relwidth=0.24,relheight=0.19)
        #botoes5
        self.numero5 = Button(self.Janelacalculadora,text="5",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(5))
        self.numero5.place(relx=0.26,rely=0.37,relwidth=0.24,relheight=0.19)
        #botoes1
        self.numero1 = Button(self.Janelacalculadora,text="1",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(1))
        self.numero1.place(relx=0.01,rely=0.57,relwidth=0.24,relheight=0.19)
        #botoes2
        self.numero2 = Button(self.Janelacalculadora,text="2",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(2))
        self.numero2.place(relx=0.26,rely=0.57,relwidth=0.24,relheight=0.19)
        #botoesC
        self.numeroc = Button(self.Janelacalculadora,text="C",bd=3,bg="ghost white",fg="gray1",font=('arial', 16, 'bold'),command=self.limpa_calcula)
        self.numeroc.place(relx=0.01,rely=0.77,relwidth=0.20,relheight=0.19)
        #botoes0
        self.numero0 = Button(self.Janelacalculadora,text="0",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(0))
        self.numero0.place(relx=0.22,rely=0.77,relwidth=0.20,relheight=0.19)
        #botoes9
        self.numero9 = Button(self.Janelacalculadora,text="9",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(9))
        self.numero9.place(relx=0.51,rely=0.17,relwidth=0.24,relheight=0.19)
        #botoes/
        self.numerod = Button(self.Janelacalculadora,text="/",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=self.realiza_divisao)
        self.numerod.place(relx=0.76,rely=0.17,relwidth=0.22,relheight=0.19)
        #botoes6
        self.numero6 = Button(self.Janelacalculadora,text="6",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(6))
        self.numero6.place(relx=0.51,rely=0.37,relwidth=0.24,relheight=0.19)
        #botoesX
        self.numerox = Button(self.Janelacalculadora,text="X",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=self.realiza_mutiplica)
        self.numerox.place(relx=0.76,rely=0.37,relwidth=0.22,relheight=0.19)
        #botoes3
        self.numero3 = Button(self.Janelacalculadora,text="3",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores(3))
        self.numero3.place(relx=0.51,rely=0.57,relwidth=0.24,relheight=0.19)
        #botoes-
        self.numeron = Button(self.Janelacalculadora,text="-",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=self.realiza_subtracao)
        self.numeron.place(relx=0.76,rely=0.57,relwidth=0.22,relheight=0.19)
        #botoes=
        self.numeroi = Button(self.Janelacalculadora,text="=",bd=3,bg="ghost white",fg="gray1",font=('arial', 16, 'bold'), command=self.realiza_calculo)
        self.numeroi.place(relx=0.59,rely=0.77,relwidth=0.19,relheight=0.19)
        #botoes+
        self.numerom = Button(self.Janelacalculadora,text="+",bd=3,bg="ghost white",fg="gray1",font=('arial', 14, 'bold'), command=self.realiza_soma)
        self.numerom.place(relx=0.79,rely=0.77,relwidth=0.20,relheight=0.19)

        self.numerodecimal = Button(self.Janelacalculadora, text=".", bd=3, bg="ghost white", fg="gray1", font=('arial', 14, 'bold'), command=lambda: self.atualiza_visores('.'))
        self.numerodecimal.place(relx=0.43, rely=0.77, relwidth=0.15, relheight=0.19)
    def vincula_eventos_teclado(self):
        numeros = '0123456789.'
        operadores = '+-*/'

        for num in numeros:
            self.Janelacalculadora.bind(num, lambda event, n=num: self.atualiza_visores(n))

        for op in operadores:
            if op != '=':
                self.Janelacalculadora.bind(op, lambda event, o=op: self.atualiza_visores(o))
        self.Janelacalculadora.bind('<Return>', lambda event: self.realiza_calculo())
        self.Janelacalculadora.bind('<BackSpace>', lambda event: self.backspace())
aplicacao()