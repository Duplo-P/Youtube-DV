import tkinter as tk
from tkinter.ttk import Progressbar
from tqdm import tqdm
import time

#Funções
def baixar():
    for i in tqdm(range(100)):
        # Simulando uma tarefa demorada
        time.sleep(0.1)
        pgb_baixar['value'] = i
        root.update_idletasks()

#Fontes
fonte_titulo = ("arial", 20, "bold")
fonte = ("verdana", 12)
#tela principal
root = tk.Tk()
root.geometry("600x400")
root.title("Youtube - DV")
lbl_main = tk.Label(root, text = "YOUTUBE DV", font = fonte_titulo)
lbl_main.pack(pady = 30)

#Frame link
frm_main = tk.Frame(root)

frm_bar = tk.Frame(frm_main)
pgb_baixar = Progressbar(frm_bar, orient="vertical", length=200, mode="determinate", maximum=99)
pgb_baixar.pack(fill = "x")
frm_bar.grid(row = 0, column = 0, padx = 10)

frm_link = tk.Frame(frm_main, borderwidth = 5, relief = "raised")
lbl_link = tk.Label(frm_link, text = "Colar link -> ", font = fonte )
lbl_link.grid(row = 0, column = 0)
en_link = tk.Entry(frm_link, width = 40)
en_link.grid(row = 0, column =1, padx = 10 )
frm_link.grid(row = 0, column = 1, pady = 10)
#botão
btb_baixar = tk.Button(frm_link, text = "Baixar", width = 12, height = 2, command = baixar)
btb_baixar.grid(row = 1, column = 1, pady = 15)


frm_main.pack()



root.mainloop()