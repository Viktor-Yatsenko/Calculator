import settings
import gui

import customtkinter

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap(settings.WINDOW_ICON)
        self.title(settings.TITLE)
        self.geometry(settings.WINDOW_SIZE)
        self.resizable(False, False)
        self.configure(fg_color=settings.WINDOW_BG_COLOR)

        #Grid
        self.grid_columnconfigure(0, weight=1)

        self.entry_frame = gui.EntryFrame(master=self)
        self.entry_frame.grid(row=1, column=0, padx=20, pady=20)

        self.buttons_frame = gui.ButtonsFrame(master=self)
        self.buttons_frame.grid(row=2, column=0, padx=10, pady=20)

app = Calculator()
app.mainloop()