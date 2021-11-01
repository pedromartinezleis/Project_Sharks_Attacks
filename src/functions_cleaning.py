import pandas as pd
def x(df):
    if df['Sex '] == "F":
        i = "F"
    elif df['Sex '] == "M":
        i = "M"
    elif df['Sex '] == "nan":
        i = "Unknown"
    elif df['Sex '] == "M ":
        i = "M"
    elif df['Sex '] == "lli":
        i = "Unknown"
    elif df['Sex '] == "n":
        i = "Unknown"
    else:
        i = "Unknown"
    return i


def f(df):
    if df['Type'] == "Boating":
        val = "Yes"
    elif df['Type'] == "Unprovoked":
        val = "No"
    elif df['Type'] == "Invalid":
        val = "No"
    elif df['Type'] == "Provoked":
        val = "Yes"
    elif df['Type'] == "Questionable":
        val = "Yes"
    elif df['Type'] == "Sea Disaster":
        val = "Yes"
    elif df['Type'] == "Boat":
        val = "Yes"
    elif df['Type'] == "Boatomg":
        val = "Yes"
    elif df['Type'] == "Unknown":
        val = "Unknown"
    return val

def y(df):
    if df['Fatal (Y/N)'] == "N":
        i = "N"
    elif df['Fatal (Y/N)'] == "Y":
        i = "Y"
    elif df['Fatal (Y/N)'] == "nan":
        i = "Unknown"
    elif df['Fatal (Y/N)'] == "M":
        i = "Unknown"
    elif df['Fatal (Y/N)'] == "Unknown":
        i = "Unknown"
    elif df['Fatal (Y/N)'] == "2017":
        i = "Unknown"
    elif df['Fatal (Y/N)'] == " N":
        i = "N"
    elif df['Fatal (Y/N)'] == "N ":
        i = "N"
    elif df['Fatal (Y/N)'] == ", ":
        i = "Unknown"
    else:
        i = "Y"
    return i
def cambioYear(x):
    x= str(x)
    x = x.split(".")
    return int(x[0])