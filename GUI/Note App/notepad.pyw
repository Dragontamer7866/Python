import tkinter as tk

history = []

BG_COLOR = "#F4F6F7"
WARNING = "#C0392B"

def submit_stuff():
    text = entry0.get()
    if text:
        notes_listbox.insert(tk.END, text)
        entry0.delete(0, tk.END)
        
def clear_stuff():
    history.clear()
    notes_listbox.delete(0, tk.END)

def limit_text(proposed_text):
    MAX_LIMIT = 150
    return len(proposed_text) <= MAX_LIMIT

def remove_selected():
    try:
        selected_index = notes_listbox.curselection()[0]
        notes_listbox.delete(selected_index)
    except IndexError:
        pass

root = tk.Tk()

try:
    icon = tk.PhotoImage(file='notepad-icon.png')
    root.iconphoto(True, icon)
except Exception:
    pass

root.title("Notes App")
root.config(padx=20, pady=20)

val_command = (root.register(limit_text), '%P')

tk.Label(root, text="WARNING: NOTES DO NOT SAVE.", font=("Helvetica", 10, "bold"), fg=WARNING).grid(row=0, column=0, sticky="w", pady=(0, 15))

input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0, sticky="w", pady=(5, 15))

tk.Label(input_frame, text="Make Note: ").pack(side="left")
entry0 = tk.Entry(input_frame, width=45, validate="key", validatecommand=val_command)
entry0.pack(side="left", padx=5)
submit0 = tk.Button(input_frame, text="Submit", cursor="hand2", command=submit_stuff)
submit0.pack(side="left", padx=5)

history_frame = tk.LabelFrame(root, text="Last 5 Notes:", font=("Helvetica", 10, "bold"), relief="solid", bd=1, padx=12, pady=12)
history_frame.grid(row=2, column=0, sticky="we", pady=(5, 15))

notes_listbox = tk.Listbox(history_frame, width=50, height=10, relief="flat", highlightthickness=0)
notes_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(history_frame, orient="vertical", command=notes_listbox.yview)
scrollbar.pack(side="right", fill="y")
notes_listbox.config(yscrollcommand=scrollbar.set)

control_frame = tk.Frame(root)
control_frame.grid(row=3, column=0, sticky="e", pady=(10, 0))

tk.Button(control_frame, text="Remove Selected", cursor="hand2", command=remove_selected, fg="#C0392B").pack(side="left", padx=5)
tk.Button(control_frame, text="Clear", cursor="hand2", command=clear_stuff).pack(side="left", padx=5)
tk.Button(control_frame, text="Exit", cursor="hand2", command=root.destroy).pack(side="left", padx=5)

root.mainloop()