import customtkinter
from PIL import Image, ImageTk

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap('icon\Calculator_window_icon.ico')
        self.title('Калькулятор')
        self.geometry('400x620')
        self.resizable(False, False)
        self.configure(fg_color='#04202C')
        
   #bg='#5B7065'
        #widgets
        self.entry_input1 = customtkinter.CTkEntry(self, placeholder_text='Введіть перше число', width=150)
        self.entry_input2 = customtkinter.CTkEntry(self, placeholder_text='Введіть друге число', width=150)

        self.button_plus = customtkinter.CTkButton(self, text=None, fg_color='#5B7065', image=ImageTk.PhotoImage(file = 'icon\Plus_imaje.png'), width=100)
        self.button_minus = customtkinter.CTkButton(self, text=None, fg_color='#5B7065', image=ImageTk.PhotoImage(file = 'icon\Minus_image.png'), width=100)

        #grid
        self.grid_columnconfigure(0, weight=1)
        self.entry_input1.grid(row=0, column=0, padx=10, pady=10)
        #button
        self.button_plus.grid(row=1, column=0, padx=20, pady = 20)
        self.button_minus.grid(row=1, column=1, padx=20, pady = 20)

        #self.button_minus.pack(padx = 20, pady = 20)

        #self.entry_input2.pack(padx = 20, pady = 20)
        

        #self.button_plus.place(x = 5, y = 110)

    def button_callbck(self):
        print("Кнопка нажата")


app = Calculator()
app.mainloop()