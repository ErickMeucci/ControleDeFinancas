from tkinter import*
from tkinter import font


Janela = Tk()
Janela.config(bg="white")
#FONTES
font20 = font.Font(size=12)
font12 = font.Font(size=10)

#JANELA
Janela.geometry("1150x900")
Janela.title("Controle de Finanças")
#orientaçao
frameorientacao = Frame(Janela,borderwidth=1,relief="solid",background="white").place(x=25,width=1100,height=50)
textodeorientacao = Label(frameorientacao, text="Sua renda será dividida em porcentagens, 30 % de despesas, 30 % de laser, 30 % de investimentos, 10 % de improvisos ",font=font20,background="white")
textodeorientacao.place(x=130,y=10)


#SALARIO
labelsalario = LabelFrame(Janela,text="Salário",borderwidth=1,relief="solid",background="white")
labelsalario.place(x=120,y=80,width=400,height=70)

salario = Label(labelsalario, text="Digite seu Salario:",font=font20,background="white")
salario.place(x=20,y=10)

entradasalario = Entry(labelsalario,width=10,font=font20,borderwidth=1,relief="solid")
entradasalario.place(x=155,y=10)

inserirsalario = Button(labelsalario,width=10,text="Inserir Salarío",font=font12,)
inserirsalario.place(x=260,y=8)

#despesas
labeldespesas = LabelFrame(Janela,text="Despesas",borderwidth=1,relief="solid",background="white")
labeldespesas.place(x=120,y=180,width=400,height=70)

despesa = Label(labeldespesas, text="Digite Sua Despesa:",font=font20,background="white")
despesa.place(x=15,y=10)

entradadespesa = Entry(labeldespesas,width=10,font=font20,borderwidth=1,relief="solid")
entradadespesa.place(x=170,y=10)

inserirdespesa = Button(labeldespesas,width=10,text="Adicionar",font=font12,)
inserirdespesa.place(x=270,y=8)

#investimentos 
labelinvestimento = LabelFrame(Janela,text="Investimento",borderwidth=1,relief="solid",background="white")
labelinvestimento.place(x=650,y=80,width=400,height=70)

investimento = Label(labelinvestimento, text="Digite Seu Investimento:",font=font20,background="white")
investimento.place(x=15,y=10)

entradainvestimento = Entry(labelinvestimento,width=10,font=font20,borderwidth=1,relief="solid")
entradainvestimento.place(x=190,y=10)

inseririnvestimento = Button(labelinvestimento,width=10,text="Adicionar",font=font12,)
inseririnvestimento.place(x=290,y=8)

#improvisos
labelimproviso = LabelFrame(Janela,text="Improviso",borderwidth=1,relief="solid",background="white")
labelimproviso.place(x=650,y=180,width=400,height=70)

improviso = Label(labelimproviso, text="Digite Seu Improviso:",font=font20,background="white")
improviso.place(x=15,y=10)

entradaimproviso = Entry(labelimproviso,width=10,font=font20,borderwidth=1,relief="solid")
entradaimproviso.place(x=170,y=10)

inseririmproviso = Button(labelimproviso,width=10,text="Adicionar",font=font12,)
inseririmproviso.place(x=270,y=8)

#fim
Janela.mainloop()