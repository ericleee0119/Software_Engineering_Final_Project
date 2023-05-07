import seaborn as sns 
import matplotlib.pyplot as plt 
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import pandas as pd
import webbrowser
import os
#import gmplot
apikey = 'gmap = gmplot.GoogleMapPlotter.from_geocode("New York, USA", apikey=apikey)'

#call which plot -> (diff plots have diff UI)

file_name = input("csvFileName: ")
data = pd.read_csv(file_name)

def Data_preprocess(data):
    data_mod = data
    data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
    data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]

    data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
                            (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
                            (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
                            (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
                            (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]
    data = data_mod
    print("data preprocessed and stored in data")
    return data_mod

commands = {
    "Data_preprocess": Data_preprocess,
    "help": lambda: print("Available commands: Data_preprocess, help, quit")
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
                args = input("Enter the arguments (comma-separated): ").split(",")
                args = [float(x.strip()) for x in args]
                result = func(*args)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

main()