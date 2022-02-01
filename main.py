# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from application import Application
from r_clicker import r_click_binder


def main():
    root = tk.Tk()
    # root.geometry('640x480')
    app = Application(master=root)
    r_click_binder(app)
    app.mainloop()


if __name__ == "__main__":
    main()
