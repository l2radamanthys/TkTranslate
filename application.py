# -*- coding: utf-8 -*-

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from const import TRANSLATE_LIST, TRANSLATE_TABLE
from translate import translate



class Application(ttk.Frame):
    """
        Main app windows
    """
    def __init__(self, master=None):
        try:
            super().__init__(master)
        except:
            ttk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.init_ui()
        self.create_widgets()

    
    def init_ui(self):
        self.master.title('Tk Translate')
        self.master.resizable(0,0)
        # self.master.grab_set()


    def create_widgets(self):
        label = tk.Label(self, text='Traducir de:')
        label.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        self.combo = ttk.Combobox(self, state='readonly')
        self.combo['values'] = TRANSLATE_LIST
        self.combo.current(0)
        self.combo.grid(row=1, column=2, sticky=tk.W)
        self.input_text = tk.Text(self, height=5)
        self.input_text.grid(row=2, column=1, columnspan=5, padx=5, pady=5)
        self.output_text = tk.Text(self, height=5)
        self.output_text.grid(row=3, column=1, columnspan=5, padx=5, pady=5)
        self.button = tk.Button(self, text='Traducir', command=self.on_traslate_click, height=2, width=15)
        self.button.grid(row=4, column=5, sticky=tk.E, padx=5, pady=5)


    def on_traslate_click(self):
        source, target = TRANSLATE_TABLE[self.combo.current()]
        raw_text = self.input_text.get("1.0",'end-1c')
        self.output_text.delete(1.0, "end")
        result = translate(raw_text, source, target)
        self.output_text.insert("end", result)
        #print(options, raw_text)
