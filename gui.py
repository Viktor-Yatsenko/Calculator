import settings
import calculate_functions as cf

import customtkinter

class EntryFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs,
            fg_color=settings.WINDOW_BG_COLOR,
        )

        self.entry_input1 = customtkinter.CTkEntry(
            self,
            placeholder_text='Введіть перше число',
            fg_color=settings.WINDOW_BG_COLOR,
            border_color=settings.FRAME_BORDER_COLOR,
            height=30,
            width=150,
            #textvariable=self.number1
        )
        number1=customtkinter.IntVar()
        number1.get()
        
        self.entry_input2 = customtkinter.CTkEntry(
            self,
            placeholder_text='Введіть друге число',
            fg_color=settings.WINDOW_BG_COLOR,
            border_color=settings.FRAME_BORDER_COLOR,
            height=30,
            width=150,
            #textvariable=self.number2
        )
        number2=customtkinter.IntVar()
        number2.get()
        
        
        self.entry_input1.grid(row=0, column=0, padx=20, pady=5)
        self.entry_input2.grid(row=1, column=0, padx=20, pady=5)


class ButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master, 
            **kwargs, 
            border_width=settings.FRAME_BORDER_WIDTH,
            border_color=settings.FRAME_BORDER_COLOR,
            fg_color=settings.WINDOW_BG_COLOR
            )
        
        self.button_clear = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='C',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_brackets = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='( )',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_percent = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='%',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_division = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='/',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_multiplication = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='*',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_minus = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='-',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        
        self.button_plus = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='+',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50,
            #command=cf.button_one_press
        )

        self.button_total = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='=',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_coma = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text=',',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_plus_minus = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='+/-',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_zero = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='0',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_one = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='1',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_two = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='2',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_three = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='3',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_four = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='4',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_five = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='5',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_six = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='6',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_seven = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='7',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_eight = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='8',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )
        self.button_nine = customtkinter.CTkButton(
            self,
            font=customtkinter.CTkFont(size=settings.FONT_SIZE),
            text='9',
            fg_color=settings.BUTTON_FUNK_BG_COLOR,
            height=50,
            width=50
        )


        self.button_clear.grid           (row=0, column=0, padx=10, pady=10)
        self.button_brackets.grid        (row=0, column=1, padx=10, pady=10)
        self.button_percent.grid         (row=0, column=2, padx=10, pady=10)
        self.button_division.grid        (row=0, column=3, padx=10, pady=10)

        self.button_seven.grid           (row=1, column=0, padx=10, pady=10)
        self.button_eight.grid           (row=1, column=1, padx=10, pady=10)
        self.button_nine.grid            (row=1, column=2, padx=10, pady=10)
        self.button_multiplication.grid  (row=1, column=3, padx=10, pady=10)

        self.button_four.grid            (row=2, column=0, padx=10, pady=10)
        self.button_five.grid            (row=2, column=1, padx=10, pady=10)
        self.button_six.grid             (row=2, column=2, padx=10, pady=10)
        self.button_minus.grid           (row=2, column=3, padx=10, pady=10)

        self.button_one.grid             (row=3, column=0, padx=10, pady=10)
        self.button_two.grid             (row=3, column=1, padx=10, pady=10)
        self.button_three.grid           (row=3, column=2, padx=10, pady=10)
        self.button_plus.grid            (row=3, column=3, padx=10, pady=10)

        self.button_plus_minus.grid      (row=4, column=0, padx=10, pady=10)
        self.button_zero.grid            (row=4, column=1, padx=10, pady=10)
        self.button_coma.grid            (row=4, column=2, padx=10, pady=10)
        self.button_total.grid           (row=4, column=3, padx=10, pady=10)