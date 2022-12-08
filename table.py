# Python program to convert
# CSV to HTML Table


import pandas as pd
# JAKARTA BARAT
# to read csv file named "sample"
a = pd.read_csv("./dataset/JakartaBarat.csv")

# to save as html file
# named as "Table"
a.to_html("./templates/rs_jakbar.html")

# assign it to a
# variable (string)
html_file = a.to_html()

# JAKARTA PUSAT
a = pd.read_csv("./dataset/JakartaPusat.csv")

a.to_html("./templates/rs_jakpus.html")

html_file = a.to_html()

# JAKARTA SELATAN
a = pd.read_csv("./dataset/JakartaSelatan.csv")

a.to_html("./templates/rs_jaksel.html")

html_file = a.to_html()

# JAKARTA TIMUR
a = pd.read_csv("./dataset/JakartaTimur.csv")

a.to_html("./templates/rs_jaktim.html")

html_file = a.to_html()

# JAKARTA UTARA
a = pd.read_csv("./dataset/JakartaUtara.csv")

a.to_html("./templates/rs_jakut.html")

html_file = a.to_html()