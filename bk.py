import tkinter as tk
from customtkinter import *

class Myapp(CTk):
    def __init__(self):
        super().__init__()
        self.listodo = []
        self.geometry("300x600")
        self.initvalue = tk.StringVar(value="")

        self.txt = CTkEntry(self, placeholder_text="Name",
            textvariable=self.initvalue,
            font=("times",35)
            )
        self.txt.pack(pady=20)

        self.bt = CTkButton(self, text="add new todo", command=self.addnew)
        self.bt.pack(pady=10)

        self.frame = CTkFrame(self, fg_color="blue")
        self.frame.pack(fill="both", expand=True)

    def addnew(self):
        value = self.txt.get()
        self.listodo.append({"name": value})
        print(self.listodo)

        self.display_listodo()

    def display_listodo(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for i, item in enumerate(self.listodo):
            frame = CTkFrame(self.frame)
            frame.pack(fill="x", pady=15, padx=20)

            label = CTkLabel(frame, text=item["name"], font=("times", 20))
            label.pack(side="top", padx=5, pady=15)

            edit_button = CTkButton(frame, text="Edit", command=lambda idx=i: self.edit_item(idx))
            edit_button.pack(side="left", padx=5, pady=15)

            delete_button = CTkButton(frame, fg_color="red", text="Delete", command=lambda idx=i: self.delete_item(idx))
            delete_button.pack(side="left", padx=5, pady=15)

    def edit_item(self, index):
        if index < len(self.listodo):
            item = self.listodo[index]
            item_name = item["name"]
            self.initvalue = item_name
            self.bt.configure(text="Update", fg_color="yellow", text_color="black", command=lambda idx=index: self.update_item(idx))
        else:
            print("Invalid index")

    def update_item(self, index):
        if index < len(self.listodo):
            updated_value = self.txt.get()
            self.listodo[index]["name"] = updated_value
            print("Updated item at index", index)
            self.display_listodo()
            self.bt.configure(text="Add New Todo" ,
                fg_color="blue",
                command=self.addnew)
        else:
            print("Invalid index")

    def delete_item(self, index):
        if index < len(self.listodo):
            self.listodo.pop(index)
            print("Deleted item at index", index)
            self.display_listodo()
        else:
            print("Invalid index")

app = Myapp()
app.mainloop()
