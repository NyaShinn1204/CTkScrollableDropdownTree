from CTkDropdownTest import *
import customtkinter

root = customtkinter.CTk()

def on_dropdown_select(result):
    print("Columns:", result["columns"])
    print("Selected Values:", result["values"])

tree_values = ["Resolution", "FPS", "Size"]
values = [
    ["1080p","30","1G"],
    ["720p","30","700M"],
]

entry = customtkinter.CTkEntry(root, placeholder_text="Click to select")
entry.pack(pady=20, padx=20)
dropdown = CTkDropdownTest(
    attach=entry,
    height=200,
    width=300,
    values=values,
    tree_colum=tree_values,
    command=on_dropdown_select
)

root.mainloop()