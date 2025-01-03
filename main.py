import customtkinter

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap('icon\Calculator_window_icon.ico')
        self.title("Калькулятор")
        self.geometry("400x620")
        self.resizable(False, False)

        #widgets
        self.entry_input = customtkinter.CTkEntry(self, placeholder_text="Введіть перше число", width=150)
        
        
        #grid
        self.entry_input.pack(padx = 20, pady = 20)


        #self.button = customtkinter.CTkButton(self, text="Сумма", command=self.button_callbck)
        #self.button.pack(padx=20, pady=20)



    def button_callbck(self):
        print("Кнопка нажата")


app = Calculator()
app.mainloop()