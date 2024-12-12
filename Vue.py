import tkinter as tk
from tkinter import messagebox


def enregistrer_joueur():
    prenom = ent_prenom.get()
    nom = ent_nom.get()
    date_naissance = ent_date_de_naissance.get()
    numero_ine = ent_numero_ine.get()
    donnees_joueur = (prenom, nom, date_naissance, numero_ine)

    if prenom == "":
        messagebox.showerror("Erreur", "veuillez saisir un Prénom valide !")
    elif nom == "":
        messagebox.showerror("Erreur", "veuillez saisir un Nom valide !")
    elif date_naissance == "":
        messagebox.showerror("Erreur", "veuillez saisir une Date de Naissance valide !")
    elif numero_ine == "":
        messagebox.showerror("Erreur", "veuillez saisir un Numéro INE valide !")
    else:
        return donnees_joueur


window = tk.Tk()
window.title("saisit de nouveau joueur")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack(padx=5, fill="both",expand=True)

frm_form.grid_rowconfigure(0, weight=1)
frm_form.grid_rowconfigure(1, weight=1)
frm_form.grid_rowconfigure(2, weight=1)
frm_form.grid_rowconfigure(3, weight=1)
frm_form.grid_columnconfigure(0, weight=1)
frm_form.grid_columnconfigure(1, weight=1)

lbl_prenom = tk.Label(master=frm_form, text="Prénom: ")
ent_prenom = tk.Entry(master=frm_form, width=50)
lbl_prenom.grid(row=0, column=0, sticky="nsew")
ent_prenom.grid(row=0, column=1, sticky="w")

lbl_nom = tk.Label(master=frm_form, text="Nom: ")
ent_nom = tk.Entry(master=frm_form, width=50)
lbl_nom.grid(row=1, column=0, sticky="nsew")
ent_nom.grid(row=1, column=1, sticky="w")

lbl_date_de_naissance = tk.Label(master=frm_form, text="Date de naissance: ")
ent_date_de_naissance = tk.Entry(master=frm_form, width=50)
lbl_date_de_naissance.grid(row=2, column=0, sticky="nsew")
ent_date_de_naissance.grid(row=2, column=1, sticky="w")

lbl_numero_ine = tk.Label(master=frm_form, text="Numero INE: ")
ent_numero_ine = tk.Entry(master=frm_form, width=50)
lbl_numero_ine.grid(row=3, column=0, sticky="nsew")
ent_numero_ine.grid(row=3, column=1, sticky="w")

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_valider = tk.Button(master=frm_buttons, text="Valider", command=enregistrer_joueur)
btn_valider.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_retour = tk.Button(master=frm_buttons, text="Retour")
btn_retour.pack(side=tk.RIGHT, ipadx=10)



window.mainloop()


