import seaborn as sns 
import matplotlib.pyplot as plt 
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import pandas as pd
import webbrowser
import os
#import gmplot
import plot_Factory as PF
import map

import finalproject_UI

#command: choose which plot to use -> UI -> call map
#plot name, line chart, histgram, map 2. data 3. UI chosen col, city, time, month
#call which plot -> (diff plots have diff UI)

#data = None

def Data_preprocess(data):
    
    data_mod = data
        
    '''data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
    data_mod['month'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[0]
    data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]'''


    #print(data_mod)
    '''data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
                            (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
                            (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
                            (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
                            (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]'''
    
    return data_mod

def File_input():
    global data
    file_name = input("csvFileName: ")
    try:
        data = pd.read_csv(file_name)
        data = Data_preprocess(data)
    except Exception as e:
        print(f"Error: {e}")
    

def Map_plot():
    # selected_options = finalproject_UI.UI()
    # chosen_city = selected_options[0]
    # chosen_plot = selected_options[1]
    # chosen_col = selected_options[2]
    
    mapPlot = PF.plot_Factory.create("map_plot", data)
    # mapPlot.create(data)

    mapPlot.draw("abc")

def Data_plot():
    # if not data:
    #     print("You need to inpu data file first, use File_input commend")
    #     return

    selected_options = finalproject_UI.UI()
    print("These are the elements:", end=".")
    print(*selected_options, sep=", ")
    
    #hard coding part
    chosen_city = selected_options[0]
    chosen_plot = selected_options[1]
    chosen_col = selected_options[2]
    print(chosen_city, chosen_plot, chosen_col)

    plot1 = PF.plot_Factory.create(chosen_plot, data)
    plot1.draw(chosen_col)


commands = {
    "File_input": File_input,
    "Data_plot": Data_plot,
    "Map_plot": Map_plot,
    "help": lambda: print("Available commands: help, quit, File_input, Data_plot, Map_plot")
}

def main():
    print("Welcome to the command line interface")
    while True:
        command = input("Enter a command: ")
        if command == "quit":
            print("Exiting...")
            break
        elif command in commands:
            func = commands[command]
            try:
                result = func()
                if command == "Map_plot":
                    print("check")
                    break
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

main()