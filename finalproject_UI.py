import tkinter as tk

class DropDownMenu:
    def __init__(self, parent):
        self.parent = parent
        self.options1 = ['ALL', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
        self.selected_option1 = tk.StringVar(parent)
        self.selected_option1.set(self.options1[0])

        self.options2 = ['year_order','month_order','time_order']
        self.selected_option2 = tk.StringVar(parent)
        self.selected_option2.set(self.options2[0])

        self.menu1 = tk.OptionMenu(parent, self.selected_option1, *self.options1)
        self.menu1.pack(side=tk.TOP, padx=10, pady=10)

        self.menu2 = tk.OptionMenu(parent, self.selected_option2, *self.options2)
        self.menu2.pack(side=tk.TOP, padx=10, pady=10)

        self.clicked_submit = False  # flag for Submit button click

        self.button = tk.Button(parent, text="Submit", command=self.on_options_select)
        self.button.pack(side=tk.TOP, padx=10, pady=10)

    def on_options_select(self):
        self.clicked_submit = True  # set flag to indicate Submit button has been clicked
        self.value1 = self.selected_option1.get()
        self.value2 = self.selected_option2.get()
        self.parent.after(0, self.parent.destroy)  # destroy window after the method has completed

    def get_selected_options(self):
        if self.clicked_submit:
            value1, value2 = self.value1, self.value2
            return value1, value2
        else:
            return None

def UI():
    root = tk.Tk()
    ddm = DropDownMenu(root)
    root.mainloop()
    
    
    # Check if Submit button was clicked and print selected options
    selected_options = ddm.get_selected_options()
    if selected_options:
        chosen_city, order = selected_options
    return chosen_city,order

#print(UI())
    