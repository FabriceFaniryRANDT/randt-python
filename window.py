import tkinter as tk
from tkinter import ttk

# Fonction pour gérer le clic sur le bouton
def on_button_click():
    label_var.set(f"Hello, {entry_var.get()}!")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Modern Tkinter Interface")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Style pour les widgets
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", 
                foreground="#FFFFFF", 
                background="#1ABC9C", 
                font=("Helvetica", 14),
                padding=10)

style.configure("TLabel", 
                foreground="#ECF0F1", 
                background="#2C3E50", 
                font=("Helvetica", 12))

style.configure("TEntry", 
                foreground="#2C3E50", 
                background="#ECF0F1", 
                font=("Helvetica", 12))

# Variables pour les widgets
entry_var = tk.StringVar()
label_var = tk.StringVar()

# Ajout des widgets
label = ttk.Label(root, text="Entrez votre nom:", style="TLabel")
label.pack(pady=20)

entry = ttk.Entry(root, textvariable=entry_var, width=30, style="TEntry")
entry.pack(pady=10)

button = ttk.Button(root, text="Cliquer ici", command=on_button_click, style="TButton")
button.pack(pady=20)

label_result = ttk.Label(root, textvariable=label_var, style="TLabel")
label_result.pack(pady=20)

# Lancement de l'application
root.mainloop()
