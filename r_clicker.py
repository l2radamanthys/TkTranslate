try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


def r_clicker(e):
    """right click context menu for all Tk Entry and Text widgets"""

    try:
        def r_click_copy(e, apnd=0):
            e.widget.event_generate("<Control-c>")

        def r_click_cut(e):
            e.widget.event_generate("<Control-x>")

        def r_click_paste(e):
            e.widget.event_generate("<Control-v>")

        e.widget.focus()

        nclst = [
            (" Copiar", lambda e=e: r_click_copy(e)),
            (" Cortar", lambda e=e: r_click_cut(e)),
            (" Pegar", lambda e=e: r_click_paste(e)),
        ]

        rmenu = tk.Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")

    except tk.TclError:
        print(" - r_click menu, something wrong")
        pass

    return "break"


def r_click_binder(r):
    try:
        for b in ["Text", "Entry", "Listbox", "Label"]:
            r.bind_class(b, sequence="<Button-3>", func=r_clicker, add="")
    except tk.TclError:
        print(" - r_click_binder, something wrong")
        pass
