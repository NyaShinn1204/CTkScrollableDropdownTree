# CTkScrollableDropdownTree
Add a scrollable dropdown menu with an embedded tree

## Features
- Tree can only be embedded.
- That's all for now.

![Platform](https://img.shields.io/powershellgallery/p/Pester?color=blue)

![screenshots](https://github.com/user-attachments/assets/025ec723-92b6-4f18-b204-2efbcb70717b)
![screenshots](https://github.com/user-attachments/assets/fae8d5c6-b197-49ba-8ea1-6fe9060c69fe)


## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/NyaShinn1204/CTkScrollableDropdownTree?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/NyaShinn1204/CTkScrollableDropdownTree/archive/refs/heads/main.zip)

**Download from the source code, paste the `CTkScrollableDropdownTree` folder in the directory where your program is present.**

Note: IT'S SUPER BUG

## MOST Simple Usage
```python
CTkDropdownTest(attach=this_is_widget_name, values=values_list, tree_colum=tree_values_list)
```

## Example
```python
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


root.mainloop()
```

## Note:
This is a 99.999% copy of CTkScrollableDropdownFrame. It's for my own use, so I have no choice.

CTkScrollableDropdownFrame Link => https://github.com/Akascape/CTkScrollableDropdown
