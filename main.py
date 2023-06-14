from tkinter import *

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("235x302")
calculadora.config(bg="#000")

quadro = Frame(calculadora, width=235, height=50, bg="#B5B5B5")
quadro.grid(row=0, column=0)

corpo = Frame(calculadora, width=235, height=280)
corpo.grid(row=1, column=0)


valores_total = ''

valor_text = StringVar()
app_label = Label(quadro, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 17 bold"), bg="#ffffff", fg="#1b1b1b")
app_label.place(x=0, y=0)


def entrada(event):
    global valores_total
    valores_total += str(event)


    valor_text.set(valores_total)


def calcular():
    global valores_total
    resultado = eval(valores_total)
    valor_text.set(str(resultado))


def limpar():
    global valores_total
    valores_total = ''
    valor_text.set('')



b_1 = Button(corpo,command= limpar,text="C", width=11, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(corpo,command = lambda: entrada("**"),text="**", width=10, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_2.place(x=90, y=0)

b_3 = Button(corpo, command = lambda: entrada("%"), text="%", width=5, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(corpo, command = lambda: entrada("7"),text="7", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(corpo,command = lambda: entrada("8"),text="8", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(corpo,command = lambda: entrada("9"),text="9", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(corpo, command = lambda: entrada("+"),text="+", width=5, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(corpo,command = lambda: entrada("4"),text="4", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_8.place(x=0, y=102)

b_9 = Button(corpo, command = lambda: entrada("5"),text="5", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_9.place(x=59, y=102)

b_10 = Button(corpo,command = lambda: entrada("6"),text="6", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_10.place(x=118, y=102)

b_11 = Button(corpo,command = lambda: entrada("-"),text="-", width=5, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_11.place(x=177, y=102)

b_16 = Button(corpo,command = lambda: entrada("1"),text="1", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_16.place(x=0, y=151)

b_17 = Button(corpo,command = lambda: entrada("2"),text="2", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_17.place(x=59, y=151)

b_18 = Button(corpo, command = lambda: entrada("3"),text="3", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_18.place(x=118, y=151)

b_19 = Button(corpo,command = lambda: entrada("*"),text="*", width=5, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_19.place(x=177, y=151)

b_21 = Button(corpo,command = calcular,text="=", width=11, height=2, bg="#FA9A01", fg="#FFFFFF", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_21.place(x=120, y=202)

b_22 = Button(corpo,command = lambda: entrada("0"),text="0", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_22.place(x=0, y=202)

b_23 = Button(corpo,command = lambda: entrada("."),text=".", width=5, height=2, bg="#FEFEDC", fg="#000000", font=("Ivy 13 bold"), relief=RAISED,overrelief=RIDGE)
b_23.place(x=59, y=202)


calculadora.mainloop()
