import tkinter as tk
from customtkinter import *

class MyApp(CTk):
    def __init__(self):
        super().__init__()
        # SET YOU WINDOW SIZE
        self.geometry("300x600")
        self.listodo = []
        self.initvalue = tk.StringVar(value="")

        # NOW CREATE TEXTBOX 
        self.txt = CTkEntry(
            self,placeholder_text="insert here",
            textvariable=self.initvalue,
            # AND SET FONT SIZE IN TEXTBOX
            font=("times",35)
            )
        self.txt.pack(pady=20)

        # ADD BUTTON
        self.bt = CTkButton(
            self,text="YOu add here",
            command=self.addnew
            )
        self.bt.pack(pady=10)

        # AND NOW CREATE FRAME FOR SEE YOU INPUT TODO
        # IN BOTTOM BUTTON 
        self.frame = CTkFrame(self,
            # ADD BGCOLOR
            fg_color="blue",
            )
        # AND SET FULL WIDTH AND FULL HEIGHT
        self.frame.pack(fill="both",expand=True)

    def addnew(self):
        # AND NOW ADD NEW TODO FUNCTION HERE
        # GET VALUE YOU INPUT
        value = self.txt.get()
        # AND YOU INPUT ADD TO listodo
        self.listodo.append({
            "name":value
            })
        print(self.listodo)

        # AND NOW I WILL CREATE REFRESH FUNCTION
        # FOR SEE DATA IN listodo
        self.display_listodo()



    def display_listodo(self):
        for w in self.frame.winfo_children():
            # DESTROY ALL
            w.destroy()
        # AND ADD TO FRAME AGAIN

        for i,item in enumerate(self.listodo):
            frame = CTkFrame(self.frame)
            frame.pack(fill="both",pady=15,padx=20)

            # AND NOW I WILL SET LAYOUT TEXT 
            # AND 2 BUTTON EDIT AND DELETE
            label = CTkLabel(
                frame,text=item['name'],
                font=("times",20)
                )
            # AND SET TO TOP FRAME 
            label.pack(side="top",padx=5,pady=15)

            # AND CREATE 2 BUTTON EDIT AND DELETE
            edit = CTkButton(frame,text="Edit",
                command=lambda idx=i:self.edit_item(idx)
                )
            edit.pack(side="left",padx=5,pady=15)

            # AND FOR DELETE BUTTON
            delete = CTkButton(frame,text="Edit",
                fg_color="red",
                command=lambda idx=i:self.delete_item(idx)
                )
            delete.pack(side="left",padx=5,pady=15)

    def edit_item(self,index):
        if index < len(self.listodo):
            # AND GET AND FIND BY INDEX
            item = self.listodo[index]
            item_name = item['name']
            # AND SET TO TEXTBOX
            self.initvalue =   item_name 
            # AND CHANGE COLOR BUTTON TO YELLOW
            # AND CHANGE NAME BUTTON
            self.bt.configure(text="Update",
                fg_color="yellow",
                text_color="black",
                command=lambda idx=index:self.update_item(idx)
                )
        else:
            print("invalid index you .....")

    def update_item(self,index):
        # AND NOW IF YOU CLICK BUTTON UPDATE
        # THEN UPDATE TO DATA 
        if index < len(self.listodo):
            # GET VALUE TEXTBOX
            update_value = self.txt.get()
            # AND UPDATE 
            self.listodo[index]['name'] = update_value
            # AND REFRESH FRAME
            self.display_listodo()

            # AND BUTTON YELLOW UPDATE CHANGE TO NORMAL
            # AGAIN
            self.bt.configure(text="Add now",
                fg_color="blue",
            command=self.addnew
                )
        else:
            print("invalid index")



    def delete_item(self,index):
        # AND NOW FOR DELETE 
        if index < len(self.listodo):
            # AND REMOVE BY INDEX
            self.listodo.pop(index)
            # AND REFRESH AGAIN
            self.display_listodo()
        else:
            print("YOU VALD DELETE INDEX...")



app = MyApp()
app.mainloop()