import seaborn as sns 
import matplotlib.pyplot as plt 
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import pandas as pd
import webbrowser
import os
#import gmplot

import finalproject_UI

#command: choose which plot to use -> UI -> call map
#plot name, line chart, histgram, map 2. data 3. UI chosen col, city, time, month
#call which plot -> (diff plots have diff UI)

print("Welcome to the command line interface")
file_name = input("csvFileName: ")
#data = pd.read_csv(file_name)
data = []
plot_names = ['line_plot', 'histogram_plot']

print('Available plot names:')
for name in plot_names:
    print('- ' + name)
chosen_name = input('Enter the name of the plot you want to use: ')

# Check if the chosen name is in the list of plot names
if chosen_name in plot_names:
    print(f'You have chosen the {chosen_name} plot.')
else:
    print(f'{chosen_name} is not a valid plot name.')

chosen_city, order = finalproject_UI.UI()
print(f'You have chosen the {chosen_city} and {order}.')


def Data_preprocess(data):
    data_mod = data
    data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
    data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]

    data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
                            (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
                            (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
                            (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
                            (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]
    #print("data preprocessed")
    return data_mod

#data = Data_preprocess(data)


commands = {
    "help": lambda: print("Available commands: help, quit")
}

def main():
    while True:
        command = input("Enter a command: ")
        if command == "quit":
            print("Exiting...")
            break
        elif command in commands:
            func = commands[command]
            try:
                args = input("Enter the arguments (comma-separated): ").split(",")
                args = [float(x.strip()) for x in args]
                result = func(*args)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

main()