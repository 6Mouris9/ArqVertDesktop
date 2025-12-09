from tkinter import Entry
import  customtkinter as ctk



class Janela():
    window = ctk.CTk()
    valor = "None"
    entrada = Entry(window, textvariable="variavel")
    entrada.grid(row=2,column=2, padx=100,pady=110)

    
    def button_callback():
        Janela.valor = Janela.entrada.get()
        print(Janela.valor)
        return True
    variavel: str
    
    
    
    button = ctk.CTkButton(window, text="CLique para printar", command=button_callback)
    button.grid(row=0,column=0, padx=20,pady=20)

janela = Janela()
janela.window.mainloop()

