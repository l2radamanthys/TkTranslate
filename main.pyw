# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from application import Application


def main():
    root = tk.Tk()
    # root.geometry('640x480')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
