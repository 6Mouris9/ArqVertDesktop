import  customtkinter as ctk



class Janela():
    window = ctk.CTk()
    

    
    def button_callback():
        print("Buttom pressed")
    
    button = ctk.CTkButton(window, text="CLique para printar", command=button_callback)
    button.grid(row=0,column=0, padx=20,pady=20)


janela = Janela()
janela.window.mainloop()

