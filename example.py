from CTkDropdownTest import *
import customtkinter

root = customtkinter.CTk()

# Some option list
tree_values = [
    "Resolution", "FPS", "Size"
]
values = [
    ["1080p","30","1G"],
    ["720p","30","700M"],
]

# Attach! 
entry = customtkinter.CTkEntry(root, placeholder_text="Click to select")
entry.pack(pady=20, padx=20)

CTkDropdownTest(
    attach=entry,
    values=values,
    tree_colum=tree_values
)

# Attach for Optionmenu!
option_menu = customtkinter.CTkOptionMenu(root, values=["Select an option"])
option_menu.pack(pady=20, padx=20)

CTkDropdownTest(
    attach=option_menu,
    values=values,
    tree_colum=tree_values
)


# Click to colum
def on_dropdown_select(result):
    print("Columns:", result["columns"])
    print("Selected Values:", result["values"])

entry = customtkinter.CTkEntry(root, placeholder_text="Click to select")
entry.pack(pady=20, padx=20)

CTkDropdownTest(
    attach=entry, values=values, tree_colum=tree_values, command=on_dropdown_select
)

# Set background for tree!

option_menu = customtkinter.CTkOptionMenu(root, values=["Select an option"])
option_menu.pack(pady=20, padx=20)

CTkDropdownTest(
    attach=option_menu,
    values=values,
    tree_colum=tree_values,
    tree_bg_color="red",
    tree_fg_color="blue"
)


root.mainloop()