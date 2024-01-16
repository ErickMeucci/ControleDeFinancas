from tkinter import*
from tkinter import font


Janela = Tk()
#FONTES
font20 = font.Font(size=12)
font12 = font.Font(size=10)

#JANELA
Janela.geometry("1050x700")
Janela.title("Controle de Finanças")
textodeorientacao = Label(Janela, text="Sua renda será dividida em porcentagens,30Porcento de despesas,30Porcento de laser,30Porcento de investimentos,10Porcento de improvisos ",font=font20)
textodeorientacao.place(x=25)


#SALARIO
labelsalario = LabelFrame(Janela,text="Salário",borderwidth=1,relief="solid")
labelsalario.place(x=25,y=30,width=400,height=70)

salario = Label(labelsalario, text="Digite seu salario:",font=font20)
salario.place(x=25,y=10)

entradasalario = Entry(labelsalario,width=10,font=font20)
entradasalario.place(x=155,y=10)

inserirsalario = Button(labelsalario,width=10,text="Inserir Salarío",font=font12,)
inserirsalario.place(x=250,y=8)



Janela.mainloop()