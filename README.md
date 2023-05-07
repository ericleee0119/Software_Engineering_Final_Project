# Software_Engineering_Final_Project

UI-
1. Instatiate dropdownmenu class- 
root = tk.Tk()
ddm = DropDownMenu(root)
root.mainloop()

2.run following code and choose city or pin type, the chosen value will then be return as (selected_option)
selected_option = ddm.get_selected_option()
if selected_option:
    print("Selected option:", selected_option)

