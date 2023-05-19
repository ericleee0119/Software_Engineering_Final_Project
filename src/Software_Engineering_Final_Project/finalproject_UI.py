import tkinter as tk
import registry

class DropDownMenu:
    def __init__(self, parent):
        self.parent = parent
        self.options1 = ['ALL', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
        self.selected_option1 = tk.StringVar(parent)
        self.selected_option1.set(self.options1[0])

        self.plot_options = list(registry.PlotRegistry.keys())
        self.selected_plot = tk.StringVar(parent)
        self.selected_plot.set(self.plot_options[0])

        self.col_options = list(registry.ColRegistry.keys())
        self.selected_col = tk.StringVar(parent)
        self.selected_col.set(self.col_options[0])

        self.menu1 = tk.OptionMenu(parent, self.selected_option1, *self.options1)
        self.menu1.pack(side=tk.TOP, padx=10, pady=10)

        self.menu_plot = tk.OptionMenu(parent, self.selected_plot, *self.plot_options)
        self.menu_plot.pack(side=tk.TOP, padx=10, pady=10)

        self.menu_col = tk.OptionMenu(parent, self.selected_col, *self.col_options)
        self.menu_col.pack(side=tk.TOP, padx=10, pady=10)

        self.clicked_submit = False  # flag for Submit button click

        self.button = tk.Button(parent, text="Submit", command=self.on_options_select)
        self.button.pack(side=tk.TOP, padx=10, pady=10)

    def on_options_select(self):
        self.clicked_submit = True  # set flag to indicate Submit button has been clicked
        self.value1 = self.selected_option1.get()
        self.selected_plot_value = self.selected_plot.get()
        self.selected_col_value = self.selected_col.get()
        self.parent.after(0, self.parent.destroy)  # destroy window after the method has completed

    def get_selected_options(self):
        if self.clicked_submit:
            value1, plot_value, col_value = self.value1, self.selected_plot_value, self.selected_col_value
            return value1, plot_value, col_value
        else:
            return None

def UI():
    root = tk.Tk()
    ddm = DropDownMenu(root)
    root.mainloop()
    
    # Check if Submit button was clicked and print selected options
    selected_options = ddm.get_selected_options()
    if selected_options:
        return selected_options
    return None

#print(UI())
    