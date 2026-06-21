import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "contacts.json"


# ---------- LOAD ----------
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                data = json.load(f)

                # SAFE FIX (id missing na add pannum)
                for i, c in enumerate(data):
                    if "id" not in c:
                        c["id"] = f"C{i+1:03d}"
                return data

        except:
            return []
    return []


# ---------- SAVE ----------
def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def generate_id():
    return f"C{len(contacts)+1:03d}"


# ---------- REFRESH ----------
def refresh_table(data=None):
    tree.delete(*tree.get_children())

    show = data if data else contacts

    for c in show:
        tree.insert("", "end", values=(
            c.get("id", ""),
            c.get("name", ""),
            c.get("phone", ""),
            c.get("email", ""),
            "⭐" if c.get("favorite") else ""
        ))

    update_dashboard()


def update_dashboard():
    lbl_total.config(text=f"Total Contacts: {len(contacts)}")
    lbl_fav.config(text=f"Favorites: {sum(1 for c in contacts if c.get('favorite'))}")


# ---------- ADD ----------
def add_contact():
    def save_new():
        contacts.append({
            "id": generate_id(),
            "name": e_name.get(),
            "phone": e_phone.get(),
            "email": e_email.get(),
            "address": e_address.get(),
            "favorite": fav_var.get()
        })

        save_contacts()
        refresh_table()
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Add Contact")

    tk.Label(win, text="Name").grid(row=0, column=0)
    tk.Label(win, text="Phone").grid(row=1, column=0)
    tk.Label(win, text="Email").grid(row=2, column=0)
    tk.Label(win, text="Address").grid(row=3, column=0)

    e_name = tk.Entry(win)
    e_phone = tk.Entry(win)
    e_email = tk.Entry(win)
    e_address = tk.Entry(win)

    e_name.grid(row=0, column=1)
    e_phone.grid(row=1, column=1)
    e_email.grid(row=2, column=1)
    e_address.grid(row=3, column=1)

    fav_var = tk.BooleanVar()
    tk.Checkbutton(win, text="Favorite", variable=fav_var).grid(row=4, columnspan=2)

    tk.Button(win, text="Save", command=save_new).grid(row=5, columnspan=2)


# ---------- DELETE ----------
def delete_contact():
    sel = tree.focus()
    if not sel:
        messagebox.showerror("Error", "Select contact")
        return

    cid = tree.item(sel)["values"][0]

    for c in contacts:
        if c.get("id") == cid:
            contacts.remove(c)
            break

    save_contacts()
    refresh_table()


# ---------- SEARCH ----------
def search_contact():
    key = search_entry.get().lower()

    result = [
        c for c in contacts
        if key in c.get("name","").lower()
        or key in c.get("phone","")
        or key in c.get("email","").lower()
    ]

    refresh_table(result)


def show_all():
    refresh_table()


def show_fav():
    refresh_table([c for c in contacts if c.get("favorite")])


# ---------- UI ----------
root = tk.Tk()
root.title("Contact Hub Pro")
root.geometry("900x550")

contacts = load_contacts()


# DASHBOARD
dash = tk.Frame(root)
dash.pack(fill="x")

lbl_total = tk.Label(dash, text="")
lbl_total.pack(side="left", padx=10)

lbl_fav = tk.Label(dash, text="")
lbl_fav.pack(side="left", padx=10)


# SEARCH
top = tk.Frame(root)
top.pack(fill="x", pady=5)

search_entry = tk.Entry(top, width=40)
search_entry.pack(side="left", padx=10)

tk.Button(top, text="Search", command=search_contact).pack(side="left")
tk.Button(top, text="All", command=show_all).pack(side="left")
tk.Button(top, text="Fav", command=show_fav).pack(side="left")


# TABLE
cols = ("ID", "Name", "Phone", "Email", "Fav")

tree = ttk.Treeview(root, columns=cols, show="headings")

for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=150)

tree.pack(fill="both", expand=True)


# BUTTONS
btn = tk.Frame(root)
btn.pack(pady=10)

tk.Button(btn, text="Add", command=add_contact).pack(side="left", padx=10)
tk.Button(btn, text="Delete", command=delete_contact).pack(side="left", padx=10)


refresh_table()
root.mainloop()