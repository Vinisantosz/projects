import login
from tkinter import *


def main():

    # GARANTE QUE O USUARIO NÃO TENTE EXECULTAR FUNÇÕES SEM QUE ESTAR LOGADO 
    while(login.login() == False):
        print("usuario ou senha invalido")

janela = Tk()
janela.title("LOGIN")
janela.mainloop()
